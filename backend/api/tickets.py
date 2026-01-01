from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.db import get_db
from core.deps import get_current_user
from models import (
    Ticket,
    TicketAttachment,
    TicketComment,
    TicketStatus,
    TicketStatusHistory,
    User,
    UserRole,
)
from schemas.ticket import (
    TicketAttachmentCreate,
    TicketAttachmentOut,
    TicketCommentCreate,
    TicketCommentOut,
    TicketCreate,
    TicketOut,
    TicketUpdate,
)
from services.audit import log_audit, serialize_model
from services.tickets import calculate_due_date

router = APIRouter(prefix="/tickets", tags=["tickets"])


def _ticket_queryset(db: Session, user: User):
    query = db.query(Ticket)
    if user.role == UserRole.RESIDENT:
        return query.filter(Ticket.resident_id == user.id)
    if user.role == UserRole.MASTER:
        return query.filter(Ticket.assigned_to_id == user.id)
    return query


@router.get("", response_model=list[TicketOut])
def list_tickets(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return _ticket_queryset(db, current_user).order_by(Ticket.created_at.desc()).all()


@router.post("", response_model=TicketOut)
def create_ticket(
    payload: TicketCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role != UserRole.RESIDENT:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only residents can create tickets")
    status = db.query(TicketStatus).filter(TicketStatus.key == "NEW").first()
    ticket = Ticket(
        title=payload.title,
        description=payload.description,
        category_id=payload.category_id,
        priority_id=payload.priority_id,
        status_id=status.id if status else None,
        resident_id=current_user.id,
        due_date=calculate_due_date(db, payload.priority_id),
    )
    db.add(ticket)
    db.flush()
    log_audit(
        db,
        actor_id=current_user.id,
        action="ticket_created",
        entity_type="Ticket",
        entity_id=ticket.id,
        before=None,
        after=serialize_model(ticket),
    )
    db.commit()
    db.refresh(ticket)
    return ticket


@router.get("/{ticket_id}", response_model=TicketOut)
def get_ticket(
    ticket_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ticket = _ticket_queryset(db, current_user).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    return ticket


@router.patch("/{ticket_id}", response_model=TicketOut)
def update_ticket(
    ticket_id: int,
    payload: TicketUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ticket = _ticket_queryset(db, current_user).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    if current_user.role == UserRole.RESIDENT and ticket.resident_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")

    before = serialize_model(ticket)
    if payload.title is not None:
        ticket.title = payload.title
    if payload.description is not None:
        ticket.description = payload.description
    if payload.category_id is not None:
        ticket.category_id = payload.category_id
    if payload.priority_id is not None:
        ticket.priority_id = payload.priority_id
        ticket.due_date = calculate_due_date(db, payload.priority_id)
    if payload.assigned_to_id is not None:
        ticket.assigned_to_id = payload.assigned_to_id
    if payload.status_id is not None:
        history = TicketStatusHistory(
            ticket_id=ticket.id,
            from_status_id=ticket.status_id,
            to_status_id=payload.status_id,
            changed_by_id=current_user.id,
        )
        db.add(history)
        ticket.status_id = payload.status_id

    log_audit(
        db,
        actor_id=current_user.id,
        action="ticket_updated",
        entity_type="Ticket",
        entity_id=ticket.id,
        before=before,
        after=serialize_model(ticket),
    )
    db.commit()
    db.refresh(ticket)
    return ticket


@router.post("/{ticket_id}/comments", response_model=TicketCommentOut)
def add_comment(
    ticket_id: int,
    payload: TicketCommentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ticket = _ticket_queryset(db, current_user).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    comment = TicketComment(
        ticket_id=ticket.id,
        author_id=current_user.id,
        content=payload.content,
        is_internal=payload.is_internal,
    )
    db.add(comment)
    db.flush()
    log_audit(
        db,
        actor_id=current_user.id,
        action="ticket_commented",
        entity_type="TicketComment",
        entity_id=comment.id,
        before=None,
        after=serialize_model(comment),
    )
    db.commit()
    db.refresh(comment)
    return comment


@router.post("/{ticket_id}/attachments", response_model=TicketAttachmentOut)
def add_attachment(
    ticket_id: int,
    payload: TicketAttachmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ticket = _ticket_queryset(db, current_user).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    attachment = TicketAttachment(
        ticket_id=ticket.id,
        file_name=payload.file_name,
        file_url=payload.file_url,
    )
    db.add(attachment)
    db.flush()
    log_audit(
        db,
        actor_id=current_user.id,
        action="ticket_attachment_added",
        entity_type="TicketAttachment",
        entity_id=attachment.id,
        before=None,
        after=serialize_model(attachment),
    )
    db.commit()
    db.refresh(attachment)
    return attachment

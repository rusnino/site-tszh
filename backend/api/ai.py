from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.db import get_db
from core.deps import require_roles
from models import AISuggestion, Ticket, TicketCategory, TicketPriority, User, UserRole
from schemas.ai import AISuggestRequest, AISuggestResponse
from services.audit import log_audit, serialize_model

router = APIRouter(prefix="/ai", tags=["ai"])


KEYWORDS = [
    ("протеч", "Сантехника", "Высокий"),
    ("канализа", "Сантехника", "Высокий"),
    ("свет", "Электрика", "Средний"),
    ("лифт", "Лифт", "Средний"),
    ("уборк", "Благоустройство", "Низкий"),
]


def _match_rule(text: str):
    lowered = text.lower()
    for keyword, category_name, priority_name in KEYWORDS:
        if keyword in lowered:
            return category_name, priority_name
    return None, None


def _find_by_name(db: Session, model, name: str | None):
    if not name:
        return None
    return db.query(model).filter(model.name == name).first()


@router.post("/suggest", response_model=AISuggestResponse)
def suggest(
    payload: AISuggestRequest,
    db: Session = Depends(get_db),
    _: User = Depends(require_roles([UserRole.DISPATCHER, UserRole.ADMIN, UserRole.MANAGER])),
):
    ticket = db.get(Ticket, payload.ticket_id)
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")

    category_name, priority_name = _match_rule(f"{ticket.title} {ticket.description}")
    category = _find_by_name(db, TicketCategory, category_name)
    priority = _find_by_name(db, TicketPriority, priority_name)

    duplicates = (
        db.query(Ticket)
        .filter(Ticket.id != ticket.id)
        .filter(Ticket.title.ilike(f"%{ticket.title[:20]}%"))
        .limit(5)
        .all()
    )
    duplicate_ids = [dup.id for dup in duplicates] if duplicates else None

    suggested_reply = (
        "Спасибо за обращение. Заявка зарегистрирована и передана в работу. "
        "Мы сообщим о ходе выполнения в личном кабинете."
    )

    suggestion = AISuggestion(
        ticket_id=ticket.id,
        suggested_category_id=category.id if category else None,
        suggested_priority_id=priority.id if priority else None,
        suggested_reply=suggested_reply,
        duplicate_ticket_ids=duplicate_ids,
    )
    db.add(suggestion)
    db.flush()
    log_audit(
        db,
        actor_id=None,
        action="ai_suggested",
        entity_type="AISuggestion",
        entity_id=suggestion.id,
        before=None,
        after=serialize_model(suggestion),
    )
    db.commit()
    db.refresh(suggestion)
    return AISuggestResponse(
        suggestion_id=suggestion.id,
        suggested_category_id=suggestion.suggested_category_id,
        suggested_priority_id=suggestion.suggested_priority_id,
        suggested_reply=suggestion.suggested_reply,
        duplicate_ticket_ids=suggestion.duplicate_ticket_ids,
    )

from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from models import TicketPriority


def calculate_due_date(db: Session, priority_id: int | None) -> datetime | None:
    if not priority_id:
        return None
    priority = db.get(TicketPriority, priority_id)
    if not priority:
        return None
    return datetime.utcnow() + timedelta(hours=priority.sla_hours)

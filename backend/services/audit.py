from datetime import datetime
from typing import Any

from sqlalchemy.orm import Session

from models import AuditLog


def log_audit(
    db: Session,
    actor_id: int | None,
    action: str,
    entity_type: str,
    entity_id: int | None,
    before: dict | None,
    after: dict | None,
) -> AuditLog:
    log = AuditLog(
        actor_id=actor_id,
        action=action,
        entity_type=entity_type,
        entity_id=entity_id,
        before_json=before,
        after_json=after,
        created_at=datetime.utcnow(),
    )
    db.add(log)
    return log


def serialize_model(model: Any) -> dict | None:
    if model is None:
        return None
    data: dict[str, Any] = {}
    for column in model.__table__.columns:
        value = getattr(model, column.name)
        data[column.name] = value
    return data

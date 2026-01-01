from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.db import get_db
from core.deps import require_roles
from models import AuditLog, User, UserRole
from schemas.admin import AdminUserOut, AuditLogOut

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/users", response_model=list[AdminUserOut])
def list_users(
    db: Session = Depends(get_db),
    _: User = Depends(require_roles([UserRole.ADMIN, UserRole.MANAGER])),
):
    return db.query(User).order_by(User.id).all()


@router.get("/audit", response_model=list[AuditLogOut])
def list_audit_logs(
    db: Session = Depends(get_db),
    _: User = Depends(require_roles([UserRole.ADMIN, UserRole.MANAGER])),
):
    return db.query(AuditLog).order_by(AuditLog.created_at.desc()).limit(500).all()

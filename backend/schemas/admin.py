from datetime import datetime

from pydantic import BaseModel, EmailStr

from models.enums import UserRole


class AdminUserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    role: UserRole
    building_id: int | None = None
    apartment_id: int | None = None

    class Config:
        from_attributes = True


class AuditLogOut(BaseModel):
    id: int
    actor_id: int | None
    action: str
    entity_type: str
    entity_id: int | None
    before_json: dict | None
    after_json: dict | None
    created_at: datetime

    class Config:
        from_attributes = True

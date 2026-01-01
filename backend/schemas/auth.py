from pydantic import BaseModel, EmailStr

from models.enums import UserRole


class UserCreate(BaseModel):
    email: EmailStr
    full_name: str
    password: str
    role: UserRole | None = None
    building_id: int | None = None
    apartment_id: int | None = None


class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    role: UserRole
    building_id: int | None = None
    apartment_id: int | None = None

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenPair(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

from datetime import datetime

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.enums import UserRole


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    full_name: Mapped[str] = mapped_column(String(255))
    password_hash: Mapped[str] = mapped_column(String(255))
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), index=True)

    building_id: Mapped[int | None] = mapped_column(ForeignKey("buildings.id"), nullable=True)
    apartment_id: Mapped[int | None] = mapped_column(ForeignKey("apartments.id"), nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    building = relationship("Building", back_populates="users")
    apartment = relationship("Apartment", back_populates="residents")
    tickets = relationship("Ticket", back_populates="resident", foreign_keys="Ticket.resident_id")
    assigned_tickets = relationship("Ticket", back_populates="assigned_to", foreign_keys="Ticket.assigned_to_id")

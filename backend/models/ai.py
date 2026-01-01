from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, JSON, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class AISuggestion(Base):
    __tablename__ = "ai_suggestions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ticket_id: Mapped[int] = mapped_column(ForeignKey("tickets.id"))
    suggested_category_id: Mapped[int | None] = mapped_column(ForeignKey("ticket_categories.id"), nullable=True)
    suggested_priority_id: Mapped[int | None] = mapped_column(ForeignKey("ticket_priorities.id"), nullable=True)
    suggested_reply: Mapped[str | None] = mapped_column(Text, nullable=True)
    duplicate_ticket_ids: Mapped[list[int] | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    ticket = relationship("Ticket")
    category = relationship("TicketCategory")
    priority = relationship("TicketPriority")

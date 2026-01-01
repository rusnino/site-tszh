from datetime import datetime

from pydantic import BaseModel


class TicketBase(BaseModel):
    title: str
    description: str


class TicketCreate(TicketBase):
    category_id: int | None = None
    priority_id: int | None = None


class TicketUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    category_id: int | None = None
    priority_id: int | None = None
    status_id: int | None = None
    assigned_to_id: int | None = None
    due_date: datetime | None = None


class TicketCommentCreate(BaseModel):
    content: str
    is_internal: bool = False


class TicketAttachmentCreate(BaseModel):
    file_name: str
    file_url: str


class TicketOut(BaseModel):
    id: int
    title: str
    description: str
    category_id: int | None
    priority_id: int | None
    status_id: int | None
    resident_id: int
    assigned_to_id: int | None
    due_date: datetime | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class TicketCommentOut(BaseModel):
    id: int
    ticket_id: int
    author_id: int
    content: str
    is_internal: bool
    created_at: datetime

    class Config:
        from_attributes = True


class TicketAttachmentOut(BaseModel):
    id: int
    ticket_id: int
    file_name: str
    file_url: str
    uploaded_at: datetime

    class Config:
        from_attributes = True

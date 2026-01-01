from pydantic import BaseModel


class AISuggestRequest(BaseModel):
    ticket_id: int


class AISuggestResponse(BaseModel):
    suggestion_id: int
    suggested_category_id: int | None
    suggested_priority_id: int | None
    suggested_reply: str | None
    duplicate_ticket_ids: list[int] | None

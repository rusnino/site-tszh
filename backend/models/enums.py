from enum import Enum


class UserRole(str, Enum):
    RESIDENT = "RESIDENT"
    DISPATCHER = "DISPATCHER"
    MASTER = "MASTER"
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"


class TicketStatusKey(str, Enum):
    NEW = "NEW"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
    CLOSED = "CLOSED"

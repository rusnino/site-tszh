from datetime import datetime

from core.db import SessionLocal
from core.security import hash_password
from models import (
    Apartment,
    Building,
    Ticket,
    TicketCategory,
    TicketPriority,
    TicketStatus,
    User,
    UserRole,
)


def seed():
    db = SessionLocal()
    try:
        if db.query(User).first():
            return

        building = Building(name="ЖК Солнечный", address="г. Москва, ул. Примерная, 10")
        db.add(building)
        db.flush()

        apartments = [
            Apartment(building_id=building.id, number="101", floor=1),
            Apartment(building_id=building.id, number="102", floor=1),
            Apartment(building_id=building.id, number="201", floor=2),
        ]
        db.add_all(apartments)

        categories = [
            TicketCategory(name="Сантехника", description="Протечки, трубы, канализация"),
            TicketCategory(name="Электрика", description="Освещение, проводка"),
            TicketCategory(name="Лифт", description="Неисправности лифта"),
            TicketCategory(name="Благоустройство", description="Уборка, двор, снег"),
        ]
        priorities = [
            TicketPriority(name="Высокий", sla_hours=8),
            TicketPriority(name="Средний", sla_hours=24),
            TicketPriority(name="Низкий", sla_hours=72),
        ]
        statuses = [
            TicketStatus(key="NEW", name="Новая"),
            TicketStatus(key="IN_PROGRESS", name="В работе"),
            TicketStatus(key="DONE", name="Выполнена"),
            TicketStatus(key="CLOSED", name="Закрыта"),
        ]
        db.add_all(categories + priorities + statuses)
        db.flush()

        users = [
            User(
                email="resident@example.com",
                full_name="Иван Житель",
                password_hash=hash_password("password"),
                role=UserRole.RESIDENT,
                building_id=building.id,
                apartment_id=apartments[0].id,
            ),
            User(
                email="dispatcher@example.com",
                full_name="Ольга Диспетчер",
                password_hash=hash_password("password"),
                role=UserRole.DISPATCHER,
                building_id=building.id,
            ),
            User(
                email="master@example.com",
                full_name="Павел Мастер",
                password_hash=hash_password("password"),
                role=UserRole.MASTER,
                building_id=building.id,
            ),
            User(
                email="admin@example.com",
                full_name="Алексей Администратор",
                password_hash=hash_password("password"),
                role=UserRole.ADMIN,
                building_id=building.id,
            ),
            User(
                email="manager@example.com",
                full_name="Марина Руководитель",
                password_hash=hash_password("password"),
                role=UserRole.MANAGER,
                building_id=building.id,
            ),
        ]
        db.add_all(users)
        db.flush()

        ticket = Ticket(
            title="Протечка в ванной",
            description="Обнаружена протечка под раковиной, требуется осмотр.",
            category_id=categories[0].id,
            priority_id=priorities[0].id,
            status_id=statuses[0].id,
            resident_id=users[0].id,
            assigned_to_id=users[2].id,
            due_date=datetime.utcnow(),
        )
        db.add(ticket)

        db.commit()
    finally:
        db.close()


if __name__ == "__main__":
    seed()

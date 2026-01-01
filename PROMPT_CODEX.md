SYSTEM ROLE:
You are Codex. Generate code and project files only. No explanations unless explicitly requested.

========================
ЗАДАЧА (RU)
========================

Нужно сгенерировать MVP веб-проекта для ТСЖ / Управляющей компании в РФ.

Проект включает:
- публичный сайт
- личный кабинет жильца
- административную панель
- систему заявок от жильцов (журналирование обязательно)
- AI-помощника в админке (только предложения, без автоизменений)

Система отражает реальный процесс работы ТСЖ/УК:
- житель создаёт заявку
- диспетчер обрабатывает
- мастер выполняет
- руководитель смотрит аналитику
- все действия логируются

AI-помощник:
- предлагает категорию и приоритет заявки
- предлагает черновик ответа жильцу
- подсказывает возможные дубликаты
- работает строго в режиме human-in-the-loop

Интерфейс — на русском языке.
Проект должен запускаться локально через Docker Compose.

========================
TECH REQUIREMENTS (EN)
========================

GENERAL
- Generate full repository
- Code-first, runnable MVP
- No questions, make assumptions

STACK
- Backend: FastAPI (Python)
- Frontend: React + Vite + TypeScript
- DB: PostgreSQL
- ORM: SQLAlchemy + Alembic
- Auth: JWT (access/refresh)
- API: REST
- Docs: OpenAPI

ARCHITECTURE
- backend/
  - api/
  - services/
  - repositories/
  - models/
  - core/
- frontend/
- docker-compose.yml

DATABASE
- PostgreSQL schema
- Alembic migrations
- Seed data script
- Indexed ticket fields

CORE MODELS
- User (roles: RESIDENT, DISPATCHER, MASTER, ADMIN, MANAGER)
- Building
- Apartment
- Ticket
- TicketCategory
- TicketPriority
- TicketStatus
- TicketComment
- TicketAttachment
- TicketStatusHistory
- AuditLog
- AI_Suggestion

TICKETS
- Full lifecycle
- SLA / due date
- Status transitions
- Attachments
- Internal/external comments
- Audit logging on every change

AUDIT LOG
- actor_id
- action
- entity_type
- entity_id
- before_json / after_json
- timestamp

AI ASSISTANT
- /ai/suggest endpoint
- Rules-based MVP implementation
- No automatic DB writes
- Suggestions stored separately

SECURITY
- RBAC checks on backend
- Residents can access own tickets only
- Staff access by role
- Hash passwords
- Basic auth rate limiting

FRONTEND PAGES
- Public: Home, Contacts
- Auth: Login, Register
- Resident: Dashboard, Create Ticket, Ticket List, Ticket Details
- Admin: Ticket Inbox, Ticket Details, Users, Dashboard, Audit Log

API ENDPOINTS
- POST /auth/register
- POST /auth/login
- POST /auth/refresh
- GET  /auth/me
- GET  /tickets
- POST /tickets
- GET  /tickets/{id}
- PATCH /tickets/{id}
- POST /tickets/{id}/comments
- POST /tickets/{id}/attachments
- GET  /admin/users
- GET  /admin/audit
- POST /ai/suggest

RBAC
- RESIDENT: own tickets
- DISPATCHER: all building tickets
- MASTER: assigned tickets
- ADMIN: full access
- MANAGER: analytics + audit

DELIVERABLES
- Working backend and frontend
- docker-compose.yml
- .env.example
- README with run instructions
- Seed/demo data

OUTPUT RULES
- Output files grouped by path
- Use clear filenames
- Ensure code compiles
- Do not include explanations

Generate the repository now.


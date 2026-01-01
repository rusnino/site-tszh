# TSZH MVP

MVP веб-проекта для ТСЖ/управляющей компании с личным кабинетом жильца, админкой и системой заявок.

## Запуск через Docker Compose

```bash
cp .env.example .env

docker compose up --build
```

Сервисы будут доступны по адресам:

- Frontend: http://localhost:5173
- Backend (OpenAPI): http://localhost:8000/docs

## Демо-данные

После запуска создаются тестовые данные и пользователи:

- resident@example.com / password
- dispatcher@example.com / password
- master@example.com / password
- admin@example.com / password
- manager@example.com / password

## Полезные команды

```bash
# Пересоздать базу данных
rm -rf db_data

docker compose up --build
```

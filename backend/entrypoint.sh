#!/usr/bin/env sh
set -e

wait_for_db() {
  python - <<'PY'
import os
import time
import psycopg2

host = os.getenv("DB_HOST", "db")
port = int(os.getenv("DB_PORT", "5432"))
dbname = os.getenv("DB_NAME", "tszh")
user = os.getenv("DB_USER", "tszh")
password = os.getenv("DB_PASSWORD", "tszh")

for attempt in range(30):
    try:
        conn = psycopg2.connect(
            host=host, port=port, dbname=dbname, user=user, password=password, connect_timeout=2
        )
        conn.close()
        break
    except psycopg2.OperationalError:
        time.sleep(1)
else:
    raise SystemExit("Database is not ready after waiting.")
PY
}

wait_for_db

alembic upgrade head
python seed.py

exec uvicorn main:app --host 0.0.0.0 --port 8000

"""initial

Revision ID: 0001_initial
Revises: 
Create Date: 2024-01-01 00:00:00.000000
"""

from alembic import op
import sqlalchemy as sa

revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "buildings",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("address", sa.String(length=255), nullable=False),
    )
    op.create_table(
        "apartments",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("building_id", sa.Integer(), sa.ForeignKey("buildings.id"), nullable=False),
        sa.Column("number", sa.String(length=50), nullable=False),
        sa.Column("floor", sa.Integer(), nullable=False),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("full_name", sa.String(length=255), nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.Column("role", sa.Enum("RESIDENT", "DISPATCHER", "MASTER", "ADMIN", "MANAGER", name="userrole"), nullable=False),
        sa.Column("building_id", sa.Integer(), sa.ForeignKey("buildings.id")),
        sa.Column("apartment_id", sa.Integer(), sa.ForeignKey("apartments.id")),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.UniqueConstraint("email"),
    )
    op.create_index("ix_users_email", "users", ["email"], unique=True)
    op.create_index("ix_users_role", "users", ["role"], unique=False)

    op.create_table(
        "ticket_categories",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.String(length=255)),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "ticket_priorities",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("sla_hours", sa.Integer(), nullable=False),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "ticket_statuses",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("key", sa.String(length=50), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.UniqueConstraint("key"),
        sa.UniqueConstraint("name"),
    )

    op.create_table(
        "tickets",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("category_id", sa.Integer(), sa.ForeignKey("ticket_categories.id")),
        sa.Column("priority_id", sa.Integer(), sa.ForeignKey("ticket_priorities.id")),
        sa.Column("status_id", sa.Integer(), sa.ForeignKey("ticket_statuses.id")),
        sa.Column("resident_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("assigned_to_id", sa.Integer(), sa.ForeignKey("users.id")),
        sa.Column("due_date", sa.DateTime()),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
    )
    op.create_index("ix_tickets_category_id", "tickets", ["category_id"], unique=False)
    op.create_index("ix_tickets_priority_id", "tickets", ["priority_id"], unique=False)
    op.create_index("ix_tickets_status_id", "tickets", ["status_id"], unique=False)
    op.create_index("ix_tickets_resident_id", "tickets", ["resident_id"], unique=False)
    op.create_index("ix_tickets_assigned_to_id", "tickets", ["assigned_to_id"], unique=False)
    op.create_index("ix_tickets_due_date", "tickets", ["due_date"], unique=False)

    op.create_table(
        "ticket_comments",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("ticket_id", sa.Integer(), sa.ForeignKey("tickets.id"), nullable=False),
        sa.Column("author_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("is_internal", sa.Boolean(), nullable=False, server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(), nullable=False),
    )
    op.create_table(
        "ticket_attachments",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("ticket_id", sa.Integer(), sa.ForeignKey("tickets.id"), nullable=False),
        sa.Column("file_name", sa.String(length=255), nullable=False),
        sa.Column("file_url", sa.String(length=500), nullable=False),
        sa.Column("uploaded_at", sa.DateTime(), nullable=False),
    )
    op.create_table(
        "ticket_status_history",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("ticket_id", sa.Integer(), sa.ForeignKey("tickets.id"), nullable=False),
        sa.Column("from_status_id", sa.Integer(), sa.ForeignKey("ticket_statuses.id")),
        sa.Column("to_status_id", sa.Integer(), sa.ForeignKey("ticket_statuses.id"), nullable=False),
        sa.Column("changed_by_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("changed_at", sa.DateTime(), nullable=False),
        sa.Column("meta", sa.JSON()),
    )
    op.create_table(
        "audit_logs",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("actor_id", sa.Integer(), sa.ForeignKey("users.id")),
        sa.Column("action", sa.String(length=100), nullable=False),
        sa.Column("entity_type", sa.String(length=100), nullable=False),
        sa.Column("entity_id", sa.Integer()),
        sa.Column("before_json", sa.JSON()),
        sa.Column("after_json", sa.JSON()),
        sa.Column("created_at", sa.DateTime(), nullable=False),
    )
    op.create_table(
        "ai_suggestions",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("ticket_id", sa.Integer(), sa.ForeignKey("tickets.id"), nullable=False),
        sa.Column("suggested_category_id", sa.Integer(), sa.ForeignKey("ticket_categories.id")),
        sa.Column("suggested_priority_id", sa.Integer(), sa.ForeignKey("ticket_priorities.id")),
        sa.Column("suggested_reply", sa.Text()),
        sa.Column("duplicate_ticket_ids", sa.JSON()),
        sa.Column("created_at", sa.DateTime(), nullable=False),
    )


def downgrade():
    op.drop_table("ai_suggestions")
    op.drop_table("audit_logs")
    op.drop_table("ticket_status_history")
    op.drop_table("ticket_attachments")
    op.drop_table("ticket_comments")
    op.drop_index("ix_tickets_due_date", table_name="tickets")
    op.drop_index("ix_tickets_assigned_to_id", table_name="tickets")
    op.drop_index("ix_tickets_resident_id", table_name="tickets")
    op.drop_index("ix_tickets_status_id", table_name="tickets")
    op.drop_index("ix_tickets_priority_id", table_name="tickets")
    op.drop_index("ix_tickets_category_id", table_name="tickets")
    op.drop_table("tickets")
    op.drop_table("ticket_statuses")
    op.drop_table("ticket_priorities")
    op.drop_table("ticket_categories")
    op.drop_index("ix_users_role", table_name="users")
    op.drop_index("ix_users_email", table_name="users")
    op.drop_table("users")
    op.drop_table("apartments")
    op.drop_table("buildings")
    op.execute("DROP TYPE IF EXISTS userrole")

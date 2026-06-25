from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    DateTime
)

DATABASE_URL = "postgresql://postgres:Ma86jtg0@localhost:5432/network_ids"

engine = create_engine(DATABASE_URL)

metadata = MetaData()

alerts = Table(
    "alerts",
    metadata,

    Column("id", Integer, primary_key=True),
    Column("source_ip", String),
    Column("destination_ip", String),
    Column("attack_type", String),
    Column("risk_score", Integer),
    Column("severity", String),
    Column("action", String),
    Column("timestamp", DateTime)
)

blocked_ips = Table(
    "blocked_ips",
    metadata,

    Column("id", Integer, primary_key=True),
    Column("ip_address", String),
    Column("reason", String),
    Column("blocked_at", DateTime)
)

metadata.create_all(engine)

print("Tables Created Successfully")
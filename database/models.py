from sqlalchemy import (
    create_engine,
    MetaData,
    Table
)

DATABASE_URL = "postgresql://postgres:Ma86jtg0@localhost:5432/network_ids"

engine = create_engine(DATABASE_URL)

metadata = MetaData()

alerts = Table(
    "alerts",
    metadata,
    autoload_with=engine
)

blocked_ips = Table(
    "blocked_ips",
    metadata,
    autoload_with=engine
)
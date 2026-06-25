from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:Ma86jtg0@localhost:5432/network_ids"

engine = create_engine(DATABASE_URL)

print("Database Connected Successfully")
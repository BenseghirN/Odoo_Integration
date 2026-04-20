from mygamecollection.infrastructure.database.base import Base
from mygamecollection.infrastructure.database.session import engine

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Database tables created successfully.")
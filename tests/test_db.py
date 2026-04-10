from mygamecollection.infrastructure.database.base import Base
from mygamecollection.infrastructure.database.session import engine
import mygamecollection.infrastructure.database.models  # Import models to ensure they are registered with SQLAlchemy

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Database tables created successfully.")
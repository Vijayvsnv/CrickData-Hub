from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
USERNAME = "postgres"
PASSWORD = "12345"
HOST = "localhost"
PORT = 5432
DB_NAME = "cricket"

urls= f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

engine = create_engine(urls,echo=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

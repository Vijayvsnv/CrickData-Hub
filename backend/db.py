from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os 
from dotenv import load_dotenv
load_dotenv()
USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
urls= f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

engine = create_engine(urls,echo=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

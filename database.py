from sqlalchemy import create_engine, text

import os 
from dotenv import load_dotenv 

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

def load_jobs_from_db():
  with engine.connect() as conn:
    res = conn.execute(text("SELECT * FROM jobs"))
    jobs = []
    for row in res.all():
        jobs.append(row._asdict())
    return jobs
        
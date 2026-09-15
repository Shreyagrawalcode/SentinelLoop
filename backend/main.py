from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = FastAPI()

DATABASE_URL = "sqlite:///./sentinelloop.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.get("/")
def read_root():
    return {"message": "SentinelLoop API running"}

@app.get("/attacks")
def get_attacks():
    return {"attacks": []}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
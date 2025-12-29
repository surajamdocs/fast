from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models, serializer
from database import engine, SessionLocal
from security import hash_password
from auth import login_user


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=serializer.UserResponse)
def create_user(user: serializer.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    db_user = models.User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        phone=user.phone,
        age=user.age,
        password=hash_password(user.password)
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user_data = login_user(db, email, password)


    return user_data

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime
from models import User, OutstandingTokens
from security import verify_password, create_access_token, create_refresh_token


def login_user(db: Session, email: str, password: str) -> str:
    user = db.query(User).filter(User.email == email).first()

    if not user or not verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid email or password"
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User in inactive"
        )
    
    access_token = create_access_token(
        data={
            "id": str(user.id),
            "email": user.email
        })

    refresh_token = create_refresh_token(
        data={"sub": str(user.id)}
    )

    reponse = {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "phone": user.phone,
        "tokens": {
            "access_token": access_token,
            "refresh_token": refresh_token
        }
    }

    OutstandingTokens.create_outstanding_token(db=db, token=refresh_token, user_id=user.id, expires_at = datetime.now())

    return reponse

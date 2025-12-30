from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import Session
from database import Base


class OutstandingTokens(Base):
    __tablename__ = "token_outstanding"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    token = Column(String(1000), nullable=False)
    expires_at = Column(DateTime, nullable=False)

    @classmethod
    def create_outstanding_token(cls, db: Session, token: str, user_id: int, expires_at=expires_at):
        outstanding = cls(token=token, user_id=user_id, expires_at=expires_at)
        db.add(outstanding)
        db.commit()
        db.refresh(outstanding)
        return None


class BlacklistedTokens(Base):
    __tablename__ = "token_blacklisted"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(Integer, ForeignKey("token_outstanding.id"), nullable=False)

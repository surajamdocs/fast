from sqlalchemy import Column, String, Integer, ForeignKey
from database import Base


class OutstandingTokens(Base):
    __tablename__ = "token_outstanding"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String(1000), nullable=False)


class BlacklistedTokens(Base):
    __tablename__ = "token_blacklisted"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(Integer, ForeignKey("token_outstanding.id"), nullable=False)

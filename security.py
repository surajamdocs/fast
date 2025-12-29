from datetime import datetime, timedelta
from jose import jwt
import hashlib
from passlib.context import CryptContext


SECRET_KEY = "CHANGE_THIS_SECRET_KEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def _prehash_password(password: str) -> bytes:
    return hashlib.sha256(password.encode("utf-8")).digest()


def hash_password(password: str) -> str:
    return pwd_context.hash(_prehash_password(password))


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(_prehash_password(password), hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

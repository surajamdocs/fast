import hashlib
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def _prehash_password(password: str) -> bytes:
    """
    Pre-hash password with SHA-256 to avoid bcrypt 72-byte limit.
    """
    return hashlib.sha256(password.encode("utf-8")).digest()


def hash_password(password: str) -> str:
    prehashed = _prehash_password(password)
    return pwd_context.hash(prehashed)


def verify_password(password: str, hashed_password: str) -> bool:
    prehashed = _prehash_password(password)
    return pwd_context.verify(prehashed, hashed_password)

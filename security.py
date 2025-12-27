from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

MAX_PASSWORD_BYTES = 72


def _normalize_password(password: str) -> bytes:
    """
    Normalize password for bcrypt:
    - UTF-8 encode
    - Truncate to 72 bytes
    """
    password_bytes = password.encode("utf-8")
    return password_bytes[:MAX_PASSWORD_BYTES]


def hash_password(password: str) -> str:
    normalized = _normalize_password(password)
    return pwd_context.hash(normalized)


def verify_password(password: str, hashed_password: str) -> bool:
    normalized = _normalize_password(password)
    return pwd_context.verify(normalized, hashed_password)

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str| None = None
    age: int| None = None
    password: str


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone: str| None
    age: int| None
    is_active: bool
    is_admin: bool
    is_staff: bool

    class Config:
        from_attributes = True

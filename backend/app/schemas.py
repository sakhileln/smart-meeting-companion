from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

# User schemas
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# Meeting schemas
class MeetingBase(BaseModel):
    title: str
    description: Optional[str] = None

class MeetingCreate(MeetingBase):
    pass

class Meeting(MeetingBase):
    id: int
    user_id: int
    audio_file_path: Optional[str] = None
    transcript: Optional[str] = None
    summary: Optional[str] = None
    created_at: datetime

    class Config:
        orm_mode = True

# Action Item schemas
class ActionItemBase(BaseModel):
    description: str
    status: str = "pending"
    assigned_to: Optional[str] = None
    due_date: Optional[datetime] = None

class ActionItemCreate(ActionItemBase):
    meeting_id: int

class ActionItem(ActionItemBase):
    id: int
    meeting_id: int
    created_at: datetime

    class Config:
        orm_mode = True

# Response models
class MeetingWithActions(Meeting):
    action_items: List[ActionItem] = []

    class Config:
        orm_mode = True

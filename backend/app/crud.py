from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext
from datetime import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_meetings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Meeting).offset(skip).limit(limit).all()

def get_user_meetings(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Meeting)
        .filter(models.Meeting.user_id == user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )

def create_user_meeting(db: Session, meeting: schemas.MeetingCreate, user_id: int):
    db_meeting = models.Meeting(**meeting.dict(), user_id=user_id)
    db.add(db_meeting)
    db.commit()
    db.refresh(db_meeting)
    return db_meeting

def get_meeting(db: Session, meeting_id: int):
    return db.query(models.Meeting).filter(models.Meeting.id == meeting_id).first()

def update_meeting_transcript(db: Session, meeting_id: int, transcript: str):
    meeting = db.query(models.Meeting).filter(models.Meeting.id == meeting_id).first()
    if meeting:
        meeting.transcript = transcript
        db.commit()
        db.refresh(meeting)
    return meeting

def update_meeting_summary(db: Session, meeting_id: int, summary: str):
    meeting = db.query(models.Meeting).filter(models.Meeting.id == meeting_id).first()
    if meeting:
        meeting.summary = summary
        db.commit()
        db.refresh(meeting)
    return meeting

def create_meeting_action_item(
    db: Session, action_item: schemas.ActionItemCreate, meeting_id: int
):
    db_action_item = models.ActionItem(**action_item.dict(), meeting_id=meeting_id)
    db.add(db_action_item)
    db.commit()
    db.refresh(db_action_item)
    return db_action_item

def get_meeting_action_items(db: Session, meeting_id: int):
    return (
        db.query(models.ActionItem)
        .filter(models.ActionItem.meeting_id == meeting_id)
        .all()
    )

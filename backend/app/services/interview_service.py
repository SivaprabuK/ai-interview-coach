from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.interview import Interview
from app.schemas.interview import InterviewCreate, InterviewUpdate


def create_interview(
    db: Session,
    interview_data: InterviewCreate,
) -> Interview:
    interview = Interview(
        role=interview_data.role,
        difficulty=interview_data.difficulty,
    )

    db.add(interview)
    db.commit()
    db.refresh(interview)

    return interview


def get_interviews(
    db: Session,
    skip: int = 0,
    limit: int = 10,
) -> list[Interview]:
    return (
        db.query(Interview)
        .filter(Interview.is_deleted.is_(False))
        .order_by(Interview.id.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_interview_count(db: Session) -> int:
    return (
        db.query(func.count(Interview.id))
        .filter(Interview.is_deleted.is_(False))
        .scalar()
        or 0
    )


def get_interview_by_id(
    db: Session,
    interview_id: int,
) -> Interview | None:
    return (
        db.query(Interview)
        .filter(
            Interview.id == interview_id,
            Interview.is_deleted.is_(False),
        )
        .first()
    )


def update_interview(
    db: Session,
    interview: Interview,
    interview_data: InterviewUpdate,
) -> Interview:
    update_data = interview_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(interview, field, value)

    db.commit()
    db.refresh(interview)

    return interview


def delete_interview(
    db: Session,
    interview: Interview,
) -> None:
    interview.is_deleted = True
    db.commit()
    db.refresh(interview)

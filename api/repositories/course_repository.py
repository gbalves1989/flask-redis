from ..entities.course_entity import CourseEntity
from ..models.course_model import CourseModel
from api import db
from typing import List


def create(entity: CourseEntity) -> CourseModel:
    course_db: CourseModel = CourseModel(
        name=entity.name,
        description=entity.description
    )

    db.session.add(course_db)
    db.session.commit()
    return course_db


def index() -> List[CourseModel]:
    courses_db: List[CourseModel] = CourseModel.query.all()
    return courses_db

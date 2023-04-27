from flask_openapi3 import Response
from flask import make_response
from ..requests.course_request import CourseBody
from ..schemas.course_schema import CourseSchema
from ..entities.course_entity import CourseEntity
from ..models.course_model import CourseModel
from ..repositories.course_repository import create, index
from typing import List
from ..utils.redis import redis_set, redis_get, redis_remove


def create_course(request: CourseBody) -> Response:
    redis_remove('courses')

    cs: CourseSchema = CourseSchema()

    new_course: CourseEntity = CourseEntity(
        name=request.name,
        description=request.description
    )

    result: CourseModel = create(new_course)
    redis_set('courses', '')
    response = make_response(cs.jsonify(result), 201)
    response.headers['Content-Type'] = 'application/json'
    response.headers['charset'] = 'UTF-8'

    return response


def list_courses() -> Response:
    cs: CourseSchema = CourseSchema(many=True)
    courses: bytes = redis_get('courses')

    if courses == b'':
        result: List[CourseModel] = index()
        redis_set('courses', cs.dumps(result))
        response = make_response(cs.jsonify(result), 200)
        response.headers['Content-Type'] = 'application/json'
        response.headers['charset'] = 'UTF-8'

        return response

    response = make_response(courses, 200)
    response.headers['Content-Type'] = 'application/json'
    response.headers['charset'] = 'UTF-8'

    return response

from api import api
from flask_openapi3 import APIBlueprint, Tag
from api.requests.course_request import CourseBody
from ..services.course_service import create_course, list_courses
from ..responses.course_response import CourseResponse, CourseListResponse


tag: Tag = Tag(name='Courses', description='List of routes')
api_courses: APIBlueprint = APIBlueprint(
    'courses',
    __name__,
    url_prefix='/courses',
    abp_tags=[tag]
)


@api_courses.post(
    '/',
    summary='Create a new course',
    description='Responsible to create and return a new course',
    responses={'201': CourseResponse}
)
async def store(body: CourseBody):
    return create_course(body)


@api_courses.get(
    '/',
    summary='Return a list of courses',
    description='Responsible to return a list of courses',
    responses={'200': CourseListResponse}
)
async def index():
    return list_courses()


api.register_api(api_courses)

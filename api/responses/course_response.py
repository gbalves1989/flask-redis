from pydantic import BaseModel, Field


class CourseResponse(BaseModel):
    id: int = Field(0, description='course id')
    name: str = Field('test', description='name of course')
    description: str = Field('test description', description='description of course')


class CourseListResponse(BaseModel):
    courses: list[CourseResponse]

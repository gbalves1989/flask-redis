from pydantic import BaseModel, Field


class CourseBody(BaseModel):
    name: str = Field(min_length=5, max_length=50, description='course name')
    description: str = Field(min_length=5, max_length=100, description='course description')

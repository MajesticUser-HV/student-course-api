from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class CourseBase(BaseModel):
    title: str
    description: str

class CourseCreate(CourseBase):
    pass

class CourseOut(CourseBase):
    id: int
    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    name: str
    email: EmailStr

class StudentCreate(StudentBase):
    pass

class StudentOut(StudentBase):
    id: int
    courses: List[CourseOut] = []
    class Config:
        orm_mode = True

class Enrollment(BaseModel):
    student_id: int
    course_id: int

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import crud, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/students/", response_model=schemas.StudentOut)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@router.post("/courses/", response_model=schemas.CourseOut)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db, course)

@router.post("/enroll/")
def enroll(enrollment: schemas.Enrollment, db: Session = Depends(get_db)):
    return crud.enroll_student(db, enrollment.student_id, enrollment.course_id)

@router.get("/students/{id}", response_model=schemas.StudentOut)
def get_student(id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.get("/courses/{id}", response_model=schemas.CourseOut)
def get_course(id: int, db: Session = Depends(get_db)):
    course = crud.get_course(db, id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

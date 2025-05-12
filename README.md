# Student Course Management API

A minimal REST API to manage students and their enrolled courses.

## Tech Stack
- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL (or SQLite for testing)

## Setup Instructions

```bash
# Clone repo and install dependencies
git clone https://github.com/MajesticUser-HV/student-course-api.git
cd student-course-api
pip install -r requirements.txt

# Run the server
 uvicorn app:app --reload

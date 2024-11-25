# School Management API

A FastAPI-based REST API for managing school-related data including schools, classes, students, and teachers. This API provides a simple yet robust interface for performing CRUD operations on educational institution data.

## Features

- Complete CRUD operations for all entities
- Data validation using Pydantic models
- Referential integrity checks
- Error handling with appropriate HTTP status codes
- In-memory database storage (for demonstration purposes)

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Pydantic

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd school-management-api
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install fastapi uvicorn pydantic
```

## Running the Application

Run the server using:
```bash
python main.py
```

The API will be available at `http://localhost:4444`

Access the interactive API documentation at `http://localhost:4444/docs`

## API Endpoints

### GET Endpoints

- `GET /schools` - Retrieve all schools
- `GET /classes` - Retrieve all classes
- `GET /students` - Retrieve all students
- `GET /teachers` - Retrieve all teachers

### POST Endpoints

#### Add Student
```bash
POST /students
```
Example request body:
```json
{
    "student_id": 2,
    "student_name": "Jane",
    "student_last_name": "Smith",
    "student_age": 15,
    "class_id": 1
}
```

#### Add Class
```bash
POST /classes
```
Example request body:
```json
{
    "class_id": 2,
    "school_id": 1,
    "class_name": "Class B",
    "supervising_teacher_id": 10
}
```

### DELETE Endpoint

Delete any object by endpoint and ID:
```bash
DELETE /objects/{endpoint}/{obj_id}
```
Example:
```bash
DELETE /objects/students/1
```

### PUT Endpoint

Modify any object field:
```bash
PUT /objects/{endpoint}/{obj_id}
```
Parameters:
- `field_name`: The name of the field to modify
- `new_value`: The new value for the field

Example:
```bash
PUT /objects/students/1?field_name=student_name&new_value=John
```

## Data Models

### Student
```python
{
    "student_id": int,
    "student_name": str,
    "student_last_name": str,
    "student_age": int (5-100),
    "class_id": int
}
```

### Class
```python
{
    "class_id": int,
    "school_id": int,
    "class_name": str,
    "supervising_teacher_id": int
}
```

### School
```python
{
    "school_id": int,
    "school_name": str,
    "school_localization": str
}
```

### Teacher
```python
{
    "teacher_id": int,
    "teacher_name": str,
    "teacher_last_name": str
}
```

## Error Handling

The API implements comprehensive error handling:

- 404 Not Found: When requested resources don't exist
- 400 Bad Request: When input validation fails
- 400 Bad Request: When attempting to delete objects with dependencies

## Data Validation

The API implements several validation checks:

- Age validation for students (must be between 5 and 100)
- Referential integrity (e.g., can't add a student to a non-existent class)
- ID uniqueness validation
- Data type validation for numeric fields

## Limitations

- Currently uses in-memory storage (data is lost when server restarts)
- No authentication/authorization implementation
- No pagination for GET endpoints

## Future Improvements

- Add persistent database storage
- Implement authentication and authorization
- Add pagination for large datasets
- Add search and filtering capabilities
- Implement logging
- Add batch operations support

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your chosen license here]

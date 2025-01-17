# Task Manager API

A RESTful API built with FastAPI and SQLAlchemy. This project demonstrates modern Python web development practices including ORM, REST API design, and unit testing.

## Technical Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Testing**: pytest

## Features

### Implemented Endpoints
- `POST /tasks/` - Create a new task
- `GET /tasks/` - Retrieve all tasks
- `GET /tasks/uncompleted/` - List all incomplete tasks
- `GET /tasks/completed/` - List completed tasks
- `PATCH /tasks/` - Update task
- `DELETE /tasks/{task_id}` - Delete task

### Key Features
- Full CRUD operations for tasks
- Filtering by completion status
- Comprehensive unit testing
- Database session management
- Error handling for missing resources

## Testing
The project includes comprehensive unit tests covering:
- Task creation
- Task retrieval (all, completed, uncompleted)
- Task updates
- Task deletion
- Error handling

## What I'm Learning
This project has helped me understand:
- RESTful API design principles
- Database operations with SQLAlchemy ORM
- Test-driven development practices
- FastAPI framework and modern Python web development
- API documentation with OpenAPI/Swagger

## Future Development Plans
- Add user authentication
- Implement task categories
- Add due dates and priorities
- Create a frontend interface
- Add task sharing capabilities
- Implement API rate limiting

## Project Status
This is an active learning project where I'm implementing features as I learn new concepts in my MSc Computer Science program. The core API functionality and testing are complete, with frontend development and additional features planned.


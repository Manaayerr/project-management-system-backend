# Project Management System - Backend

## Project Description
This is the backend of a Project Management System built with Django and Django REST Framework. 
It provides APIs for user authentication, project and task management, and connects with the React frontend.

## Tech Stack
- Python
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication

## Frontend Repository
[https://github.com/Manaayerr/project-management-system-frontend]

## Deployed Site
[Deployed Site Link Here](#) 
"Will be added later.

## ERD Diagram
<img width="526" height="624" alt="Screenshot 2025-10-25 201801" src="https://github.com/user-attachments/assets/2498d700-15d7-46ae-ab9e-9d84c5b53c85" />

## Routing Table (Frontend Routes)
| Path             | Component/Endpoint        | Notes                         |
|-----------------|-------------------------|-------------------------------|
| /login           | Login                    | User login page               |
| /register        | Register                 | User registration page        |
| /projects        | ProjectsPage             | Dashboard showing projects (Private Route) |
| /projects/:id    | ProjectDetailsPage       | Details of a specific project (Private Route) |


## Installation Instructions
1. Clone this repository
```bash
git clone <backend-repo-link>
Create virtual environment

bash
Copy code
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Install dependencies

bash
Copy code
pip install -r requirements.txt
Run migrations

bash
Copy code
python manage.py migrate
Start the server

bash
Copy code
python manage.py runserver
Optional: Run with Docker if configured

IceBox Features:

Password reset feature

User profile

Kanban board for project management

Dashboard improvements

yaml
Copy code

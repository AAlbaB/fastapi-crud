# BookStack API

BookStack is a FastAPI-based application for managing books, reviews, and tags with full CRUD operations. It features JWT authentication, role-based access control, and asynchronous database operations using SQLModel and PostgreSQL.

## Features

- **Book Management:** Create, read, update, and delete books
- **User Authentication:** JWT-based authentication with access and refresh tokens
- **Role-Based Access Control (RBAC):** Admin and user roles with permission checking
- **Email Verification:** Verify user account using the token sent to their email 
- **Reviews System:** Users can add and manage reviews for books with ratings
- **Tags System:** Organize books with tags and manage tag associations
- **Redis Integration:** Token blocklist management for logout functionality
- **Async Operations:** Built with async/await for high performance
- **Database Migrations:** Alembic for version control of database schema

## Technology Stack

- **Python 3.12**
- **FastAPI** – high-performance async web framework
- **SQLModel / SQLAlchemy (Async)** – ORM and database layer
- **PostgreSQL** – relational database
- **Redis** – token blocklist and session-related operations
- **Celery** - asynchronous task queuing and distributed computing
- **Alembic** – database migrations
- **Docker** – service containerization
- **JWT** – secure authentication mechanism

## Project Structure

```
├── src/
│   ├── auth/                    # Authentication and user management
│   ├── books/                   # Book CRUD and related logic
│   ├── db/                      # Database models and session management
│   ├── reviews/                 # Review CRUD and related logic
│   ├── tags/                    # Tag CRUD and related logic
│   ├── __init__.py              # FastAPI app initialization
│   ├── config.py                # App configuration (env vars)
│   ├── errors.py                # Custom error classes and handlers
├── docs/                        # Documentation and Postman collection
├── migrations/                  # Alembic migration scripts
├── .gitignore                   # Git ignore file
├── .env                         # Environment variables
├── alembic.ini                  # Alembic config for migrations
├── compose.yml                  # Compose file 
├── Dockerfile                   # Docker file 
└── requirements.txt             # Python dependencies
```

## Getting Started with Docker

### 1. Clone the repository

```sh
git clone https://github.com/AAlbaB/fastapi-crud.git
cd fastapi-crud
```

### 2. Configure environment variables

Create a `.env` file in the root directory:

```
DATABASE_URL=postgresql+asyncpg://user:password@db:5432/bookstack_db
JWT_SECRET=your-secret-key
JWT_ALGORITHM=HS256
REDIS_URL=redis://redis:6379
POSTGRES_USER=your-user-db
POSTGRES_PASSWORD=your-pass-db
POSTGRES_DB=bookstack_db
```

The application uses **Async SMTP** for sending verification emails. Configure these environment variables:

```
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_FROM=your-email@gmail.com
MAIL_FROM_NAME=BookStack
DOMAIN=localhost:8000
```

**Important:** For Gmail, use an [App Password](https://myaccount.google.com/apppasswords) instead of your regular password.

### 2. Run containers
```sh
docker-compose up -d
```

### 3. Create tables (Just once)
```sh
docker-compose exec web alembic upgrade head
```

### 4. Stop and remove containers
```sh
docker-compose down    
```

You can see the Flower interface in: [http://127.0.0.1:5555](http://127.0.0.1:5555)

The API will be available at [http://127.0.0.1:8000/api/v1](http://127.0.0.1:8000/api/v1)

## API Documentation

- Interactive docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Postman collection: [`docs/BookStack.postman_collection.json`](docs/BookStack.postman_collection.json)

## Authentication Flow

```
1. User signs up with email/password: 
   ↓
2. Verification email sent with secure token
   ↓
3. User clicks verification link
   ↓
4. Account marked as verified
   ↓
5. User logs in with credentials
   ↓
6. Receives access_token (short-lived) & refresh_token (long-lived)
   ↓
7. Use access_token for API requests
   ↓
8. When access_token expires, use refresh_token to get new one
   ↓
9. On logout, token is added to Redis blocklist
```

## Development Notes

- Alembic is used for all database migrations.
- Use the `RoleChecker` dependency for role-based access.
- The project uses async SQLModel sessions for all DB operations.
- JWT tokens are validated on each request and checked against Redis blocklist for revoked tokens.
- Email verification tokens are URL-safe and expire after a configured duration.
# Notas BookStack

## Creación de tag

1. Pararse en la rama que se desea hacer el tag (usualmente en main, porque se relaciona con el commit): `git tag -a v1.0 -m "Versión inicial"`

2. Para listar todas las etiquetas: `git tag`

3. Subir todas las etiquetas: `git push origin --tags`

4. Dentro de GitHub, se puede crear un release con el tag creado.

## Migración con Alembic

Alembic se usa para crear versiones y realizar cambios en BD cuando se realicen:
- Para ejecutar Alembic: `alembic init -t async migrations` 
    > Se deben realizar cambios en env.py y script

- Crear version de Alembic: `alembic revision --autogenerate -m "init"` 
    > Se debe tener conexión en BD, lo que hace es como comparar lo que se tiene en BD y en lo que se tiene en código para crear que falta, "init" es el mensaje.

- Para aplicar la ultima version de Alembic: `alembic upgrade head`
    > Aplica los cambios de la última revision

- Ayuda de Alembic: `alembic -h`

Notas:
- La mejor forma de crear las tablas en BD es usando Alembic. Usar el init_db no es recomendable en producción. En caso de usarlo, se debe importar los modelos en ese método y  llamarlo con "lifespan" al momento de crear la aplicación con FastAPI.

- Para la autenticación, basta con usar el método "RoleChecker" de dependencies (Utiliza la clase de AccessTokenBearer), si se necesita verificar el rol del autenticado. Pero si no se necesita roles, sino solo que este autenticado, se puede con la clase de "AccessTokenBearer".

## Getting Started Localy

### 1. Clone the repository

```sh
git clone https://github.com/AAlbaB/fastapi-crud.git
cd fastapi-crud
```

### 2. Create and activate a virtual environment

**Linux/macOS:**
```sh
python3 -m venv env
source env/bin/activate
```

**Windows:**
```sh
python -m venv env
env\Scripts\activate
```

### 3. Install dependencies

**Linux/macOS:**
```sh
python3 -m pip install -r requirements.txt
```

**Windows:**
```sh
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/bookstack_db
JWT_SECRET=your-secret-key
JWT_ALGORITHM=HS256
REDIS_URL=redis://localhost:6379
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


### 5. Start PostgreSQL and Redis with docker

**PostgreSQL:**
```sh
docker run -d \
  --name postgres-container \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=admin1234 \
  -e POSTGRES_DB=bookstack_db \
  -p 5432:5432 \
  -v postgres-volume:/var/lib/postgresql \
  postgres:latest
```

**Redis:**
```sh
docker run -d \
  --name redis \
  -p 6379:6379 \
  redis:7
```

### 6. Run database migrations

```sh
alembic upgrade head
```

### 7. Start the FastAPI application

```sh
uvicorn src:app --reload
```

**Start Celery (In other terminal)**
```sh
celery -A src.celery_tasks.c_app worker
```

**Start Flower (In other terminal) - Optional**
```sh
celery -A src.celery_tasks.c_app flower
```

## Comandos docker compose
- Crear y levantar contenedores: `docker-compose up -d`
- Detener y borrar contenedores: `docker-compose down`
- Detener y borrar contenedores con volumenes: `docker-compose down -v`
- Solo detener contenedores: `docker-compose stop`
- Volver a iniciar contenedores: `docker-compose start`
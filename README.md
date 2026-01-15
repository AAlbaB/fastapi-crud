## Ejecutar aplicación local

1. Crear ambiente virtual en carpeta Backend, Windows: `python -m venv env`, Ubuntu: `python3 -m venv env`

2. Activar ambiente virtual, Windows: `env/Scripts/activate`, Ubuntu: `source env/bin/activate`

3. En caso de tener problemas con activar el entorno virtual, se debe abrir el PowerShell como administrador y ejecutar el siguiente comando:  `Set-ExecutionPolicy RemoteSigned -Force`

4. Validar en la consola que se tiene activo el ambiente virtual, para desactivar env: `deactivate`

5. Instalar requirements, Windows: `pip install -r requirements.txt`, Ubuntu: `python3 -m pip install -r requirements.txt`

6. Crear el contenedor de Postgres:

```docker
docker run -d --name postgres-container -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin1234 -e POSTGRES_DB=bookly_db -p 5432:5432 -v postgres-volume:/var/lib/postgresql postgres:latest
```

7. Correr la aplicación con: `uvicorn src:app --reload`, si tiene FastAPI: `fastapi dev src/`


## Notas
Alembic se usa para crear versiones y realizar cambios en BD cuando se realicen:
- Para ejecutar Alembic: `alembic init -t async migrations` 
    > Se deben realizar cambios en env.py y script

- Crear version de Alembic: `alembic revision --autogenerate -m "init"` 
    > Se debe tener conexión en BD, lo que hace es como comparar lo que se tiene en BD y en lo que se tiene en código para crear que falta, "init" es el mensaje.

- Para aplicar la ultima version de Alembic: `alembic upgrade head`
    > Aplica los cambios de la última revision

- Ayuda de Alembic: `alembic -h`

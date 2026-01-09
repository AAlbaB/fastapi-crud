## Ejecutar aplicación en Windows (Local)

1. Crear ambiente virtual en carpeta Backend: `python -m venv .env`
2. Activar ambiente virtual: `.env/Scripts/activate`
3. En caso de tener problemas con activar el entorno virtual, se debe abrir el PowerShell como administrador y ejecutar el siguiente comando:  `Set-ExecutionPolicy RemoteSigned -Force`
4. Validar en la consola que se tiene activo el ambiente virtual, para desactivar env: `deactivate`
5. Instalar requirements: `pip install -r requirements.txt`
6. Crear el contenedor de Postgres: `docker run -d --name postgres-container -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin1234 -e POSTGRES_DB=bookly_db -p 5432:5432 -v postgres-volume:/var/lib/postgresql postgres:latest`
7. Correr la aplicación con: `uvicorn src:app --reload`

## Ejecutar aplicación en Ubuntu (Local)
1. Crear ambiente virtual en carpeta Backend: `python3 -m venv .env`
2. Activar ambiente virtual: `source .env/bin/activate`
3. Validar en la consola que se tiene activo el ambiente virtual, para desactivar env: `deactivate`
4. Instalar requirements: `python3 -m pip install -r requirements.txt`
5. Crear el contenedor de Postgres: `docker run -d --name postgres-container -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin1234 -e POSTGRES_DB=bookly_db -p 5432:5432 -v postgres-volume:/var/lib/postgresql postgres:latest`
6. Correr la aplicación con: `fastapi dev src/`
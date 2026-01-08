## Ejecutar aplicación en Windows (Local)
Para el correcto funcionamiento del programa, se debe crear un ambiente virtual e instalar unos paquetes

1. Crear ambiente virtual en carpeta Backend: `python -m venv env`
2. Activar ambiente virtual: `env/Scripts/activate`
3. En caso de tener problemas con activar el entorno virtual, se debe abrir el PowerShell como administrador y ejecutar el siguiente comando:  `Set-ExecutionPolicy RemoteSigned -Force`
4. Validar en la consola que se tiene activo el ambiente virtual, para desactivar env: `deactivate`
5. Instalar requirements: `pip install -r requirements.txt`
6. Correr la aplicación con: `uvicorn src:app --reload`
## Creación de tag:

1. Pararse en la rama que se desea hacer el tag (usualmente en main, porque se relaciona con el commit): `git tag -a v1.0 -m "Versión inicial"`

2. Para listar todas las etiquetas: `git tag`

3. Subir todas las etiquetas: `git push origin --tags`

4. Dentro de GitHub, se puede crear un release con el tag creado.

Notas:
- La mejor forma de crear las tablas en BD es usando Alembic. Usar el init_db no es recomendable en producción. En caso de usarlo, se debe importar los modelos en ese método y  llamarlo con "lifespan" al momento de crear la aplicación con FastAPI.

- Para la autenticación, basta con usar el método "RoleChecker" de dependencies (Utiliza la clase de AccessTokenBearer), si se necesita verificar el rol del autenticado. Pero si no se necesita roles, sino solo que este autenticado, se puede con la clase de "AccessTokenBearer". 
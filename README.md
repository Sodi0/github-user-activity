# Visor de Actividad de Usuario en GitHub

Este proyecto es un script en Python que permite visualizar los eventos públicos recientes de cualquier usuario de GitHub utilizando la API oficial.

## Características
- Consulta los eventos públicos de un usuario de GitHub.
- Muestra información amigable sobre cada evento (commits, estrellas, forks, issues, etc.).
- Permite elegir cuántos eventos mostrar.
- Manejo de errores comunes (usuario no encontrado, sin actividad, problemas de conexión).

## Uso
1. Ejecuta el script en tu terminal:
    ```bash
    python nombre_del_script.py
    ```
2. Ingresa el nombre de usuario de GitHub cuando se te solicite.
3. Especifica cuántos eventos deseas ver (opcional, por defecto 5).

## Ejemplo de salida

```
Bienvenido al visor de eventos de GitHub
Ingrese el nombre de usuario de GitHub: octocat
Cuantos datos quieres ver? (por defecto 5): 3

📄 Mostrando los últimos 3 eventos de @octocat:

- 💾 Pushed 2 commit(s) to octocat/Hello-World
- ⭐ Starred octocat/Spoon-Knife
- 🍴 Forked octocat/linguist
```

## Requisitos

- Python 3.x

## Notas

- Utiliza la API pública de GitHub, por lo que está sujeta a límites de uso.
- No requiere autenticación para eventos públicos.

## Licencia
Este proyecto se distribuye bajo la licencia MIT.
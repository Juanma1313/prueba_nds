# **Descripción del Proyecto**
Desarrollar una aplicación web para un sistema de gestión de tareas. Los usuarios podrán
registrarse, iniciar sesión, crear, editar, eliminar y listar tareas. La aplicación deberá contar con
un frontend en React, un backend en Django, y utilizar PostgreSQL como base de datos.
Requisitos del sistema:

## 1. Backend (Django/Python):

- Crear una API RESTful con Django Rest Framework (DRF) para gestionar las tareas. 
    La API debe permitir:

    - [x] Registro de usuarios (sign up).
    - [x] Autenticación de usuarios (login/logout) con JWT.
    - [x] Gestión de tareas (CRUD):
        - [x] Crear tarea.
        - [x] Leer tarea(s).
        - [x] Actualizar tarea.
        - [x] Eliminar tarea.
    - [x] La API debe validar la entrada y devolver errores de forma adecuada.
    - [ ] Usar PostgreSQL para almacenar los datos de los usuarios y las tareas.

## 2. Frontend (React):

- Crear una aplicación en React que consuma la API del backend. 
    Debe incluir:

    - [ ] Página de registro y login.
    - [ ] Una página principal donde los usuarios puedan ver sus tareas (listartareas).
    - [ ] Formularios para crear y editar tareas.
    - [ ] Implementar un sistema de autenticación usando JWT para mantener la sesión activa.▪
    - [ ] Buen uso de los componentes funcionales, hooks, y manejo de estados.

## 3. Base de datos (PostgreSQL):

- [ ] Usar PostgreSQL como base de datos para almacenar la información de usuarios y tareas. 
- [x] La base de datos debe ser definida mediante migraciones en Django.
- [x] El esquema de la base de datos debe contener al menos dos tablas: usuarios y tareas.

## 4. Docker:

- [ ] Dockerizar tanto el frontend como el backend.
- [ ] Crear un archivo docker-compose.yml para orquestar la ejecución de los servicios (backend, frontend y base de datos).
- [ ] Asegurarse de que todo funcione correctamente al ejecutar docker-compose up.

## 5. GitHub:
- [x] Subir el código a un repositorio de GitHub.
- [x] Asegúrate de que el repositorio tenga un README.md detallado que incluya:
    - [ ] Instrucciones para ejecutar la aplicación localmente (backend y frontend).
    - [ ] Instrucciones para desplegar en un servidor (si el candidato tiene uno disponible para este paso).
    - [ ] Descripción de la arquitectura de la aplicación.
- [x] Usar una estrategia adecuada para commits y ramas (trabajar en una rama para la implementación, y hacer PRs para integrar el código).

---
---
# **Pruebas**
Aunque he realizado pruebas sobre todas las interfaces, usando usando la herramienta Postman de VSC. Estas no han sido exaustivas.

Para popular más facilmente la base de datos, he creado las interfaces de administración de datos usando la API de administracion de Django. 

Adjunto algunos de los ejemplos de las pruebas que he realizado usando curl.

## Pruebas de alta de usuarios
### Solicitar la creación de un usuario válido.
```
curl --location 'http://127.0.0.1:8000/register_user/'
--form 'email="test@gmail.com"'
--form 'username="juanma"'
--form 'first_name="Juan Manuel"'
--form 'last_name="de las Heras Arroyo"'
--form 'password="Enunlugardelamancha"'
```
#### Respuesta
```
{
    "id": 3,
    "email": "test@gmail.com",
    "username": "juanma",
    "first_name": "Juan Manuel",
    "last_name": "de las Heras Arroyo"
}
```

## Probar la interfaz JWT 

### Soplicitar sesion con un usuario válido

```
curl --location 'http://127.0.0.1:8000/api/token/' --form 'username="juanma"' --form 'password="enunlugardelamancha"'
```
#### Respuesta
```
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
        eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczODgxMTg4MiwiaWF0IjoxNzM4NzI1NDgyLCJqdGkiOiJmMmQzYzY3YTU5MTI0ZDFhOTk2YTBlNGQ4ZjE1OTE1NyIsInVzZXJfaWQiOjJ9.
        iKfQ-8ehj2hL4MTStdr2Y2fqzkkemiKXzJDg4u-0mxs",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
        eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM4NzI5MDgyLCJpYXQiOjE3Mzg3MjU0ODIsImp0aSI6IjE3ZGViOTYxNDkwYTQxMzY5NmVkNzJlY2JlYjhlMjYwIiwidXNlcl9pZCI6Mn0.
        muisS9ehx6cUBVnUUdm3oTLN-KFcF9dWiF3gb1uLh4g"
}
```

### Soplicitar sesion con un usuario válido

```
curl --location 'http://127.0.0.1:8000/api/token/' --form 'username="baduser"' --form 'password="enunlugardelamancha"'
```
#### Respuesta
```
{
    "detail": "No active account found with the given credentials"
}
```

### Solicitar la creación de una tarea válida
```
curl --location 'http://127.0.0.1:8000/task_create/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM4NzM0NDAyLCJpYXQiOjE3Mzg3MzA4MDIsImp0aSI6ImMxNzBjMmMyZDZhMDRkYmRiZjA3ZTBhMDllNGEzZjg3IiwidXNlcl9pZCI6Mn0.KpqCKx-_l4oRhPUKL2QI_3BOdrf68wtRMLL2I2zLGY4' \
--form 'title="Task 9"' \
--form 'details="Task number 9"' \
--form 'starts_on="2025-02-15T14:30"' \
--form 'ends_on="2025-02-16T00:00"' \
--form 'priority="4"'
```
#### Respuesta
```
{
    "id": 12,
    "title": "Task 9",
    "author": {
        "id": 2,
        "username": "juanma",
        "first_name": "Juan Manuel",
        "last_name": "de las Heras Arroyo"
    },
    "details": "Task number 9",
    "priority": 4,
    "starts_on": "2025-02-15T14:30:00Z",
    "ends_on": "2025-02-16T00:00:00Z",
    "created_on": "2025-02-05T04:58:16.404674Z",
    "updated_on": "2025-02-05T04:58:16.404649Z",
    "status": 0
}
```
### Solicitar la creación de una tarea No válida
```
curl --location --request PUT 'http://127.0.0.1:8000/task_update/9/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM4NzM0MDcyLCJpYXQiOjE3Mzg3MzA0NzIsImp0aSI6IjQ0ZGI2OGViMGZmNjQ5YjRhOTJiYTIxY2YxMTA1YmMxIiwidXNlcl9pZCI6M30.luKDCHZGiynOr8WdKgfcqpDwULC-_B2eYp602SHRQiw' \
--form 'title="Task 6"' \
--form 'details="Task number 6 updated"'
```
#### Respuesta 
```
{
    "error": "You are not the author of this task"
}
```
### Solicitar la actualización de una tarea existente
```
curl --location --request PUT 'http://127.0.0.1:8000/task_update/9/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM4NzM0NDAyLCJpYXQiOjE3Mzg3MzA4MDIsImp0aSI6ImMxNzBjMmMyZDZhMDRkYmRiZjA3ZTBhMDllNGEzZjg3IiwidXNlcl9pZCI6Mn0.KpqCKx-_l4oRhPUKL2QI_3BOdrf68wtRMLL2I2zLGY4' \
--form 'title="Task 6"' \
--form 'details="Task number 6 updated"' \
--form 'starts_on="2025-02-15T14:30"' \
--form 'ends_on="2025-02-16T00:00"'
```
#### Respuesta
```
{
    "id": 9,
    "title": "Task 6",
    "author": {
        "id": 2,
        "username": "juanma",
        "first_name": "Juan Manuel",
        "last_name": "de las Heras Arroyo"
    },
    "details": "Task number 6 updated",
    "priority": 2,
    "starts_on": "2025-02-15T14:30:00Z",
    "ends_on": "2025-02-16T00:00:00Z",
    "created_on": "2025-02-05T03:54:53.482177Z",
    "updated_on": "2025-02-05T04:48:45.946519Z",
    "status": 0
}
```
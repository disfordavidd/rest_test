# CRUD DJANGO RESTFRAMEWORK Lampara

Este proyecto contiene un CRUD para gestionar lamparas, las cuales se pueden registrar con un nombre, precio, cantidad y fecha.

## Configuración inicial

1. Instalar entorno virtual 

    `python -m venv venv`

2. Activar el entorno virtual 

    `.\venv\Scripts\activate`

3. Instalar lor paquetes requeridos 

    `pip install -r requirements.txt`

Si se desea utilizar la base de datos por defecto de Django (db.sqlite3), ejecute los pasos 4 y 5, si requiere utilizar otra ubicación de base de datos deberá configurar la constante DATABASES del proyecto en 'test_site\settings.py'

4. Crear las migraciones

    `python .\manage.py makemigrations`

5. Aplicar las migraciónes

    `python .\manage.py migrate`

Finalmente levante el proyecto:

6. Ejecutar un servidor local

    `python .\manage.py runserver (Opcional)puerto`

# REST API

A continuación se describe la API REST.

## Obtener listado de todas las lamparas registradas

### Request

`GET /lampara/`

**Example** `http://localhost:8000/lampara/`

### Response

    HTTP 200 OK
    Allow: GET, POST, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept

    {
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 12,
                "nombre": "Lampara de lava",
                "precio": 568.0,
                "cantidad": 264,
                "fecha": "2024-05-18T20:55:00Z"
            },
            {
                "id": 16,
                "nombre": "Lampara de calle",
                "precio": 12600.0,
                "cantidad": 10,
                "fecha": "2024-05-21T21:00:00Z"
            }
        ]
    }

## Obtener una lampara en específico

### Request

`GET /lampara/<id>/`

**Example** `http://localhost:8000/lampara/12/`

### Response

    HTTP 200 OK
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept

    {
        "id": 12,
        "nombre": "Lampara de lava",
        "precio": 568.0,
        "cantidad": 264,
        "fecha": "2024-05-18T20:55:00Z"
    }

## Agregar una nueva lámpara

### Request

`POST /lampara/`

**Example** `http://localhost:8000/lampara/` with `form-data = {"nombre": "Lampara de noche", "precio": "340.50", "cantidad": "20", "fecha": "2024-05-22 19:16:00"}`

### Response

    HTTP 201 Created
    Allow: GET, POST, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept

    {
        "id": 17,
        "nombre": "Lampara de noche",
        "precio": 340.5,
        "cantidad": 20,
        "fecha": "2024-05-22T19:16:00Z"
    }

## Actualizar información de lampara

### Request

`PUT /lampara/<id>/`

**Example** `http://localhost:8000/lampara/17/` with `form-data = {"nombre": "Lampara de noche color negro", "precio": "350.80", "cantidad": "20", "fecha": "2024-05-22 19:16:00"}`

### Response

    HTTP 200 OK
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept

    {
        "id": 17,
        "nombre": "Lampara de noche color negro",
        "precio": 350.8,
        "cantidad": 20,
        "fecha": "2024-05-22T19:16:00Z"
    }

## Eliminar lampara

### Request

`DELETE /lampara/<id>/`

**Example** `http://localhost:8000/lampara/17/`

### Response

    HTTP 204 No Content
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept
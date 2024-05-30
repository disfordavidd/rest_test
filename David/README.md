# CRUD DJANGO RESTFRAMEWORK CON MODELO SILLA

Este proyecto contiene un CRUD para gestionar SILLAS, las cuales se pueden registrar con precio, fecha, tipo y cantidad.

## Configuración inicial

1. Instalar entorno virtual 

    `python -m venv venv`

2. Activar el entorno virtual 

    `env/Scripts/activate`

3. Instalar lor paquetes requeridos 

    `pip install -r requirements.txt`

Si se desea utilizar la base de datos por defecto de Django (db.sqlite3), ejecute los pasos 4 y 5, si requiere utilizar otra ubicación de base de datos deberá configurar la constante DATABASES del proyecto en 'test_site\settings.py'

4. Crear las migraciones

    `python manage.py makemigrations`

5. Aplicar las migraciónes

    `python manage.py migrate`

Finalmente levante el proyecto:

6. Ejecutar un servidor local

    `python manage.py runserver (Opcional)puerto`

# REST API

A continuación se describe la API REST.

## Obtener listado de todas las lsillas registradas

### Request

`GET /sillas/`

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
                "id": 2,
                "fecha": "2024-05-24T03:26:20Z",
                "tipo": "Madera"
            },
            {
                "id": 3,
                "fecha": "2024-05-23T21:28:00Z",
                "tipo": "Metal"
            }
        ]
    }

## Obtener una silla en específico

### Request

`GET /sillas/<id>/`

**Example** `http://localhost:8000/sillas/2/`

### Response

    HTTP 200 OK
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept

    {
        "id": 2,
        "fecha": "2024-05-24T03:26:20Z",
        "tipo": "Madera"
    }

## Agregar una nueva silla

### Request

`POST /sillas/`

**Example** `http://localhost:8000/sillas/` with `form-data = {"fecha": "2024-05-29T22:24:00Z", "tipo": "Plástico" }`

### Response

    HTTP 201 Created
    Allow: GET, POST, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept

    {
        "id": 4,
        "fecha": "2024-05-29T22:24:00Z",
        "tipo": "Plástico"
    }

## Actualizar información de sillas

### Request

`PUT /sillas/<id>/`

**Example** `http://localhost:8000/sillas/4/` with `form-data = {"fecha": "2024-05-29T22:24:00Z", "tipo": "Plástico reciclado"}`

### Response

    HTTP 200 OK
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept

    {
        "id": 4,
        "fecha": "2024-05-29T22:24:00Z",
        "tipo": "Plástico reciclado"
    }

## Eliminar sillas

### Request

`DELETE /sillas/<id>/`

**Example** `http://localhost:8000/sillas/4/`

### Response

    HTTP 204 No Content
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept

# API Restful Deportiva

Esta es una API Restful desarrollada para la gestión de usuarios, ejercicios y rutinas deportivas. Está construida utilizando **FastAPI** y conectada a una base de datos relacional con **PostgreSQL**. Además, cuenta con pruebas automatizadas mediante **Pytest** para garantizar la calidad y funcionalidad del proyecto.

## 🚀 Características principales

- Gestión de usuarios: Crear, leer, actualizar y eliminar usuarios.
- Gestión de ejercicios: Crear, leer, actualizar y eliminar ejercicios.
- Gestión de rutinas: Crear, leer, actualizar y eliminar rutinas asociadas a usuarios y ejercicios.
- Documentación interactiva generada automáticamente con Swagger y ReDoc.

## 🛠️ Herramientas y tecnologías utilizadas

- **Lenguajes**: Python (v3.11.3)
- **Framework principal**: [FastAPI](https://fastapi.tiangolo.com/)
- **Base de datos**: PostgreSQL
- **ORM**: SQLAlchemy
- **Pruebas**: Pytest, Pytest-asyncio
- **Dependencias adicionales**:
  - [Faker](https://faker.readthedocs.io/): Para generar datos aleatorios en pruebas.
  - [Pydantic](https://pydantic-docs.helpmanual.io/): Validación de datos y esquemas.
  - [Uvicorn](https://www.uvicorn.org/): Servidor ASGI.


## 📋 Requisitos previos

1. **Python**: Asegúrate de tener Python 3.11.3 instalado en tu máquina.
2. **PostgreSQL**: Instala PostgreSQL y crea una base de datos para el proyecto.

## ⚙️ Instalación y configuración

1. **Clona este repositorio**:

git clone <URL_DEL_REPOSITORIO>
cd api-restful-project

2. **Crea y activa un entorno virtual**:

python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

3. **Instala las dependencias**:

pip install -r requirements.txt

4. **Configura la base de datos**:

Asegúrate de que PostgreSQL esté en ejecución.
Crea un archivo .env en la raíz del proyecto con la siguiente configuración:

DATABASE_URL=postgresql+psycopg2://usuario:contraseña@localhost/nombre_base_datos

4. **Aplica las migraciones (si es necesario)**:

Aplica las migraciones (si es necesario):


## ▶️ Ejecución del proyecto

1. **Inicia el servidor**:

uvicorn app.main:app --reload

2. **Accede a la documentación interactiva**:

Swagger UI: http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc

## 🧪 Ejecutar pruebas

Ejecuta las pruebas con Pytest para verificar la funcionalidad de la API:

pytest



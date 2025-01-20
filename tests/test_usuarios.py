from faker import Faker
import pytest

faker = Faker()

@pytest.mark.asyncio
async def test_crear_usuario(client):
    # Generar datos aleatorios
    nombre = faker.name()
    correo = faker.email()
    contrasena = faker.password()
    
    # Hacer la petición POST para crear un usuario
    response = await client.post(
        "/usuarios/",
        json={
            "nombre": nombre,
            "correo": correo,
            "contrasena": contrasena
        }
    )
    
    # Verificar respuesta
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == nombre
    assert data["correo"] == correo

@pytest.mark.asyncio
async def test_leer_usuarios(client):
    # Hacer la petición GET para obtener usuarios
    response = await client.get("/usuarios/")
    
    # Verificar respuesta
    assert response.status_code == 200
    assert isinstance(response.json(), list)

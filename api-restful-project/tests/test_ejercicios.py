from faker import Faker
import pytest

faker = Faker()

@pytest.mark.asyncio
async def test_crear_ejercicio(client):
    # Generar datos aleatorios
    nombre = faker.word()
    descripcion = faker.text(max_nb_chars=50)
    categoria = faker.word()
    nivel_dificultad = faker.word()

    # Hacer la petición POST para crear un ejercicio
    response = await client.post(
        "/ejercicios/",
        json={
            "nombre": nombre,
            "descripcion": descripcion,
            "categoria": categoria,
            "nivel_dificultad": nivel_dificultad
        }
    )
    
    # Verificar respuesta
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == nombre
    assert data["descripcion"] == descripcion

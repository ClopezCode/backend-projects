from faker import Faker
import pytest

faker = Faker()

@pytest.mark.asyncio
async def test_crear_rutina(client):
    # Obtener un usuario existente
    usuarios_response = await client.get("/usuarios/")
    usuarios = usuarios_response.json()
    if usuarios:
        usuario_id = usuarios[0]["id"]
    else:
        # Crear un nuevo usuario si no existe
        usuario_response = await client.post(
            "/usuarios/",
            json={
                "nombre": faker.name(),
                "correo": faker.email(),
                "contrasena": faker.password(),
            },
        )
        assert usuario_response.status_code == 200
        usuario_data = usuario_response.json()
        usuario_id = usuario_data["id"]

    # Obtener un ejercicio existente
    ejercicios_response = await client.get("/ejercicios/")
    ejercicios = ejercicios_response.json()
    if ejercicios:
        ejercicio_id = ejercicios[0]["id"]
    else:
        # Crear un nuevo ejercicio si no existe
        ejercicio_response = await client.post(
            "/ejercicios/",
            json={
                "nombre": faker.word(),
                "descripcion": faker.text(max_nb_chars=50),
                "categoria": faker.word(),
                "nivel_dificultad": faker.word(),
            },
        )
        assert ejercicio_response.status_code == 200
        ejercicio_data = ejercicio_response.json()
        ejercicio_id = ejercicio_data["id"]

    # Crear una rutina usando los IDs existentes
    rutina_response = await client.post(
        "/rutinas/",
        json={
            "usuario_id": usuario_id,
            "ejercicio_id": ejercicio_id,
            "duracion": 60,
            "fecha": faker.date_time_this_year().isoformat(),  # Fecha generada automáticamente
        },
    )
    assert rutina_response.status_code == 200
    rutina_data = rutina_response.json()

    # Verificar que los datos de la rutina se crearon correctamente
    assert rutina_data["usuario_id"] == usuario_id
    assert rutina_data["ejercicio_id"] == ejercicio_id
    assert rutina_data["duracion"] == 60

@pytest.mark.asyncio
async def test_leer_rutinas(client):
    # Hacer la petición GET para obtener rutinas
    response = await client.get("/rutinas/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

import pytest
from httpx import AsyncClient
from asgi_lifespan import LifespanManager
from app.main import app


@pytest.fixture
async def client():
    async with LifespanManager(app):
        async with AsyncClient(base_url="http://127.0.0.1:8000") as client:
            yield client




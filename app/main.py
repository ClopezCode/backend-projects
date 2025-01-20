from fastapi import FastAPI
from .database import engine
from .models import Base
from .routers import usuarios, ejercicios, rutinas

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Restful Deportiva",
    description="API para la gestión de usuarios, ejercicios y rutinas deportivas.",
    version="1.0.0"
)

# Incluir routers
app.include_router(usuarios.router)
app.include_router(ejercicios.router)
app.include_router(rutinas.router)

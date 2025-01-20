from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/ejercicios",
    tags=["Gestión de Ejercicios"]
)

@router.get("/", response_model=list[schemas.Ejercicio], description="Obtiene una lista de todos los ejercicios disponibles en el sistema.")
def obtener_ejercicios(db: Session = Depends(get_db)):
    return db.query(models.Ejercicio).all()

@router.post("/", response_model=schemas.Ejercicio, description="Crea un nuevo ejercicio. Es necesario proporcionar un nombre, descripción, categoría y nivel de dificultad.")
def crear_ejercicio(ejercicio: schemas.EjercicioCreate, db: Session = Depends(get_db)):
    nuevo_ejercicio = models.Ejercicio(**ejercicio.dict())
    db.add(nuevo_ejercicio)
    db.commit()
    db.refresh(nuevo_ejercicio)
    return nuevo_ejercicio

@router.put("/{ejercicio_id}", response_model=schemas.Ejercicio, description="Actualiza los datos de un ejercicio existente. Requiere el ID del ejercicio y los datos a modificar.")
def actualizar_ejercicio(ejercicio_id: int, ejercicio: schemas.EjercicioCreate, db: Session = Depends(get_db)):
    ejercicio_db = db.query(models.Ejercicio).filter(models.Ejercicio.id == ejercicio_id).first()
    if not ejercicio_db:
        raise HTTPException(status_code=404, detail="Ejercicio no encontrado")
    for key, value in ejercicio.dict().items():
        setattr(ejercicio_db, key, value)
    db.commit()
    db.refresh(ejercicio_db)
    return ejercicio_db

@router.delete("/{ejercicio_id}", description="Elimina un ejercicio del sistema utilizando su ID.")
def eliminar_ejercicio(ejercicio_id: int, db: Session = Depends(get_db)):
    ejercicio_db = db.query(models.Ejercicio).filter(models.Ejercicio.id == ejercicio_id).first()
    if not ejercicio_db:
        raise HTTPException(status_code=404, detail="Ejercicio no encontrado")
    db.delete(ejercicio_db)
    db.commit()
    return {"detail": "Ejercicio eliminado"}

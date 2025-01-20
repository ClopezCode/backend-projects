from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/rutinas",
    tags=["Gestión de Rutinas"]
)

@router.get("/", response_model=list[schemas.Rutina], description="Obtiene una lista de todas las rutinas creadas en el sistema.")
def obtener_rutinas(db: Session = Depends(get_db)):
    return db.query(models.Rutina).all()

@router.post("/", response_model=schemas.Rutina, description="Crea una nueva rutina asociada a un usuario y a un ejercicio. Es necesario indicar el ID del usuario, el ID del ejercicio, la duración y, opcionalmente, la fecha.")
def crear_rutina(rutina: schemas.RutinaCreate, db: Session = Depends(get_db)):
    nueva_rutina = models.Rutina(**rutina.dict())
    db.add(nueva_rutina)
    db.commit()
    db.refresh(nueva_rutina)
    return nueva_rutina

@router.put("/{rutina_id}", response_model=schemas.Rutina, description="Actualiza los datos de una rutina existente. Requiere el ID de la rutina y los datos a modificar.")
def actualizar_rutina(rutina_id: int, rutina: schemas.RutinaCreate, db: Session = Depends(get_db)):
    rutina_db = db.query(models.Rutina).filter(models.Rutina.id == rutina_id).first()
    if not rutina_db:
        raise HTTPException(status_code=404, detail="Rutina no encontrada")
    for key, value in rutina.dict().items():
        setattr(rutina_db, key, value)
    db.commit()
    db.refresh(rutina_db)
    return rutina_db

@router.delete("/{rutina_id}", description="Elimina una rutina del sistema utilizando su ID.")
def eliminar_rutina(rutina_id: int, db: Session = Depends(get_db)):
    rutina_db = db.query(models.Rutina).filter(models.Rutina.id == rutina_id).first()
    if not rutina_db:
        raise HTTPException(status_code=404, detail="Rutina no encontrada")
    db.delete(rutina_db)
    db.commit()
    return {"detail": "Rutina eliminada"}

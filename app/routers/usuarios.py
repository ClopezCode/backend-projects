from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/usuarios",
    tags=["Gestión de Usuarios"]
)

@router.get("/", response_model=list[schemas.Usuario], description="Obtiene la lista de todos los usuarios registrados.")
def leer_usuarios(db: Session = Depends(get_db)):
    return db.query(models.Usuario).all()

@router.post("/", response_model=schemas.Usuario, description="Registra un nuevo usuario en el sistema. Se deben proporcionar el nombre, correo y contraseña.")
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    nuevo_usuario = models.Usuario(**usuario.dict())
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@router.put("/{usuario_id}", response_model=schemas.Usuario, description="Actualiza la información de un usuario existente. Requiere el ID del usuario y los datos a modificar (nombre, correo o contraseña).")
def actualizar_usuario(usuario_id: int, usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    usuario_db = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if not usuario_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    for key, value in usuario.dict().items():
        setattr(usuario_db, key, value)
    db.commit()
    db.refresh(usuario_db)
    return usuario_db

@router.delete("/{usuario_id}", description="Elimina un usuario del sistema por su ID.")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario_db = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if not usuario_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(usuario_db)
    db.commit()
    return {"detail": "Usuario eliminado"}

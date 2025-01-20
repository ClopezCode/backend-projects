from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Esquema para Usuario
class UsuarioBase(BaseModel):
    nombre: str
    correo: str

class UsuarioCreate(UsuarioBase):
    pass
    contrasena: str

class Usuario(UsuarioBase):
    id: int
    fecha_registro: Optional[datetime]

    class Config:
        orm_mode = True

# Esquema para Ejercicio
class EjercicioBase(BaseModel):
    nombre: str
    descripcion: str
    categoria: str
    nivel_dificultad: str

class EjercicioCreate(EjercicioBase):
    pass

class Ejercicio(EjercicioBase):
    id: int
    fecha_creacion: Optional[datetime]

    class Config:
        orm_mode = True

# Esquema para Rutina
class RutinaBase(BaseModel):
    usuario_id: int
    ejercicio_id: int
    duracion: int
    fecha: Optional[datetime]

class RutinaCreate(RutinaBase):
    pass

class Rutina(RutinaBase):
    id: int
    class Config:
        orm_mode = True
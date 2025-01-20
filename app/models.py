from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    fecha_registro = Column(TIMESTAMP, server_default="NOW()")
    contrasena = Column(String(255), nullable=False)

    rutinas = relationship("Rutina", back_populates="usuario")


class Ejercicio(Base):
    __tablename__ = "ejercicios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String, nullable=True)
    categoria = Column(String(50), nullable=False)
    nivel_dificultad = Column(String(50), nullable=False)
    fecha_creacion = Column(TIMESTAMP, server_default="NOW()")


class Rutina(Base):
    __tablename__ = "rutinas"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    ejercicio_id = Column(Integer, ForeignKey("ejercicios.id"), nullable=False)
    duracion = Column(Integer, nullable=False)  # En minutos
    fecha = Column(TIMESTAMP, server_default="NOW()")

    usuario = relationship("Usuario", back_populates="rutinas")
    ejercicio = relationship("Ejercicio")

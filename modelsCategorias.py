from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from database import Base


class Categoria(Base):
    __tablename__ = 'categorias'
    
    idCategoria = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), index=True, unique=True)
    
    tareas = relationship("Tarea", back_populates="categoria")


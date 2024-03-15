from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base
from modelsCategorias import Categoria
from sqlalchemy.orm import relationship
from dateutil.parser import parse


class Tarea(Base):
    __tablename__ = 'tareas'
    fecha = default=func.now()
    idTarea = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), index=True)
    descripcion = Column(String(255), index=True)
    fecha_creacion = Column(String(255), default=str(func.now()))
    categoria_id = Column(Integer, ForeignKey(default=func.now()))

    categoria = relationship("Categoria", back_populates="tareas")

    @property
    def fecha_creacion_as_datetime(self):
        return parse(self.fecha_creacion)




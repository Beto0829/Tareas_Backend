from ast import List
import datetime
from sqlalchemy import func
from sqlalchemy.orm import Session

from modelsCategorias import Categoria
from modelsTareas import Tarea
from schemasTareas import TareaDate
from schemasCategorias import CategoriaDate

def formatear_fecha(fecha: datetime) -> str:
    return fecha.strftime("%Y-%m-%d %H:%M:%S")

def get_tareas(db: Session):
    return db.query(Tarea).all()

#def get_tareas(db: Session) -> List[TareaDate]:
  #  tareas = db.query(Tarea).all()
   # return [TareaDate(
    ##   descripcion=tarea.descripcion,
      #  categoria_id=tarea.categoria_id,
       # fecha_creacion=tarea.fecha_creacion.strftime("%Y-%m-%d %H:%M:%S")
    #) for tarea in tareas]

def get_categorias(db: Session):
    return db.query(Categoria).all()

def get_tarea_by_id(db: Session, id: int):
    return db.query(Tarea).filter(Tarea.idTareas == id).first()

def get_categoria_by_id(db: Session, id: int):
    return db.query(Categoria).filter_by(idCategoria=id).first()

#nose usa aun
def get_tarea_por_id_categoria(db: Session, categoria_id: int):
    return db.query(Tarea).filter(Tarea.categoria_id == categoria_id).all()

def get_categoria_por_nombre(db: Session, nombre: str):
    return db.query(Categoria).filter(Categoria.nombre == nombre).first()

def get_tarea_por_titulo(db: Session, titulo: str):
    return db.query(Tarea).filter(Tarea.titulo == titulo).first()

def create_tarea(db: Session, tarea: TareaDate):
    new_tarea = Tarea(
        titulo=tarea.titulo,
        descripcion=tarea.descripcion,
        categoria_id=tarea.categoria_id,
    )
    db.add(new_tarea)
    db.commit()
    return new_tarea


def create_categoria(db: Session, categoria: CategoriaDate):
    new_categoria = Categoria(nombre = categoria.nombre)
    db.add(new_categoria)
    db.commit()
    db.flush(new_categoria)
    return new_categoria
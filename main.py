from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import crud

from database import engine, localSession
from schemasCategorias import CategoriaDate, CategoriaId
from schemasTareas import TareaDate, TareaId
from modelsCategorias import Base as CategoriasBase
from modelsTareas import Base as TareasBase

CategoriasBase.metadata.create_all(bind=engine)
TareasBase.metadata.create_all(bind=engine) 

app = FastAPI()

origin = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()
        

@app.get("/")
def root():
    return "Hola Papi"

@app.post('/api/categorias/', response_model= CategoriaId)
def create_categoria(categoria: CategoriaDate, db: Session = Depends(get_db)):
    check_nombre = crud.get_categoria_por_nombre(db=db, nombre = categoria.nombre)
    if check_nombre:
        raise HTTPException(status_code= 404, detail='Esta categoria ya existe!!')
    return crud.create_categoria(db=db, categoria=categoria)

@app.post('/api/tareas/', response_model=TareaId)
def create_tarea(tarea: TareaDate, db: Session = Depends(get_db)):
    categoria = crud.get_categoria_by_id(db=db, id=tarea.categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail='No existe la categoría a la que le estás asignando la tarea!!')
    return crud.create_tarea(db=db, tarea=tarea)


@app.get("/api/categorias/", response_model= list[CategoriaId])
def get_categorias(db: Session = Depends(get_db)):
    return crud.get_categorias(db=db)

@app.get("/api/tareas/", response_model= list[TareaId])
def get_tareas(db: Session = Depends(get_db)):
    return crud.get_tareas(db=db)

@app.get('/api/tareas{titulo:str}', response_model= TareaId)
def get_tarea(titulo, db: Session = Depends(get_db)):
    tarea_by_titulo = crud.get_tarea_por_titulo(db=db, titulo=titulo)
    if tarea_by_titulo:
        return tarea_by_titulo
    raise HTTPException(status_code=404, detail="Tarea no encontrada!!")
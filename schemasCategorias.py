from pydantic import BaseModel

class CategoriaDate(BaseModel):
    nombre: str

class CategoriaId(CategoriaDate):
    idCategoria: int
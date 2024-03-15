from pydantic import BaseModel

class TareaDate(BaseModel):
    titulo: str
    descripcion: str
    categoria_id: int


class TareaId(TareaDate):
    idTarea: int

class TareaFecha(TareaDate):
    fecha_actual: str






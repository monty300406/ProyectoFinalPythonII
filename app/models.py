from pydantic import BaseModel
from typing import Optional

class Celular(BaseModel):
    id: int
    marca: str
    modelo: str
    precio: float

class Cliente(BaseModel):
    id: int
    nombre: str
    email: str

class Proveedor(BaseModel):
    id: int
    nombre: str
    telefono: str

# Modelos para creación (sin id porque se genera automático)
class CelularCreate(BaseModel):
    marca: str
    modelo: str
    precio: float

class ClienteCreate(BaseModel):
    nombre: str
    email: str

class ProveedorCreate(BaseModel):
    nombre: str
    telefono: str

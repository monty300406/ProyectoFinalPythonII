from typing import List
from app.models import Celular, Cliente, Proveedor

celulares: List[Celular] = [
    Celular(id=1, marca="Samsung", modelo="Galaxy S21", precio=1800000),
    Celular(id=2, marca="Apple", modelo="iPhone 13", precio=2250000),
]

clientes: List[Cliente] = [
    Cliente(id=1, nombre="Carlos Cardenas", email="Carlos@mail.com"),
    Cliente(id=2, nombre="Maria De Los Angeles Espinosa", email="mariadelosangeles@mail.com"),
]

proveedores: List[Proveedor] = [
    Proveedor(id=1, nombre="Vidrio Listo JM", telefono="123456789"),
    Proveedor(id=2, nombre="Farmatodo", telefono="987654321"),
]

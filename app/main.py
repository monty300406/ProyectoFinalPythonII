from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
from app.models import Celular, Cliente, Proveedor
from app.data import celulares, clientes, proveedores

import os

app = FastAPI()

# Montar carpeta "static" correctamente
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# Plantillas HTML (Jinja2)
templates = Jinja2Templates(directory="app/templates")


# === MODELOS DE ENTRADA PARA JSON ===

class CelularInput(BaseModel):
    marca: str
    modelo: str
    precio: float

class ClienteInput(BaseModel):
    nombre: str
    email: str
    telefono: str

class ProveedorInput(BaseModel):
    nombre: str
    empresa: str
    telefono: str

# === RUTAS FRONTEND (FORMULARIO) ===

@app.get("/", response_class=HTMLResponse)
def form_index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "celulares": celulares,
        "clientes": clientes,
        "proveedores": proveedores
    })

@app.post("/guardar", response_class=HTMLResponse)
def guardar_datos(
    request: Request,
    tipo: str = Form(...),
    marca: str = Form(None),
    modelo: str = Form(None),
    precio: float = Form(None),
    nombre: str = Form(None),
    email: str = Form(None),
    telefono: str = Form(None),
    empresa: str = Form(None)
):
    if tipo == "celular" and marca and modelo and precio is not None:
        nuevo = Celular(
            id=len(celulares) + 1,
            marca=marca,
            modelo=modelo,
            precio=precio
        )
        celulares.append(nuevo)

    elif tipo == "cliente" and nombre and email and telefono:
        nuevo = Cliente(
            id=len(clientes) + 1,
            nombre=nombre,
            email=email,
            telefono=telefono
        )
        clientes.append(nuevo)

    elif tipo == "proveedor" and nombre and empresa and telefono:
        nuevo = Proveedor(
            id=len(proveedores) + 1,
            nombre=nombre,
            empresa=empresa,
            telefono=telefono
        )
        proveedores.append(nuevo)

    return RedirectResponse("/", status_code=303)

# === RUTAS API PARA POSTMAN (JSON) ===

@app.get("/celulares", response_model=List[Celular])
def get_celulares():
    return celulares

@app.post("/celulares", response_model=Celular)
def create_celular(celular: CelularInput):
    new_id = max([c.id for c in celulares], default=0) + 1
    nuevo = Celular(id=new_id, **celular.dict())
    celulares.append(nuevo)
    return nuevo

@app.put("/celulares/{celular_id}", response_model=Celular)
def update_celular(celular_id: int, celular: CelularInput):
    for idx, c in enumerate(celulares):
        if c.id == celular_id:
            celulares[idx] = Celular(id=celular_id, **celular.dict())
            return celulares[idx]
    return {"error": "Celular no encontrado"}

@app.delete("/celulares/{celular_id}")
def delete_celular(celular_id: int):
    for idx, c in enumerate(celulares):
        if c.id == celular_id:
            del celulares[idx]
            return {"mensaje": f"Celular con ID {celular_id} eliminado"}
    return {"error": "Celular no encontrado"}

@app.get("/clientes", response_model=List[Cliente])
def get_clientes():
    return clientes

@app.post("/clientes", response_model=Cliente)
def create_cliente(cliente: ClienteInput):
    new_id = max([c.id for c in clientes], default=0) + 1
    nuevo = Cliente(id=new_id, **cliente.dict())
    clientes.append(nuevo)
    return nuevo

@app.put("/clientes/{cliente_id}", response_model=Cliente)
def update_cliente(cliente_id: int, cliente: ClienteInput):
    for idx, c in enumerate(clientes):
        if c.id == cliente_id:
            clientes[idx] = Cliente(id=cliente_id, **cliente.dict())
            return clientes[idx]
    return {"error": "Cliente no encontrado"}

@app.delete("/clientes/{cliente_id}")
def delete_cliente(cliente_id: int):
    for idx, c in enumerate(clientes):
        if c.id == cliente_id:
            del clientes[idx]
            return {"mensaje": f"Cliente con ID {cliente_id} eliminado"}
    return {"error": "Cliente no encontrado"}



@app.get("/proveedores", response_model=List[Proveedor])
def get_proveedores():
    return proveedores

@app.post("/proveedores", response_model=Proveedor)
def create_proveedor(proveedor: ProveedorInput):
    new_id = max([p.id for p in proveedores], default=0) + 1
    nuevo = Proveedor(id=new_id, **proveedor.dict())
    proveedores.append(nuevo)
    return nuevo

@app.put("/proveedores/{proveedor_id}", response_model=Proveedor)
def update_proveedor(proveedor_id: int, proveedor: ProveedorInput):
    for idx, c in enumerate(proveedores):
        if c.id == proveedor_id:
            proveedores[idx] = Proveedor(id=proveedor_id, **proveedor.dict())
            return proveedores[idx]
    return {"error": "Proveedor no encontrado"}

@app.delete("/proveedores/{proveedor_id}")
def delete_proveedor(proveedor_id: int):
    for idx, c in enumerate(proveedores):
        if c.id == proveedor_id:
            del proveedores[idx]
            return {"mensaje": f"Proveedor con ID {proveedor_id} eliminado"}
    return {"error": "Proveedor no encontrado"}
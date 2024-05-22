from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, StringConstraints, validator
from typing_extensions import Annotated
import helpers
import database as db


headers = {"content-type": "charset=utf-8"} 

class ModeloCliente(BaseModel):
    dni: Annotated[str, StringConstraints(min_length=9, max_length=9)]
    nombre: Annotated[str, StringConstraints(min_length=3, max_length=30)]
    apellido: Annotated[str, StringConstraints(min_length=3, max_length=30)]


class ModeloCrearCliente(ModeloCliente):
    @validator('dni')
    def validar_dni(cls, dni):
        if helpers.validate_dni(dni, db.Clientes.lista):
            return dni
        raise ValueError("Cliente existente o DNI incorrecto") 


app = FastAPI(
    title="API Gestor de clientes",
    description="Diferentes funciones para gestionar los clientes"
)


@app.get('/clientes/', tags=["Clientes"])
async def clientes():
    content = [cliente.to_dict() for cliente in db.Clientes.lista]
    return JSONResponse(content=content, headers=headers)


@app.get('/clientes/buscar/{dni}/', tags=["Clientes"])
async def clientes_buscar(dni: str):
    cliente = db.Clientes.buscar(dni=dni)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return JSONResponse(content=cliente.to_dict(), headers=headers)


@app.post('/clientes/crear/', tags=["Clientes"])
async def clientes_crear(datos: ModeloCrearCliente):
    cliente = db.Clientes.crear(datos.dni, datos.nombre, datos.apellido)
    if cliente:
        return JSONResponse(content=cliente.to_dict(), headers=headers)
    raise HTTPException(status_code=404, detail="Cliente no creado")


@app.put('/clientes/actualizar/', tags=["Clientes"])
async def clientes_actualizar(datos: ModeloCliente):
    if db.Clientes.buscar(datos.dni):
        cliente = db.Clientes.modificar(datos.dni, datos.nombre, datos.apellido)
        if cliente:
            return JSONResponse(content=cliente.to_dict(), headers=headers)
    raise HTTPException(status_code=404, detail="Cliente no creado")

    
@app.delete('/clientes/borrar/{dni}/', tags=["Clientes"])
async def clientes_borrar(dni: str):    
    if db.Clientes.buscar(dni=dni):
        cliente = db.Clientes.borrar(dni=dni)
        return JSONResponse(content=cliente.to_dict(), headers=headers)
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

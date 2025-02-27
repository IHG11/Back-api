from pydantic import BaseModel, Field
from datetime import date

class UsuarioDTOPeticion(BaseModel):
    nombre:str
    edad:int
    telefono:str
    correo:str 
    contraseña:str
    fechaRegistro:date
    ciudad:str 
    class Config:
        orm_mode=True

class UsuarioDTORespuesta(BaseModel):
    id:int
    nombre:str
    telefono: str
    ciudad: str
    class Config:
        orm_mode=True

class GastoDTOPeticion(BaseModel):
    monto:int
    fecha:date
    descripcion:str
    nombre:str
    class config:
        orm_mode=True

class GastoDTORespuesta(BaseModel):
    id:int
    monto:int
    fecha:date
    descripcion:str
    nombre:str
    class config:
        orm_mode=True

class IngresoDTOPeticion(BaseModel):
    monto: int
    fecha: date
    descripcion: str
    nombre: str
    class Config:
        orm_mode = True

class IngresoDTORespuesta(BaseModel):
    id: int  
    monto: int
    fecha: date
    descripcion: str
    nombre: str
    class Config:
        orm_mode = True

class CategoriaDTOPeticion(BaseModel):
    monto: int
    fecha: date
    nombre: str
    descripcion: str
    class config:
        orm_mode=True

class CategoriaDTORespuesta(BaseModel):
    id: int
    monto: int
    fecha: date
    nombre: str
    descripcion: str
    class Config:
        orm_mode = True

class MetodopagoDTOPeticion(BaseModel):
    monto: int
    fecha: date
    nombre: str
    descripcion: str
    class Config:
        orm_mode = True

class MetodopagoDTORespuesta(BaseModel):
    id: int
    monto: int
    fecha: date
    nombre: str
    descripcion: str
    class config:
        orm_mode=True



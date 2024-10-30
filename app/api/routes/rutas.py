from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.api.schemas.DTO import UsuarioDTOPeticion, UsuarioDTORespuesta
from app.api.models.modelosApp import Usuario
from app.api.schemas.DTO import GastoDTOPeticion, GastoDTORespuesta
from app.api.models.modelosApp import Gasto
from app.api.schemas.DTO import IngresoDTOPeticion, IngresoDTORespuesta
from app.api.models.modelosApp import Ingreso
from app.database.configuration import sessionLocal, engine

#Para que un api funcione debe tener un archivo enrutador
rutas=APIRouter() #ENDPOINTS

#Crear una funcion para establecer cuando yo quiera y necesite
#conexion hacia la base de datos
def getDataBase():
    basedatos=sessionLocal()
    try:
        yield basedatos
    except Exception as error:
        basedatos.rollback()
        raise error
    finally:
        basedatos.close()

#PROGRAMACION DE CADA UNO DE LOS SERVICIOS
#QUE OFRECERA NUESTRA API

#SERVICIO PARA REGISTRAR O GUARDAR UN USUARIO EN BD
@rutas.post("/usuarios", response_model=UsuarioDTORespuesta)
def guardarUsuario(datosPeticion:UsuarioDTOPeticion, db:Session=Depends(getDataBase) ):
    try:
        usuario=Usuario(
            nombres=datosPeticion.nombre,
            edad=datosPeticion.edad,
            telefono=datosPeticion.telefono,
            correo=datosPeticion.correo,
            contraseña=datosPeticion.contraseña,
            fechaRegistro=datosPeticion.fechaRegistro,
            ciudad=datosPeticion.ciudad
        )
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return UsuarioDTORespuesta(
            id=usuario.id,
            nombre=usuario.nombres,  # Asegúrate de usar el campo correcto
            telefono=usuario.telefono,
            ciudad=usuario.ciudad
        )
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar el usuario")


    try:
        usuario=Usuario(
            nombres=datosPeticion.nombre,
            edad=datosPeticion.edad,
            telefono=datosPeticion.telefono,
            correo=datosPeticion.correo,
            contraseña=datosPeticion.contraseña,
            fechaRegistro=datosPeticion.fechaRegistro,
            ciudad=datosPeticion.ciudad
        )
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return UsuarioDTORespuesta(
            id=usuario.id,
            nombre=usuario.nombres,  # Asegúrate de usar el campo correcto
            telefono=usuario.telefono,
            ciudad=usuario.ciudad
        )
    except Exception as error:
        db.rollback()
        raise HTTPException()

@rutas.get("/usuarios", response_model=List[UsuarioDTORespuesta])
def buscarUsuarios(db:Session=Depends(getDataBase)):
    try:
        listadoDeUsuarios=db.query(Usuario).all()
        return [
            UsuarioDTORespuesta(
                id=usuario.id,
                nombre=usuario.nombres, 
                telefono=usuario.telefono,
                ciudad=usuario.ciudad
            ) for usuario in listadoDeUsuarios
        ]
    except Exception as error:
        db.rollback()
        raise HTTPException()

@rutas.post("/gastos", response_model=GastoDTORespuesta)
def guardarGasto(datosPeticion: GastoDTOPeticion, db: Session = Depends(getDataBase)):
    try:
        gasto = Gasto(
            monto=datosPeticion.monto,
            fecha=datosPeticion.fecha,
            descripcion=datosPeticion.descripcion,
            nombre=datosPeticion.nombre
        )
        db.add(gasto)
        db.commit()
        db.refresh(gasto)
        return GastoDTORespuesta(
            id=gasto.id,
            monto=gasto.monto,
            fecha=gasto.fecha,
            descripcion=gasto.descripcion,
            nombre=gasto.nombre
        )
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar el gasto")

# Servicio para obtener todos los gastos
@rutas.get("/gastos", response_model=List[GastoDTORespuesta])
def buscarGastos(db: Session = Depends(getDataBase)):
    try:
        listadoDeGastos = db.query(Gasto).all()
        return [
            GastoDTORespuesta(
                id=gasto.id,
                monto=gasto.monto,
                fecha=gasto.fecha,
                descripcion=gasto.descripcion,
                nombre=gasto.nombre
            ) for gasto in listadoDeGastos
        ]
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al buscar los gastos")
    
@rutas.post("/ingresos", response_model=IngresoDTORespuesta)
def guardarIngreso(datosPeticion: IngresoDTOPeticion, db: Session = Depends(getDataBase)):
    try:
        ingreso = Ingreso(
            monto=datosPeticion.monto,
            fecha=datosPeticion.fecha,
            descripcion=datosPeticion.descripcion,
            nombre=datosPeticion.nombre
        )
        db.add(ingreso)
        db.commit()
        db.refresh(ingreso)
        return IngresoDTORespuesta(
            id=ingreso.id,
            monto=ingreso.monto,
            fecha=ingreso.fecha,
            descripcion=ingreso.descripcion,
            nombre=ingreso.nombre
        )
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar el ingreso")

# Servicio para obtener una lista de ingresos
@rutas.get("/ingresos", response_model=List[IngresoDTORespuesta])
def buscarIngresos(db: Session = Depends(getDataBase)):
    try:
        listadoDeIngresos = db.query(Ingreso).all()
        return [
            IngresoDTORespuesta(
                id=ingreso.id,
                monto=ingreso.monto,
                fecha=ingreso.fecha,
                descripcion=ingreso.descripcion,
                nombre=ingreso.nombre
            ) for ingreso in listadoDeIngresos
        ]
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al buscar ingresos")












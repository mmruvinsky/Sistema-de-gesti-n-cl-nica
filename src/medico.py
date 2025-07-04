from src.especialidad import Especialidad
from src.validadores import _validar_matricula, _validar_nombre
import re
from src.excepciones import (
    MedicoInvalidoException,
    MatriculaInvalidaException
)

class Medico:
    
    def __init__(self, nombre: str, matricula: str, especialidades: list[Especialidad]):
        self.__nombre = _validar_nombre(nombre) 
        self.__matricula =_validar_matricula(matricula)
        self.__especialidades = especialidades.copy()

# GETTERS

    def obtener_matricula(self) -> str:
        return self.__matricula
    
    def obtener_nombre(self) -> str:
        return self.__nombre
    
    def obtener_especialidades(self) -> list[Especialidad]:
        return self.__especialidades.copy()
    
    def obtener_especialidad_para_dia(self, dia: str) -> str | None:
        for especialidad in self.__especialidades:
            if especialidad.verificar_dia(dia):
                return especialidad.obtener_especialidad()
        return None
    
# AGREGAR
    
    def agregar_especialidad(self, especialidad: Especialidad) -> None:
        if especialidad not in self.__especialidades:
            self.__especialidades.append(especialidad)
       
    def __str__(self) -> str:
        return f"Medico: {self.__nombre}, Matricula: {self.__matricula}, Especialidades: {self.__especialidades}"
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
        dia_normalizado = dia.lower().strip()
        for especialidad in self.__especialidades:
            if especialidad.verificar_dia(dia_normalizado):
                return especialidad.obtener_especialidad()
        return None
    
# AGREGAR
    
    def agregar_especialidad(self, especialidad: Especialidad) -> None:
        if especialidad not in self.__especialidades:
            self.__especialidades.append(especialidad)
       
    def __str__(self) -> str:
        if self.__especialidades:
            especialidades_str = ", ".join(str(esp) for esp in self.__especialidades)
            return f"Medico: {self.__nombre}, Matricula: {self.__matricula}, Especialidades: [{especialidades_str}]"
        else:
            return f"Medico: {self.__nombre}, Matricula: {self.__matricula}, Sin especialidades"
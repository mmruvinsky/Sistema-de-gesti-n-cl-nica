import re
from src.excepciones import ( DNIInvalidoException, PacienteInvalidoException, FechaInvalidaException ) 
from datetime import datetime
from src.validadores import _validar_dni, _validar_fecha, _validar_nombre

class Paciente:

    def __init__(self, nombre: str, dni: str, fecha_de_nacimiento: str):
        self.__nombre = _validar_nombre(nombre)  
        self.__dni = _validar_dni(dni)
        self.__fecha_de_nacimiento = _validar_fecha(fecha_de_nacimiento)  

# GETTERS

    def obtener_nombre(self) -> str:
        return self.__nombre

    def obtener_dni(self) -> str:
        return self.__dni
    
    def __str__(self) -> str:
        return f"Paciente: {self.__nombre}, DNI: {self.__dni}, Fecha de nacimiento: {self.__fecha_de_nacimiento}"
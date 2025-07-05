from src.paciente import Paciente
from src.medico import Medico
from src.excepciones import RecetaInvalidaException
from datetime import datetime

class Receta:
    def __init__(self, paciente: Paciente, medico: Medico, medicamentos: list[str]):
        if not medicamentos:
            raise ValueError("La receta debe contener al menos un medicamento.")

        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos
        self.__fecha = datetime.now()

  
    def __str__(self) -> str:
        medicamentos_str = ", ".join(self.__medicamentos)
        fecha_str = self.__fecha.strftime("%d/%m/%Y")
        
        return (
            f"Receta:\n"
            f"   Paciente: {self.__paciente.obtener_nombre()}\n"
            f"   DNI: {self.__paciente.obtener_dni()}\n"
            f"   Médico: {self.__medico.obtener_nombre()}\n"
            f"   Matrícula: {self.__medico.obtener_matricula()}\n"
            f"   Medicamentos: {medicamentos_str}\n"
            f"   Fecha: {fecha_str}"
        )
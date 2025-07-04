from src.excepciones import (
    ClinicaException,
    PacienteInvalidoException,
    MedicoInvalidoException,
    DNIInvalidoException,
    MatriculaInvalidaException,
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    MedicoNoEncontradoException,
    HistoriaClinicaNoEncontradaException,
    TurnoOcupadoException,
    RecetaInvalidaException,
    FechaInvalidaException
)
from datetime import datetime
import re


def _validar_nombre(nombre: str) -> str:
        # Verificar que el nombre no esté vacío
        if not nombre:
            raise PacienteInvalidoException("El nombre del paciente no puede estar vacío")
        
        nombre_limpio = nombre.strip()
        
        if not nombre_limpio:
            raise PacienteInvalidoException("El nombre del paciente no puede estar vacío")
        
        # Verificar que el nombre no tenga números ni caracteres especiales
        if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$', nombre_limpio):
            raise PacienteInvalidoException("El nombre solo puede contener letras y espacios")
        
        return nombre_limpio  


def _validar_dni(dni: str) -> str:
        # Verificar que el DNI no esté vacío
        if not dni:
            raise DNIInvalidoException("El DNI no puede estar vacío")
        
        # Eliminar puntos y espacios
        dni_limpio = re.sub(r'[.\s]', '', dni)
        
        # Verificar que solo contenga números
        if not dni_limpio.isdigit():
            raise DNIInvalidoException("El DNI debe contener solo números")
        
        # Verificar que tenga 7 u 8 dígitos
        if not 7 <= len(dni_limpio) <= 8:
            raise DNIInvalidoException("DNI inválido. Debe tener 7 u 8 dígitos")
        
        return dni_limpio


def _validar_fecha(fecha_str: str) -> datetime:
        # Verificar que la fecha no esté vacía
        if not fecha_str or not fecha_str.strip():
            raise FechaInvalidaException("La fecha no puede estar vacía")
        
        # Verificar el formato de la fecha
        try:
            fecha_limp = datetime.strptime(fecha_str.strip(), "%d/%m/%Y")
        except ValueError:
            raise FechaInvalidaException("La fecha debe tener formato dd/mm/aaaa y ser válida")
        
        # Verificar coherencia de la fecha
        fecha_act = datetime.today().date()

        if fecha_limp.date() > fecha_act:
            raise FechaInvalidaException("La fecha no puede estar en el futuro")
        
        limite_min = datetime.strptime("01/01/1900", "%d/%m/%Y")
        if fecha_limp < limite_min:
            raise FechaInvalidaException("La fecha no puede ser anterior al 01/01/1900")

        return fecha_limp


def _validar_matricula(matricula: str) -> str:
        
         # Verificar que la matrícula no esté vacía
        if not matricula:
            raise MatriculaInvalidaException("La matrícula no puede estar vacía")
        
        # Verificar el formato de la matrícula
        matricula_limpia = matricula.strip().upper()
        patron_matricula = r'^M[NP]\d{4,6}$'
        
        if not re.match(patron_matricula, matricula_limpia):
            raise MatriculaInvalidaException("Matrícula inválida. Formato: MN##### o MP##### (4-6 dígitos)")
        
        return matricula_limpia


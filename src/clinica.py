from typing import List, Dict
from src.paciente import Paciente
from src.medico import Medico
from src.turno import Turno
from src.historia_clinica import HistoriaClinica
from datetime import datetime
from src.receta import Receta
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
    RecetaInvalidaException
)

class Clinica:
    def __init__(self, medicos: dict[str, Medico], pacientes: dict[str, Paciente], turnos: list[Turno], historias_clinicas: dict[str, HistoriaClinica]) -> None:
        self.__medicos = medicos
        self.__pacientes = pacientes
        self.__turnos = turnos
        self.__historias_clinicas = historias_clinicas


# AGREGAR

    def agregar_medico(self, medico: Medico) -> None:
        # VERIFICAR SI EL MÉDICO ESTÁ REGISTRADO EN LA CLINICA
        if medico.obtener_matricula() in self.__medicos:
            print(f"El médico con matrícula {medico.obtener_matricula()} ya está registrado.")

        else:
            self.__medicos[medico.obtener_matricula()] = medico
            print(f"Médico {medico.obtener_nombre()} agregado correctamente.")


    def agregar_paciente(self, paciente: Paciente) -> None:
        # VERIFICAR SI EL PACIENTE ESTÁ REGISTRADO EN LA CLINICA
        if paciente.obtener_dni() in self.__pacientes:
            print(f"El paciente con DNI {paciente.obtener_dni()} ya está registrado.")
        else:
            self.__pacientes[paciente.obtener_dni()] = paciente
            print(f"Paciente {paciente.obtener_nombre()} agregado correctamente.")


# AGENDAR TURNO

    def agendar_turno(self, dni: str, matricula: str, especialidad: str, fecha_hora: datetime) -> Turno:

        # VERIFICAR SI EL PACIENTE ESTÁ REGISTRADO EN LA CLÍNICA
        if not self.validar_existencia_paciente(dni):
            raise PacienteNoEncontradoException(
                f"Paciente con DNI {dni} no está registrado en la clínica"
            )

        # VERIFICAR SI EL MÉDICO ESTÁ REGISTRADO EN LA CLÍNICA
        if not self.validar_existencia_medico(matricula):
            raise MedicoNoEncontradoException(
                f"Médico con matrícula {matricula} no está registrado en la clínica"
            )

        # OBTENER LOS OBJETOS
        paciente = self.obtener_paciente_por_dni(dni)
        medico = self.obtener_medico_por_matricula(matricula)

        # VALIDAR ESPECIALIDAD
        especialidad_normalizada = especialidad.lower().strip()
        tiene_especialidad = any(
            esp.obtener_especialidad().lower().strip() == especialidad_normalizada
            for esp in medico.obtener_especialidades()
        )

        if not tiene_especialidad:
            raise MedicoNoDisponibleException(
                f"El médico no atiende la especialidad {especialidad}"
            )

        # VALIDAR SI EL MÉDICO ATIENDE ESA ESPECIALIDAD ESE DÍA
        dia_semana = self.obtener_dia_semana_en_espanol(fecha_hora)
        especialidad_para_dia = medico.obtener_especialidad_para_dia(dia_semana)

        if (
            not especialidad_para_dia
            or especialidad_para_dia.lower().strip() != especialidad_normalizada
        ):
            raise MedicoNoDisponibleException(
                f"El médico no atiende {especialidad} los {dia_semana}"
            )

        # VALIDAR TURNO DUPLICADO
        if self.validar_turno_duplicado(matricula, fecha_hora):
            raise TurnoOcupadoException(
                "Ya existe un turno para ese médico en esa fecha y hora"
            )

        # CREAR EL TURNO (después de todas las validaciones)
        turno = Turno(paciente, medico, fecha_hora, especialidad)

        # AGREGAR EL TURNO
        self.__turnos.append(turno)

        historia = self.obtener_historia_clinica_por_DNI(dni)
        if historia:
            historia.agregar_turno(turno)
        else:
            nueva_historia = HistoriaClinica(paciente)
            nueva_historia.agregar_turno(turno)
            self.__historias_clinicas[dni] = nueva_historia

        return turno
    
# EMITIR RECETA

    def emitir_receta(self, dni: str, matricula: str, medicamentos: list[str]) -> str:
        
        # VALIDACIONES BÁSICAS
        if not self.validar_existencia_paciente(dni):
            raise RecetaInvalidaException(f"Error: Paciente con DNI {dni} no está registrado en la clínica")
            
        if not self.validar_existencia_medico(matricula):
            raise RecetaInvalidaException(f"Error: Médico con matrícula {matricula} no está registrado en la clínica")
        
        if not medicamentos:
            raise RecetaInvalidaException("Error: La receta debe contener al menos un medicamento")
        
        # OBTENER OBJETOS
        paciente = self.obtener_paciente_por_dni(dni)
        medico = self.obtener_medico_por_matricula(matricula)
        
        # CREAR LA RECETA
        receta = Receta(paciente, medico, medicamentos)
            
        # AGREGAR A LA HISTORIA CLÍNICA
        historia = self.obtener_historia_clinica_por_DNI(dni)
        if historia:
                historia.agregar_receta(receta)
        else:
                # Crear historia clínica si no existe
                nueva_historia = HistoriaClinica(paciente)
                nueva_historia.agregar_receta(receta)
                self.__historias_clinicas[dni] = nueva_historia
            
        return f"Receta emitida correctamente para {paciente.obtener_nombre()}"
            
# OBTENER

    def obtener_medicos_dict(self) -> dict[str, Medico]:
        return self.__medicos
    
    def obtener_pacientes_dict(self) -> dict[str, Paciente]:
        return self.__pacientes
    
    def obtener_medico_por_matricula(self, matricula: str) -> Medico | None:
        medico = self.__medicos.get(matricula)
        if medico is None:
            raise MedicoNoEncontradoException(f"Médico con matrícula {matricula} no encontrado")
        return medico
    
    def obtener_paciente_por_dni(self, dni: str) -> Paciente | None:
        paciente = self.__pacientes.get(dni)
        if paciente is None:
            raise PacienteNoEncontradoException(f"Paciente con DNI: {dni} no encontrado")
        return paciente
    
    def obtener_historia_clinica_por_DNI(self, dni: str) -> HistoriaClinica | None: 
        hc = self.__historias_clinicas.get(dni) 
        if hc is None:
            return None 
        return hc

    def obtener_turnos(self) -> list[Turno]:  
        return self.__turnos.copy()  
    
    def obtener_pacientes(self) -> list[Paciente]:
        return list(self.__pacientes.values())

    def obtener_medicos(self) -> list[Medico]:
        return list(self.__medicos.values())
        
    def obtener_especialidad_disponible(self, medico: Medico, dia_semana: str) -> str | None:
        return medico.obtener_especialidad_para_dia(dia_semana)
    
    def obtener_dia_semana_en_espanol(self, fecha_hora: datetime) -> str:
        dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
        return dias[fecha_hora.weekday()]
    
    
# VALIDACIONES INTERNAS CLASE CLINICA
    
    def validar_existencia_paciente(self, dni: str) -> bool:
        if dni in self.__pacientes:
            return True
        else:
            return False
           
    def validar_existencia_medico(self, matricula: str) -> bool:
            if matricula in self.__medicos:
                return True
            else:
                return False
                     
    def validar_turno_duplicado(self, matricula: str, fecha_hora: datetime) -> bool:
            for turno in self.__turnos:
                if (turno.obtener_medico().obtener_matricula() == matricula and 
                    turno.obtener_fecha_hora() == fecha_hora):
                    return True     
            return False 
    
    
    
    


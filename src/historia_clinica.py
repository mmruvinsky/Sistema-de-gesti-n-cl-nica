from src.turno import Turno
from src.paciente import Paciente
from src.receta import Receta
from src.turno import Turno

class HistoriaClinica:

    def __init__(self, paciente: Paciente):
        self.__paciente = paciente
        self.__turnos = []
        self.__recetas = []

# OBTENER

    def obtener_turnos(self) -> list[Turno]:
        return self.__turnos.copy()

    def obtener_recetas(self) -> list[Receta]:
        return self.__recetas.copy()

# AGREGAR

    def agregar_turno(self, turno: Turno) -> None:
        self.__turnos.append(turno)

    def agregar_receta(self, receta: Receta) -> None:
        self.__recetas.append(receta)

    def __str__(self) -> str:
        resultado = f"📄 HISTORIA CLÍNICA\n"
        resultado += f"{'='*50}\n"
        resultado += f"👤 Paciente: {self.__paciente.obtener_nombre()}\n"
        resultado += f"🆔 DNI: {self.__paciente.obtener_dni()}\n"
        resultado += f"📅 Fecha de nacimiento: {self.__paciente.obtener_fecha_nacimiento().strftime('%d/%m/%Y')}\n"
        resultado += f"{'='*50}\n"
        
        # Sección de turnos
        resultado += f"\n📋 TURNOS:\n"
        resultado += f"{'-'*30}\n"
        if self.__turnos:
            for i, turno in enumerate(self.__turnos, 1):
                resultado += f"{i}. Médico: {turno.obtener_medico().obtener_nombre()}\n"
                resultado += f"   Matrícula: {turno.obtener_medico().obtener_matricula()}\n"
                resultado += f"   Especialidad: {turno.obtener_especialidad()}\n"
                resultado += f"   Fecha: {turno.obtener_fecha_hora().strftime('%d/%m/%Y %H:%M')}\n"
                resultado += f"\n"
        else:
            resultado += "   Sin turnos registrados\n"
        
        # Sección de recetas
        resultado += f"\n💊 RECETAS:\n"
        resultado += f"{'-'*30}\n"
        if self.__recetas:
            for i, receta in enumerate(self.__recetas, 1):
                resultado += f"{i}. {receta}\n"
        else:
            resultado += "   Sin recetas registradas\n"
        
        return resultado
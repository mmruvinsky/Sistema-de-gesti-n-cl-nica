import unittest
import sys
import os
from src.receta import Receta
from src.paciente import Paciente
from src.medico import Medico
from src.especialidad import Especialidad
from src.excepciones import RecetaInvalidaException
from datetime import datetime


class TestReceta(unittest.TestCase):
    
    def setUp(self):
        self.paciente_valido = Paciente("Juan Pérez", "12345678", "01/01/1990")
        especialidad = Especialidad("Cardiología", ["lunes", "martes"])
        self.medico_valido = Medico("Juan García", "MN1234", [especialidad])
    
    def test_crear_receta_valida(self):
        medicamentos = ["Paracetamol", "Ibuprofeno"]
        receta = Receta(self.paciente_valido, self.medico_valido, medicamentos)
        self.assertIsNotNone(receta)
    
    def test_crear_receta_sin_medicamentos_error(self):
        with self.assertRaises(ValueError):
            Receta(self.paciente_valido, self.medico_valido, [])
    
    def test_crear_receta_medicamentos_none_error(self):
        with self.assertRaises(ValueError):
            Receta(self.paciente_valido, self.medico_valido, None)
    
    def test_crear_receta_un_medicamento(self):
        medicamentos = ["Paracetamol"]
        receta = Receta(self.paciente_valido, self.medico_valido, medicamentos)
        self.assertIsNotNone(receta)
    
    def test_crear_receta_multiples_medicamentos(self):
        medicamentos = ["Paracetamol", "Ibuprofeno", "Aspirina"]
        receta = Receta(self.paciente_valido, self.medico_valido, medicamentos)
        self.assertIsNotNone(receta)
    
    def test_str_representation(self):
        medicamentos = ["Paracetamol", "Ibuprofeno"]
        receta = Receta(self.paciente_valido, self.medico_valido, medicamentos)
        fecha_actual = datetime.now().strftime("%d/%m/%Y")
        
        expected = (
            f"Receta:\n"
            f"   Paciente: {self.paciente_valido.obtener_nombre()}\n"
            f"   DNI: {self.paciente_valido.obtener_dni()}\n"
            f"   Médico: {self.medico_valido.obtener_nombre()}\n"
            f"   Matrícula: {self.medico_valido.obtener_matricula()}\n"
            f"   Medicamentos: Paracetamol, Ibuprofeno\n"
            f"   Fecha: {fecha_actual}"
        )
        self.assertEqual(str(receta), expected)

    def test_str_representation_un_medicamento(self):
        medicamentos = ["Paracetamol"]
        receta = Receta(self.paciente_valido, self.medico_valido, medicamentos)
        fecha_actual = datetime.now().strftime("%d/%m/%Y")
        
        expected = (
            f"Receta:\n"
            f"   Paciente: {self.paciente_valido.obtener_nombre()}\n"
            f"   DNI: {self.paciente_valido.obtener_dni()}\n"
            f"   Médico: {self.medico_valido.obtener_nombre()}\n"
            f"   Matrícula: {self.medico_valido.obtener_matricula()}\n"
            f"   Medicamentos: Paracetamol\n"
            f"   Fecha: {fecha_actual}"
        )
        self.assertEqual(str(receta), expected)


if __name__ == '__main__':
    unittest.main()
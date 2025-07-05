import unittest
import sys
import os
from src.medico import Medico
from src.especialidad import Especialidad
from src.excepciones import (MedicoInvalidoException, MatriculaInvalidaException)


class TestMedico(unittest.TestCase):
    
    def setUp(self):
        self.esp_cardiologia = Especialidad("cardiologia", ["lunes", "miércoles"])
        self.esp_neurologia = Especialidad("neurologia", ["martes", "jueves"])
    
    def test_crear_medico_valido(self):
        medico = Medico("Juan Pérez", "MN1234", [self.esp_cardiologia])
        self.assertEqual(medico.obtener_nombre(), "Juan Pérez")
        self.assertEqual(medico.obtener_matricula(), "MN1234")
        self.assertEqual(len(medico.obtener_especialidades()), 1)
    
    def test_crear_medico_matricula_mn_4_digitos(self):
        medico = Medico("Ana García", "MN1234", [self.esp_cardiologia])
        self.assertEqual(medico.obtener_matricula(), "MN1234")
    
    def test_crear_medico_matricula_mn_6_digitos(self):
        medico = Medico("Carlos López", "MN123456", [self.esp_neurologia])
        self.assertEqual(medico.obtener_matricula(), "MN123456")
    
    def test_crear_medico_matricula_mp_4_digitos(self):
        medico = Medico("María González", "MP5678", [self.esp_cardiologia])
        self.assertEqual(medico.obtener_matricula(), "MP5678")
    
    def test_crear_medico_matricula_mp_6_digitos(self):
        medico = Medico("Laura Martínez", "MP567890", [self.esp_neurologia])
        self.assertEqual(medico.obtener_matricula(), "MP567890")
    
    def test_crear_medico_nombre_con_espacios(self):
        medico = Medico("José María Fernández", "MN1234", [self.esp_cardiologia])
        self.assertEqual(medico.obtener_nombre(), "José María Fernández")
    
    def test_crear_medico_nombre_con_acentos(self):
        medico = Medico("José María Peña", "MN1234", [self.esp_cardiologia])
        self.assertEqual(medico.obtener_nombre(), "José María Peña")
    
    def test_crear_medico_multiples_especialidades(self):
        medico = Medico("Multi Especialista", "MN1234", [self.esp_cardiologia, self.esp_neurologia])
        self.assertEqual(len(medico.obtener_especialidades()), 2)
    
    def test_matricula_vacia_error(self):
        with self.assertRaises(MatriculaInvalidaException):
            Medico("Test", "", [self.esp_cardiologia])
    
    def test_matricula_muy_corta_error(self):
        with self.assertRaises(MatriculaInvalidaException):
            Medico("Test", "MN12", [self.esp_cardiologia])
    
    def test_matricula_muy_larga_error(self):
        with self.assertRaises(MatriculaInvalidaException):
            Medico("Test", "MN1234567", [self.esp_cardiologia])
    
    def test_matricula_formato_incorrecto_sin_mn_mp_error(self):
        with self.assertRaises(MatriculaInvalidaException):
            Medico("Test", "AB1234", [self.esp_cardiologia])
    
    def test_matricula_formato_incorrecto_con_letras_error(self):
        with self.assertRaises(MatriculaInvalidaException):
            Medico("Test", "MN12A4", [self.esp_cardiologia])
    
    def test_matricula_formato_incorrecto_solo_letras_error(self):
        with self.assertRaises(MatriculaInvalidaException):
            Medico("Test", "MNABCD", [self.esp_cardiologia])
    
    def test_obtener_especialidad_para_dia_existente(self):
        medico = Medico("Test", "MN1234", [self.esp_cardiologia])
        resultado = medico.obtener_especialidad_para_dia("lunes")
        self.assertEqual(resultado, "cardiologia")
    
    def test_obtener_especialidad_para_dia_no_existente(self):
        medico = Medico("Test", "MN1234", [self.esp_cardiologia])
        resultado = medico.obtener_especialidad_para_dia("viernes")
        self.assertIsNone(resultado)
    
    def test_agregar_especialidad_nueva(self):
        medico = Medico("Test", "MN1234", [self.esp_cardiologia])
        medico.agregar_especialidad(self.esp_neurologia)
        self.assertEqual(len(medico.obtener_especialidades()), 2)
    
    def test_agregar_especialidad_duplicada(self):
        medico = Medico("Test", "MN1234", [self.esp_cardiologia])
        medico.agregar_especialidad(self.esp_cardiologia)  # Misma especialidad
        self.assertEqual(len(medico.obtener_especialidades()), 1)
    
    def test_str_representation(self):
        medico = Medico("Juan Pérez", "MN1234", [self.esp_cardiologia])
        expected = f"Medico: Juan Pérez, Matricula: MN1234, Especialidades: {[str(self.esp_cardiologia)]}"
        self.assertEqual(str(medico), expected)


if __name__ == '__main__':
    unittest.main()
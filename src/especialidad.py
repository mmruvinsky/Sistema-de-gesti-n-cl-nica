
class Especialidad:
    
    def __init__(self, tipo: str, dias: list[str]):
        self.__tipo = tipo
        self.__dias = [d.lower() for d in dias]

    def verificar_dia(self, dia: str) -> bool:
        dia_normalizado = dia.lower().strip()
        return dia_normalizado in self.__dias

    def obtener_especialidad(self):
        return self.__tipo
    
    def obtener_dias(self):
        return self.__dias.copy()
    
    def __str__(self) -> str:
            return f"Tipo de especialidad: {self.__tipo}, Días: {self.__dias}"
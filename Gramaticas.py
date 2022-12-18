class Gramatica:
    def __init__(self, nombre, no_terminales, terminales, no_terminal_inicial, producciones) -> None:
        self.nombre = nombre
        self.no_terminales = no_terminales
        self.terminales = terminales
        self.no_terminale_inicial = no_terminal_inicial
        self.producciones = producciones
        

class Producciones:
    def __init__(self, no_terminal, expresiones) -> None:
        self.no_terminal = no_terminal
        self.expresiones = expresiones
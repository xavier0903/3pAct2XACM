class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("División sobre cero no esta permitido")
        return a / b
#comentario de prueba en calculadora.py

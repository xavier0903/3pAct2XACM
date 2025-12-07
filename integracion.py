from calculadora import Calculadora

def flujo_completo():
    calc = Calculadora()
    total = calc.suma(10, 5)
    return calc.divide(total, 3)

if __name__ == "__main__":
    print("Flujo integración OK:", flujo_completo())

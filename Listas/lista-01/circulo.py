class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcularArea(self):
        return 3.14 * (self.raio * self.raio)

    def calcularCircunferencia(self):
        return 2 * 3.14 * self.raio

    def __str__(self):
        return f"Circulo de raio {self.raio}"

def __main__():
    inst = int(input("Insira a quantidade de instâncias: "))

    circulos = []

    for n in range(0, inst):
        raio = int(input(f"Insira o raio do circulo {n + 1}: "))
        novo_circulo = Circulo(raio)

        circulos.append(novo_circulo)

    for n in range(0, inst):
        print(circulos[n])

__main__()
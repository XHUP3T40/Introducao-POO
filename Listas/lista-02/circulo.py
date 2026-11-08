class Circulo:
    def __init__(self, raio:float):
        self._raio = raio

    def calc_area(self) -> float:
        return 3.14*(self._raio**2)
    
    def calc_circunferencia(self) -> float: 
        return 2*3.14*self._raio
    
    def set_raio(self, v:float) -> None:
        self._raio = v

    def get_raio(self) -> float:
        return self._raio

    def __str__(self):
        return f"Círculo de raio {self._raio}"

    def __repr__(self):
        return self.__str__()

def __main__():

    circulos = []

    while True:
        print('''
            ==================================

            1 - Criar um novo círculo
            2 - Listar circulos
            3 - Atualizar raio de um círculo

            ==================================
        ''')

        opt = int(input("Informe a opção escolhida: "))

        match opt:
            case 1:

                raio = float(input("Insira o valor do raio do novo círculo: "))
                novo_circulo = Circulo(raio)

                circulos.append(novo_circulo)

                print("Novo circulo criado com sucesso")
            case 2:

                print(f"Lista de círculos criados: {circulos}")
            case 3:

                index = int(input("Informe o index do círculo na lista: "))
                selecionado = circulos[index]

                novo_raio = float(input("Informe o novo raio: "))
                selecionado.set_raio(novo_raio)

                print("Valor do raio atualizado com sucesso")
            case _:
                print("Opção inválida. Tente novamente")

__main__()
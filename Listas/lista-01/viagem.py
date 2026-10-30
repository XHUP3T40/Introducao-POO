class Viagem:
    def __init__(self, distancia, temp_h, temp_min):
        self.distancia = distancia
        self.temp_h = temp_h
        self.temp_min = temp_min

    def velocidade_media(self):
        return (self.distancia / (self.temp_h + self.temp_min / 60))
    
def __main__():
    inst = int(input("Insira a quantidade de viagens que foram feitas: "))

    viagens = []

    for n in range(0, inst):
        dist = float(input(f"Insira a distância da viagem {n + 1}: "))

        tem_h, tem_min = map(int, input(f"Quanto tempo demorou a viagem {n + 1} (HH:mm)? ").split(":"))

        # tem_h = int(input(f"Quantas horas demorou a viagem {n + 1}? "))
        # tem_min = int(input(f"e quantos minutos? "))

        nova_viagem = Viagem(distancia=dist, temp_h=tem_h, temp_min=tem_min)

        viagens.append(nova_viagem)

    for n in range(0, inst):
        print(f"Velocidade média da viagem {n + 1}: {int(viagens[n].velocidade_media())}Km/h")

__main__()
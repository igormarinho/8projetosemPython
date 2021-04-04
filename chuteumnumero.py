import random


class chuteOnumero():
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_min = 1
        self.valor_max = 100
        self.tentarNovamente = True;

    def iniciar(self):
        self.pedirvalor()
        self.GerarNumeroAleatório()#metodo

        while self.tentarNovamente == True:
            if self.valorchutado > self.valor_aleatorio:
                print("Chute um valor mais baixo")
                self.pedirvalor()
            elif self.valorchutado < self.valor_aleatorio:
                print("chute um valor mais alto")
                self.pedirvalor()

    def pedirvalor(self):
        self.valorchutado = int(input("chute o numero"))


    def GerarNumeroAleatório(self):
        self.valor_aleatorio= random.randint(self.valor_min,self.valor_max)

import random 
from random import shuffle

class cores(object):

    def __init__(self, cor, lados):
        self.cor = cor
        self.lados = lados

    def roll(self):
        return self.lados[random.randint(0,5)]

class Player(object):

    def __init__(self, nome, pontos):
        self.nome = nome
        self.pontos = pontos

    def rodada(self):
        print()
        print(f'A rodada comeca com: {self.nome} ')
        self.temp_pontos = {'cerebros': 0, 'tiros': 0}
        self.meuDado = Dadosgg()
        self.dadoRolado = []
        escolha = 'sim'
        while self.temp_pontos['tiros'] < 3 and escolha == 'sim' and len(self.meuDado) > 0:
            self.dadoRolado = self.escolherDado(self.dadoRolado)
            resultado = self.jogarDado(self.dadoRolado)
            resultado, self.dadoRolado = self.separarDados(resultado, self.dadoRolado)
            if self.temp_pontos['tiros'] >= 3:
                print("Voce tomou muitos tiros!")
                self.temp_pontos['cerebros'] = 0
                break
            escolha = self.Decisao()
            self.pontos += self.temp_pontos['cerebros']

    def escolherDado(self, dadoNaMao):
        while len(dadoNaMao) < 3:
            dadoNaMao.append(self.meuDado.pop())
        return dadoNaMao

    def jogarDado(self, dadoNaMao):
        resultadoJogada = []
        resultadoBasico = []
        for cada_cor in dadoNaMao:
            resultadoBasico.append(cada_cor.roll())
            resultadoJogada.append(cada_cor.cor + ' ' + resultadoBasico[-1])
        print(resultadoJogada)
        return resultadoBasico

    def separarDados(self, dadoNaMao, dadoOBJ):
        for i in range(2, -1, -1):
            if dadoNaMao[i] != "passos":
                self.temp_pontos[dadoNaMao[i]] += 1
                dadoNaMao.pop(i)
                dadoOBJ.pop(i)
        return dadoNaMao, dadoOBJ

    def Decisao(self):
        decisaoAgr = ''
        print(self.temp_pontos)
        while decisaoAgr != 'sim' and decisaoAgr != 'nao':
            decisaoAgr = input('continuar (sim/nao)? ')
        return decisaoAgr

def Dadosgg():
    tuboDeDados = []
    dadoVerde = cores('dadoVerde',["cerebros","passos","cerebros","tiros","passos","cerebros"])
    dadoVermelho = cores('dadoVermelho',["tiros","passos","tiros","cerebros","passos","tiros"])
    dadoAmarelo = cores('dadoAmarelo',["tiros","passos","cerebros","tiros","passos","cerebros"])
    
    for i in range(1, 6):
        tuboDeDados.append(dadoVerde)
    for i in range(1, 4):
        tuboDeDados.append(dadoAmarelo)
    for i in range(1, 3):
        tuboDeDados.append(dadoVermelho)
    
    shuffle(tuboDeDados)
    return tuboDeDados

def rodadaJogo(naRodada):
    for cadaJogador in naRodada:
        cadaJogador.rodada()
        print()
        print("Fim da rodada: ")
        display_pontos(naRodada)
    return naRodada

def criarJogadores():
    totalDeJogadores = int(input("Digite o numero de jogadores:  "))
    jogadores = []
    for i in range(1, totalDeJogadores+1):
        jogNome = input("Player %s nome: " % i)
        esseJogador = Player(jogNome, 0)
        jogadores.append(esseJogador)
        shuffle(jogadores)
        print()
        print("Ordem aleatoria de jogadores: ")
        for i in range(len(jogadores)):
            print(i+1, ':', jogadores[i].nome)
            print()
    return jogadores

def display_pontos(pontos):
    print("Os pontos sao:")
    for i in range(len(pontos)):
        print(pontos[i].nome, pontos[i].pontos)
        print()

def main():
    jogadores = criarJogadores()
    game_over = False
    while game_over == False:
        rodadaJogo(jogadores)
        for cadaJogador in jogadores:
            if cadaJogador.pontos == 13:
                game_over = True
                print("Game over. Pontos finais:")
        for cadaJogador in jogadores:
            print(f'Game over. Pontos finais:{cadaJogador.nome, cadaJogador.pontos}')
    return 0

if __name__ == '__main__':
    main()
import time

class Jogador:
    # Lista de classe para rastrear as instâncias de jogadores criadas
    jogadores = []

    def __init__(self, nome='', letra=''):
        self.nome = nome
        self.letra = letra
        Jogador.jogadores.append(self)

def criar_tabuleiro():
    # Representação do tabuleiro usando um dicionário com posições de 1 a 9
    tabuleiro = {
        1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
        7: ' ', 8: ' ', 9: ' '
    }
    return tabuleiro

def imprimir_tabuleiro(tabuleiro):
    print(' ' + tabuleiro[1] + ' │ ' + tabuleiro[2] + ' │ ' + tabuleiro[3] + ' ')
    print('───┼───┼───')
    print(' ' + tabuleiro[4] + ' │ ' + tabuleiro[5] + ' │ ' + tabuleiro[6] + ' ')
    print('───┼───┼───')
    print(' ' + tabuleiro[7] + ' │ ' + tabuleiro[8] + ' │ ' + tabuleiro[9] + ' ')
    print('')

def espaco_esta_vazio(tabuleiro, posicao):
    if tabuleiro[posicao] == ' ':
        return True
    else:
        return False

def buscar_obj_computador():
    for jogador in Jogador.jogadores:
        if jogador.name == 'computador':
            return jogador

def buscar_obj_humano():
    for jogador in Jogador.jogadores:
        if jogador.name == 'humano':
            return jogador

def jogar_novamente():
    print('')
    opcao = input('Deseja jogar novamente? Digite "s" para Sim ou qualquer tecla para encerrar: ')
    if opcao == 's' or opcao == 'S':
        print('')
        # Reinicia a lista de jogadores para evitar duplicatas na nova partida
        Jogador.jogadores = []
        principal()
    else:
        exit()

def atraso():
    time.sleep(0.5)

def inserir_letra(tabuleiro, letra, posicao):
    atraso()
    if espaco_esta_vazio(tabuleiro, posicao):
        tabuleiro[posicao] = letra
        print('')
        imprimir_tabuleiro(tabuleiro)

        # Verifica estados de fim de jogo após cada inserção
        if verificar_empate(tabuleiro):
            print('Empate!')
            jogar_novamente()
        elif vitoria(tabuleiro):
            # Identifica quem venceu com base na letra da jogada atual
            if letra == buscar_obj_computador().letra:
                print('O computador ganhou!')
            elif letra == buscar_obj_humano().letra:
                print('Você ganhou!')
            jogar_novamente()
        return

    else:
        print('A posição escolhida está ocupada!')
        atraso()
        posicao = int(input('Escolha uma nova posição: '))
        inserir_letra(tabuleiro, letra, posicao)
        return

def verificar_vitoria_linhas(tabuleiro, letra=None):
    if letra is None:
        if tabuleiro[1] == tabuleiro[2] and tabuleiro[1] == tabuleiro[3] and tabuleiro[1] != ' ':
            return True
        elif tabuleiro[4] == tabuleiro[5] and tabuleiro[4] == tabuleiro[6] and tabuleiro[4] != ' ':
            return True
        elif tabuleiro[7] == tabuleiro[8] and tabuleiro[7] == tabuleiro[9] and tabuleiro[7] != ' ':
            return True
        else:
            return False
    else:
        if tabuleiro[1] == tabuleiro[2] and tabuleiro[1] == tabuleiro[3] and tabuleiro[1] == letra:
            return True
        elif tabuleiro[4] == tabuleiro[5] and tabuleiro[4] == tabuleiro[6] and tabuleiro[4] == letra:
            return True
        elif tabuleiro[7] == tabuleiro[8] and tabuleiro[7] == tabuleiro[9] and tabuleiro[7] == letra:
            return True
        else:
            return False

def verificar_vitoria_colunas(tabuleiro, letra=None):
    if letra is None:
        if tabuleiro[1] == tabuleiro[4] and tabuleiro[1] == tabuleiro[7] and tabuleiro[1] != ' ':
            return True
        elif tabuleiro[2] == tabuleiro[5] and tabuleiro[2] == tabuleiro[8] and tabuleiro[2] != ' ':
            return True
        elif tabuleiro[3] == tabuleiro[6] and tabuleiro[3] == tabuleiro[9] and tabuleiro[3] != ' ':
            return True
        else:
            return False
    else:
        if tabuleiro[1] == tabuleiro[4] and tabuleiro[1] == tabuleiro[7] and tabuleiro[1] == letra:
            return True
        elif tabuleiro[2] == tabuleiro[5] and tabuleiro[2] == tabuleiro[8] and tabuleiro[2] == letra:
            return True
        elif tabuleiro[3] == tabuleiro[6] and tabuleiro[3] == tabuleiro[9] and tabuleiro[3] == letra:
            return True
        else:
            return False

def verificar_vitoria_diagonal(tabuleiro, letra=None):
    if letra is None:
        if tabuleiro[1] == tabuleiro[5] and tabuleiro[1] == tabuleiro[9] and tabuleiro[1] != ' ':
            return True
        elif tabuleiro[7] == tabuleiro[5] and tabuleiro[7] == tabuleiro[3] and tabuleiro[7] != ' ':
            return True
        else:
            return False
    else:
        if tabuleiro[1] == tabuleiro[5] and tabuleiro[1] == tabuleiro[9] and tabuleiro[1] == letra:
            return True
        elif tabuleiro[7] == tabuleiro[5] and tabuleiro[7] == tabuleiro[3] and tabuleiro[7] == letra:
            return True
        else:
            return False

def vitoria(tabuleiro):
    if verificar_vitoria_linhas(tabuleiro):
        return True
    elif verificar_vitoria_colunas(tabuleiro):
        return True
    elif verificar_vitoria_diagonal(tabuleiro):
        return True
    else:
        return False

def jogador_venceu(tabuleiro, letra_jogador):
    if verificar_vitoria_linhas(tabuleiro, letra_jogador):
        return True
    elif verificar_vitoria_colunas(tabuleiro, letra_jogador):
        return True
    elif verificar_vitoria_diagonal(tabuleiro, letra_jogador):
        return True
    else:
        return False

def verificar_empate(tabuleiro):
    for chave in tabuleiro.keys():
        if tabuleiro[chave] == ' ':
            return False
    return True

def movimento_humano(tabuleiro, humano):
    posicao = int(input('Digite a posição para sua jogada "' + humano.letra + '": '))
    inserir_letra(tabuleiro, humano.letra, posicao)
    return

def movimento_computador(tabuleiro, computador):
    # Algoritmo de busca pela melhor jogada inicializando com um score muito baixo
    melhor_pontuacao = -800
    melhor_jogada = 0

    for chave in tabuleiro.keys():
        if tabuleiro[chave] == ' ':
            tabuleiro[chave] = computador.letra
            # Chama o minimax para prever o resultado dessa jogada
            pontuacao = minimax(tabuleiro, 0, False)
            tabuleiro[chave] = ' '
            if pontuacao > melhor_pontuacao:
                melhor_pontuacao = pontuacao
                melhor_jogada = chave
    print('Jogada do computador:', melhor_jogada)
    inserir_letra(tabuleiro, computador.letra, melhor_jogada)
    return

def minimax(tabuleiro, profundidade, eh_maximizando):
    computador = buscar_obj_computador()
    humano = buscar_obj_humano()

    # Casos base para a recursão (vitoria, derrota ou empate)
    if jogador_venceu(tabuleiro, computador.letra):
        return 1
    elif jogador_venceu(tabuleiro, humano.letra):
        return -1
    elif verificar_empate(tabuleiro):
        return 0

    if eh_maximizando:
        melhor_pontuacao = -800
        for chave in tabuleiro.keys():
            if tabuleiro[chave] == ' ':
                tabuleiro[chave] = computador.letra
                pontuacao = minimax(tabuleiro, profundidade + 1, False)
                tabuleiro[chave] = ' '
                if pontuacao > melhor_pontuacao:
                    melhor_pontuacao = pontuacao
        return melhor_pontuacao

    else:
        melhor_pontuacao = 800
        for chave in tabuleiro.keys():
            if tabuleiro[chave] == ' ':
                tabuleiro[chave] = humano.letra
                pontuacao = minimax(tabuleiro, profundidade + 1, True)
                tabuleiro[chave] = ' '
                if pontuacao < melhor_pontuacao:
                    melhor_pontuacao = pontuacao
        return melhor_pontuacao

def definir_primeiro_jogador():
    atraso()
    opcao = int(input('Digite 1 para jogar primeiro, ou 0 para o computador iniciar: '))
    if opcao == 1:
        print('Você é o primeiro a jogar! Boa Sorte!')
        return True
    elif opcao == 0:
        print('O Computador joga primeiro! Boa Sorte!')
        return False
    else:
        print('Digite uma opção válida!')
        return definir_primeiro_jogador()

def criar_jogadores(configuracao):
    humano = Jogador('humano', 'X')
    computador = Jogador('computador', 'O')

    # Se o computador começa, ele assume a letra 'X' por padrão de convenção
    if configuracao == 0:
        humano.letra = 'O'
        computador.letra = 'X'

    return humano, computador

def principal():
    print('##################################################')
    print('#                 Jogo da Velha                  #')
    print('##################################################')
    print('Na sua rodada, digite o número referente a posição')
    print('que você deseja jogar, seguindo o mapa abaixo:')
    print('')
    atraso()
    print(' 1 │ 2 │ 3 ')
    print('───┼───┼───')
    print(' 4 │ 5 │ 6 ')
    print('───┼───┼───')
    print(' 7 │ 8 │ 9 ')
    print('')

    tabuleiro = criar_tabuleiro()
    humano_comeca = definir_primeiro_jogador()
    print('')

    if humano_comeca:
        humano, computador = criar_jogadores(1)
        imprimir_tabuleiro(tabuleiro)
        while not vitoria(tabuleiro):
            atraso()
            movimento_humano(tabuleiro, humano)
            # Verifica se o humano venceu ou empatou antes do computador jogar
            if vitoria(tabuleiro) or verificar_empate(tabuleiro):
                break
            atraso()
            movimento_computador(tabuleiro, computador)

    else:
        humano, computador = criar_jogadores(0)
        while not vitoria(tabuleiro):
            atraso()
            movimento_computador(tabuleiro, computador)
            # Verifica se o computador venceu ou empatou antes do humano jogar
            if vitoria(tabuleiro) or verificar_empate(tabuleiro):
                break
            atraso()
            movimento_humano(tabuleiro, humano)

if __name__ == '__main__':
    principal()
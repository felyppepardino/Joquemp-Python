import random
# Escolha de modalidade
print('1 - humano x humano\n2 - humano x computador\n3 - computador x computador')
modalidade = int(input('Insira a modalidade desejada: '))
jogar = 1
placar1 = 0
placar2 = 0

while jogar == 1:
    # Se a modalidade escolhida for humano x humano
    if modalidade == 1:
        # Entradas de cada jogador entre pedra, papel ou tesoura
        jogador1 = int(input('Jogador 1, escolha entre: 1 - pedra, 2 - papel ou 3 - tesoura: '))
        jogador2 = int(input('Jogador 2, escolha entre: 1 - pedra, 2 - papel ou 3 - tesoura: '))
        # Condições para empate
        if (jogador1 == 1 and jogador2 == 1) or (jogador1 == 2 and jogador2 == 2) or (jogador1 == 3 and jogador2 == 3):
            print('Empate')
            print('Placar: ', placar1,'x', placar2)
        # Partida entre pedra e papel
        elif (jogador1 == 1 and jogador2 == 2) or (jogador1 == 2 and jogador2 == 1):
            if jogador1 == 2:
                print('Papel vence, jogador 1 vencedor')
                placar1 = placar1 + 1
                print('Placar: ', placar1, 'x', placar2)
            elif jogador2 == 2:
                print('Papel vence, jogador 2 vencedor')
                placar2 = placar2 + 1
                print('Placar: ', placar1, 'x', placar2)
        # Partida entre pedra e tesoura
        elif (jogador1 == 1 and jogador2 == 3) or (jogador1 == 3 and jogador2 == 1):
            if jogador1 == 1:
                print('Pedra vence, jogador 1 vencedor')
                placar1 = placar1 + 1
                print('Placar: ', placar1, 'x', placar2)
            elif jogador2 == 1:
                print('Pedra vence, jogador 2 vencedor')
                placar2 = placar2 + 1
                print('Placar: ', placar1, 'x', placar2)
        # Partida entre papel e tesoura
        elif (jogador1 == 2 and jogador2 == 3) or (jogador1 == 3 and jogador2 == 2):
            if jogador1 == 3:
                print('Tesoura vence, jogador 1 vencedor')
                placar1 = placar1 + 1
                print('Placar: ', placar1, 'x', placar2)
            elif jogador2 == 3:
                print('Tesoura vence, jogador 2, vencedor')
                placar2 = placar2 + 1
                print('Placar: ', placar1, 'x', placar2)

    # Se a modalidade escolhida for humano x computador
    if modalidade == 2:
        # Entrada somente do jogador
        jogador = int(input('Escolha entre: 1 - pedra, 2 - papel ou 3 - tesoura: '))
        # Computador escolhe aleatoriamente um valor entre 1 e 3
        computador = random.randint(1,3)
        if (jogador == 1 and  computador == 1) or (jogador == 2 and computador == 2) or (jogador == 3 and computador == 3):
            print('Empate')
            if jogador == 1 and computador == 1:
                print('Pedra x pedra')
            if jogador == 2 and computador == 2:
                print('Papel x papel')
            if jogador == 3 and computador == 3:
                print('Tesoura x tesoura')
            print('Placar: ', placar1, 'x', placar2)
        # Partida entre pedra e papel
        elif (jogador == 1 and computador == 2) or (jogador == 2 and computador == 1):
            if jogador == 2:
                print('Jogador = papel.\nComputador = pedra.\nPapel vence. Jogador vencedor')
                placar1 = placar1 + 1
                print('Placar: ', placar1, 'x', placar2)
            elif computador == 2:
                print('Jogador = pedra.\nComputador = papel.\nPapel vence, computador vencedor')
                placar2 = placar2 + 1
                print('Placar: ', placar1, 'x', placar2)
        # Partida entre pedra e tesoura
        elif (jogador == 1 and computador == 3) or (jogador == 3 and computador == 1):
            if jogador == 1:
                print('Jogador = pedra.\nComputador = tesoura.\nPedra vence, jogador vencedor')
                placar1 = placar1 + 1
                print('Placar: ', placar1, 'x', placar2)
            elif computador == 1:
                print('Jogador = tesoura.\nComputador = pedra.\nPedra vence, computador vencedor')
                placar2 = placar2 + 1
                print('Placar: ', placar1, 'x', placar2)
        # Partida entre papel e tesoura
        elif (jogador == 2 and computador == 3) or (jogador == 3 and computador == 2):
            if jogador == 3:
                print('Jogador = tesoura.\nComputador = papel.\nTesoura vence, jogador vencedor')
                placar1 = placar1 + 1
                print('Placar: ', placar1, 'x', placar2)
            elif computador == 3:
                print('Jogador = papel.\nComputador = tesoura.\nTesoura vence, computador vencedor')
                placar2 = placar2 + 1
                print('Placar: ', placar1, 'x', placar2)

    # Se a modalidade escolhida for computador x computador
    if modalidade == 3:
        # As saídas das variáveis são aleatórias
        computador1 = random.randint(1,3)
        computador2 = random.randint(1,3)
        if computador1 == 1 and computador2 == 1:
            print('pedra x pedra')
        if computador1 == 2 and computador2 == 2:
            print('papel x papel')
        if computador1 == 3 and computador2 == 3:
            print('tesoura x tesoura')
        # Condições de empate
        if (computador1 == 1 and computador2 == 1) or (computador1 == 2 and computador2 == 2) or (computador1 == 3 and computador2 == 3):
            print('Empate')
            print('Placar: ', placar1, 'x', placar2)
        # Partida entre pedra e papel
        elif (computador1 == 1 and computador2 == 2) or (computador1 == 2 and computador2 == 1):
            if computador1 == 2:
                print('Computador 1 = papel.\nComputador 2 = pedra.\nPapel vence, computador 1 vencedor')
                placar1 = placar1 + 1
                print('Placar: ', placar1, 'x', placar2)
            elif computador2 == 2:
                print('Computador 1 = pedra.\nComputador 2 = papel.\nPapel vence, computador 2 vencedor')
                placar2 = placar2 + 1
                print('Placar: ', placar1, 'x', placar2)
        # Partida entre pedra e tesoura
        elif (computador1 == 1 and computador2 == 3) or (computador1 == 3 and computador2 == 1):
            if computador1 == 1:
                print('Computador 1 = pedra.\nComputador 2 = tesoura.\nPedra vence, computador 1 vencedor')
                placar1 = placar1 + 1
                print('Placar: ', placar1, 'x', placar2)
            elif computador2 == 1:
                print('Computador 1 = tesoura.\nComputador 2 = pedra.\nPedra vence, computador 2 vencedor')
                placar2 = placar2 + 1
                print('Placar: ', placar1, 'x', placar2)
        # Partida entre papel e tesoura
        elif (computador1 == 2 and computador2 == 3) or (computador1 == 3 and computador2 == 2):
            if computador1 == 3:
                print('Computador 1 = tesoura.\nComputador 2 = papel.\nTesoura vence, computador 1 vencedor')
                placar1 = placar1 + 1
                print('Placar: ', placar1, 'x', placar2)
            elif computador2 == 3:
                print('Computador 1 = papel.\nComputador 2 = tesoura.\nTesoura vence, computador 2 vencedor')
                placar2 = placar2 + 1
                print('Placar: ', placar1, 'x', placar2)

    jogar = int(input('Insira 1 se deseja jogar mais uma partida ou 0 caso queira encerrar: '))
    # Impede que a entrada seja diferente de 0 e 1
    while jogar != 0 and jogar != 1:
        print('Inserção inválida.')
        jogar = int(input('Insira 1 se deseja jogar mais uma partida ou 0 caso queira encerrar: '))
    # Se a entrada for o valor 0, é mostrado na tela o placar final conforme os resultados das partidas e é encerrado o jogo
    if jogar == 0:
        print('Jogador 1:', placar1, 'X Jogador 2: ', placar2)
        if placar1 > placar2:
            print('O vencedor geral foi o Jogador 1')
        elif placar2 > placar1:
            print('O vencedor geral foi o Jogador 2')
        elif placar1 == placar2:
            print('O placar final ficou empatado.')
        print('\nObrigado por jogar o nosso joquempô. Feito por: Amanda O. B. Santos e Felyppe P. Silva')


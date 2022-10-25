import random

pontos_usuario = 0
pontos_computador = 0


opcao = ['pd', 't', 'p']


while True:
    escolha_usuario = input('Escolha PD(Pedra), T(Tesoura), P(Papel) ou Q para sair:').lower()

    if escolha_usuario == 'q':
        break

    if escolha_usuario not in opcao:
        continue

    escolha_computador = random.randint(0, 2)

    escolha_computador = opcao[escolha_computador]

    print('O computador escolheu ' + escolha_computador)

    if escolha_usuario == escolha_computador:
        print('Empate!')

    elif escolha_usuario == 'pd' and escolha_computador == 't':
        print('Você ganhou!')
        pontos_usuario = pontos_computador + 1

    elif escolha_usuario == 'p' and escolha_computador == 'pd':
        print('Você ganhou!')
        pontos_usuario = pontos_computador + 1

    elif escolha_usuario == 't' and escolha_computador == 'p':
        print('Você ganhou!')
        pontos_usuario = pontos_computador + 1

    else:
        print('Você perdeu!')
        pontos_computador = pontos_computador + 1

print('Sua pontuação: ' + str(pontos_usuario))
print('Pontuação do Computador: ' + str(pontos_computador))

if pontos_computador > pontos_usuario:
    print('Derrota!!')
elif pontos_computador == pontos_usuario:
    print('Empate!!')
else:
    print('Vitória!!')

print('********************************************************')
print('*********        JOGO DA ADVINHAÇÃO      ***************')
print('********************************************************')
print('')
print('Bem Vindo(a): Neste jogo, você irá tentar acertar um número que está entre 0 a 100!!')
print('')

#Escolha de um numero feito de maneira aleatória pelo sistema
from random import choice

vocabulario = range(100)

numero_secreto = choice(vocabulario)


print('Escolha um NÍVEL para jogar:')
print(' *   nivel 1 = 20 tentativas')
print(' *   nivel 2 = 10 tentativas')
print(' *   nivel 3 =  5 tentativas')
print('')

nivel= int(input('Nivel escolhido:'))
print('')

rodada = 1

total_de_tentativas1 = 20
total_de_tentativas2 = 10
total_de_tentativas3 = 5



if (nivel==1):
    print('Você irá jogar no nivel', nivel, 'e terá direito a', total_de_tentativas1, 'tentativas.')
    print('')
    print('Vamos lá, Boa Sorte!!')
    print('')

if (nivel==2):
    print('Você irá jogar no nivel', nivel, 'e terá direito a', total_de_tentativas2, 'tentativas.')
    print('')
    print('Vamos lá, Boa Sorte!!')
    print('')

if (nivel==3):
    print('Você irá jogar no nivel', nivel, 'e terá direito a', total_de_tentativas3, 'tentativas.')
    print('')
    print('Vamos lá, Boa Sorte!!')
    print('')

if (nivel>=4):
    print('Desculpe, escolha somente os níveis 1,2 ou 3..')
    print('')



if nivel==1:
  for rodada in range (1, total_de_tentativas1 + 1):
    print('Tentativa',rodada,'de',total_de_tentativas1,'.')

    chute=int(input('Tente acertar o numero secreto, lembrando que ele está entre 0 a 100: '))
    print('')
    print('____________________________________________________________________________')
    print('Você digitou:', chute)

    acertou= chute == numero_secreto
    maior= chute>numero_secreto
    menor= chute<numero_secreto

    if(acertou):
       print('')
       print('                  Parabéns, vc acertou!!!')
       print('')
       print('"A melhor vista vem depois de escalar a montanha mais alta!!"')
       print('')
       break

    elif(maior):
       print('Seu chute foi MAIOR do que o esperado..tente novamente!')
       print('')

    elif(menor):
       print('Seu chute foi MENOR do que o esperado..tente novamente!')
       print('')

    rodada = rodada + 1

if nivel==2:
  for rodada in range (1, total_de_tentativas2 + 1):
    print('Tentativa',rodada,'de',total_de_tentativas2,'.')

    chute=int(input('Tente acertar o numero secreto, lembrando que ele está entre 0 a 100: '))
    print('')
    print('____________________________________________________________________________')
    print('Você digitou:', chute)

    acertou= chute == numero_secreto
    maior= chute>numero_secreto
    menor= chute<numero_secreto

    if(acertou):
       print('')
       print('                  Parabéns, vc acertou!!!')
       print('')
       print('"Nas grandes batalhas da vida, o primeiro passo para a vitória é o desejo de vencer!"')
       print('')
       break

    elif(maior):
       print('Seu chute foi MAIOR do que o esperado..tente novamente!')
       print('')

    elif(menor):
       print('Seu chute foi MENOR do que o esperado..tente novamente!')
       print('')


    rodada = rodada + 1


if nivel==3:
  for rodada in range (1, total_de_tentativas3 + 1):
    print('Tentativa',rodada,'de',total_de_tentativas3,'.')

    chute=int(input('Tente acertar o numero secreto, lembrando que ele está entre 0 a 100: '))
    print('')
    print('____________________________________________________________________________')
    print('Você digitou:', chute)

    acertou= chute == numero_secreto
    maior= chute>numero_secreto
    menor= chute<numero_secreto

    if(acertou):
       print('')
       print('                  Parabéns, vc acertou!!!')
       print('')
       print('"A vitória está sempre ao redor daqueles que não param de lutar!"')
       print('')
       break

    elif(maior):
       print('Seu chute foi MAIOR do que o esperado..tente novamente!')
       print('')

    elif(menor):
       print('Seu chute foi MENOR do que o esperado..tente novamente!')
       print('')


    rodada = rodada + 1



if(nivel==1):
    if(rodada>total_de_tentativas1):
      print('')
      print('"Desculpe, você não acertou, mais sorte da próxima vez.."')
if(nivel==2):
    if(rodada>total_de_tentativas2):
      print('')
      print('"Desculpe, você não acertou, mais sorte da próxima vez.."')
if(nivel==3):
    if(rodada>total_de_tentativas3):
      print('')
      print('"Desculpe, você não acertou, mais sorte da próxima vez.."')


print('')
print('                        FIM DE JOGO')
print('')


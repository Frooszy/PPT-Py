#Importa as Bibliotecas que são útilizadas no Código.

import time
import random
import os

def Inciar(): #Crio a função Iniciar, que é basicamente um Print de "Bem Vindo", e chamo ela mais em breve na Main.
    os.system('cls') #Dá um "Clear" no console.
    print('------------------------------------')
    print('-        Bem vindo Ao PPT!         -')
    print('------------------------------------')
    print()

    
def Escolhas(Escolha_User, Escolha_Bot): #Função "Escolhas", que também é chamada em breve na Main, ela que define o Empate e etc. Ela vem seguida dos Parâmetros que prescisam estar ali, se não ele não "Pega" esses parâmetros que foram definidos na Main e traz para cá.
    if Escolha_User == Escolha_Bot: #Basicamente, Se a escolha do User, for igual a do Bot, ele printa Impate, e segue assim para a vitória e derrota.
        time.sleep(1)
        print('Houve um Empate.')

    elif((Escolha_User == 'Papel' and Escolha_Bot == 'Pedra') or (Escolha_User == 'Pedra' and Escolha_Bot == 'Tesoura') or (Escolha_User == 'Tesoura' and Escolha_Bot == 'Papel')):
        time.sleep(1)
        print('Parabéns, Você ganhou!') 

    elif((Escolha_Bot == 'Papel' and Escolha_User == 'Pedra') or (Escolha_Bot == 'Pedra' and Escolha_User == 'Tesoura') or (Escolha_Bot == 'Tesoura' and Escolha_User == 'Papel')):
        time.sleep(1)
        print('Infelizmente Você Perdeu.')


def Main(): #Defino a Função "Main", que é como se fosse o "Sistema" por traz.
    Inciar() #Puxo o inicio

    time.sleep(2)
    nome = input('Digite seu Nome: ') #Input para definir o Nome do Jogdor.
    print()

    if nome == '': #Se o nome for um Espaço/Enter, ele finaliza.
        print('Nome Inválido, Jogo finalizado.')
        time.sleep(1)
        os.system('cls')
        return  

    while True:  #Loop Do jogo.
        time.sleep(1)

        Escolha_User = input(f'{nome}, Escolha Uma Opção (Pedra, Papel, Tesoura): ') #Sistema que define a escolha do Jogador.
        Escolha_Bot = random.choice(['Pedra', 'Papel', 'Tesoura']) #Sistema que randomiza a escolha do bot.

        if Escolha_User == '': #Se for um Enter, ele finaliza.
            os.system('cls')
            print('Escolha inválida, jogo finalizado.')
            break

        elif Escolha_User != 'Pedra' and Escolha_User != 'Papel' and Escolha_User != 'Tesoura':#Se não for nenhuma das escolhas, ele finaliza.
            os.system('cls')
            print('Escolha inválida, jogo finalizado.')
            break

        else: #Caso esteja tudo certo, ele roda a Função que defina se ele ganhou/perdeu/empatou, limpa o sistema, e o jogo começa novamente.
            Escolhas(Escolha_User, Escolha_Bot)
            time.sleep(2)
            os.system('cls')

Main() #Chamo a Função Main, logo quando inicia-se o Código.

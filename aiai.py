import random
num_sorteado = random.randint(0, 9)
#definindo funcoes, se ouver ganhador ou perdedor elas retornam True fazendo o while parar de se repetir.
def tem_ganhador(a, b, c, d, e, f, g, h, i):
    return a == b == c or \
           d == e == f or \
           g == h == i or \
           a == d == g or \
           b == e == h or \
           c == f == i or \
           a == e == i or \
           c == e == g

def deu_velha(a, b, c, d, e, f, g, h, i):
    return a != '1' and b != '2' and c != '3' and \
           d != '4' and e != '5' and f != '6' and\
           g != '7' and h != '8' and i != '9'

#variavel para ajudar no menu, se o participante vai ou n continuar jogando.
jogando= True

#estrutura de repeticao, emquanto jogando for verdade ele se repete, printando o tabuleiro, deixando mais organizado e certo
while jogando == True:
    print("Digite o nome dos jogadores")
    jog1 = input("- ")
    jog2 = input("- ")
    a = '1'
    b = '2'
    c = '3'
    d = '4'
    e = '5'
    f = '6' 
    g = '7'
    h = '8'
    i = '9'
    separa = '|'
    separa2 = '-+-+-'
    linhaum = a + separa + b + separa + c
    linha2 = d + separa + e + separa + f 
    linha3 = g + separa + h + separa +  i 
    tabuleiro = linhaum + '\n'+ separa2 +'\n'+ linha2 + '\n' + separa2 +'\n'+linha3
    print (tabuleiro)
    jogadas = num_sorteado
    vazia = ''# recebe x ou bolinha dependendo de quem esta jogando 
    while not tem_ganhador(a, b, c, d, e, f, g, h, i) and not deu_velha(a, b, c, d, e, f, g, h, i):
        # para decidir quem eh o ou x
        if (jogadas % 2) != 0 :
            vazia = 'x'
            print(jog1, "digite o lugar que deseja jogar" )
            jogada = input(': ')
        else:
            vazia = 'O'
            print(jog2, "digite o lugar que deseja jogar" )
            jogada=input(': ')
        # para conferir se a casa onde vao jogar ja nao esta ocupada, e entao pedir para jogar novamente ou substituir o numero da casa pelo simbolo que aquele
        #jogador recebe(o ou x)
        if jogada == '1' and a == '1':
            a = vazia
            jogadas = jogadas +1 #se o numero sorteado for par, vai acrecentar um e virar impar, assim trocando de jogador na proxima rodada.
        elif jogada == '2' and b == '2':
            b = vazia
            jogadas = jogadas +1
        elif jogada == '3' and c == '3':
            c = vazia
            jogadas = jogadas +1
        elif jogada == '4' and d == '4':
            d = vazia
            jogadas = jogadas +1
        elif jogada == '5' and e == '5':
            e = vazia
            jogadas = jogadas +1
        elif jogada == '6' and f == '6':
            f = vazia
            jogadas = jogadas +1
        elif jogada == '7' and g == '7':
            g = vazia
            jogadas = jogadas +1
        elif jogada == '8' and h == '8':
            h = vazia
            jogadas = jogadas +1
        elif jogada == '9' and i == '9':
            i = vazia
            jogadas = jogadas +1
        else:
            print("sua jogada foi invalidada, jogue novamente...")
        linhaum = a + separa + b + separa + c
        linha2 = d + separa + e + separa + f 
        linha3 = g + separa + h + separa +  i 
        tabuleiro = linhaum + '\n'+ linha2 +'\n'+linha3
        print (tabuleiro)
    #confere se tem que continuar jogando, se ja tem um ganhador ou se deu velha
    if tem_ganhador(a, b, c, d, e, f, g, h, i):
        if vazia == 'x':
            print("o jogador ",  jog1, "ganhou!!!")
            jogando = False
        else:
            print ("o jogador", jog2, "ganhou!!!")
            jogando = False
    else:
        print ("deu velha!!!")
        jogando = False

    #menu, jogar novamente ou nao 
    res = str(input("deseja continuar jogando? y ou n "))

    if res == 'y' or res == 'Y':
        jogando = True
    elif res == 'n' or res == 'N':
        jogando = False

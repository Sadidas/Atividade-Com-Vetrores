"""
a) Menu: chamada no início do programa e ao final de cada operação;
b) Digitação dos 10 números inteiros no vetor;
c) Impressão do valor do somatório dos números do vetor;
d) Impressão da média dos números do vetor;
e) Substituir todos os números negativos por zero;
f) Substituir todos os números repetidos por zero;
g) Proponha uma nova função utilizando o vetor. Seja criativo(a)!
"""

import random
import time
Deus = True


def tela_incial(primeira: bool):
    if primeira:
        print('       <#============================================#>')
        print('       |/                Bem-Vindo a                 \|')
        print('       ||              Tarefa de Vetores             ||')
        print('       ||              Para o Professor              ||')
        print('       |\                <3 Andery <3                /|')
        print('       <#============================================#>')
        primeira = False
    print(f'\nEscolhas:')
    print('1 -> Digitar o vetor                  4 -> Substituir os números negativos por zero')
    print('2 -> Somar os valores do vetor        5 -> Substituir os números repetidos por zero')
    print('3 -> Encontrar a media do vetor       6 -> Função especial ;)')
    escolha = input()
    return escolha, primeira


def verificacao_int(talvez_int: str) -> bool:
    try:
        int(talvez_int)
        return True
    except ValueError:
        return False


def digitar_vetor(vetor: list) -> list:
    i = 0
    while i < 10:
        digitacao = input(f'Digite um valor numérico para ser adicionado ao vetor\n')
        if verificacao_int(digitacao):
            print(f'-> Valor {digitacao} adicionado ao vetor!')
            vetor.append(int(digitacao))
            print(f'-> Estado do vetor: {vetor}')
            i += 1
        else:
            print(f'{digitacao} Inválido!')
        print('===============================================')
    return vetor


def vetor_aleatorio(vetor: list) -> list:
    for i in range(10):
        aleatorio = random.randint(-100, 100)
        vetor.append(aleatorio)
    print()
    print(f'|====\ Os números que foram gerados são: {vetor} /====|')
    return vetor


def case1(vetor: list) -> list:
    vetor.clear()
    while True:
        print()
        print('<#==============================#>')
        print('|/       Como Você Deseja       \|')
        print('|\      Inserir os valores?     /|')
        print('<#==============================#>')
        print(f'\nEscolhas:')
        print('1 -> Digite os Números Manualmente')
        escolha_case1 = input(f'2 -> Escolhar os Digitos Aleatoriamente\n')

        if escolha_case1.strip(' ') == '1':
            vetor = digitar_vetor(vetor)
            break
        elif escolha_case1.strip(' ') == '2':
            vetor = vetor_aleatorio(vetor)
            break
        print('|====\ Digite um valor válido! /====|')
    return vetor


def somatorio(vetor: list) -> int:
    if vetor:
        soma = 0
        for digitos in vetor:
            soma += digitos
        return soma
    else:
        print('|====\ Digite os valores primeiro! /====|')


def encontra_media(vetor: list):
    if vetor:
        media = somatorio(vetor) / 10
        print(f'|====\ A media do vetor é igual a: {media} /====|')
    else:
        print('|====\ Digite os valores primeiro! /====|')


def substituir_negativos(vetor: list) -> list:
    if vetor:
        for digitos in range(len(vetor)):
            if vetor[digitos] < 0:
                vetor[digitos] = 0
        print(f'|====\ Depois de substituir os números negativos por 0 o vetor ficou assim: {vetor} /====|')
        return vetor
    else:
        print('|====\ Digite os valores primeiro! /====|')


def substituir_repetidos(vetor: list) -> list:
    if vetor:
        set_vetor = set()
        for digitos in range(len(vetor)):
            if vetor[digitos] in set_vetor:
                vetor[digitos] = 0
            else:
                set_vetor.add(vetor[digitos])
        print(f'|====\ Depois de substituir os números repetidos por 0 o vetor ficou assim: {vetor} /====|')
        return vetor
    else:
        print('|====\ Digite os valores primeiro! /====|')


def inverter_valores(vetor: list) -> list:
    valor_invertido = []
    for algarismos in range(len(vetor)):
        if vetor[algarismos] >= 0:
            string_alg = str(vetor[algarismos])
            string_alg = string_alg[::-1]
            int_alg = int(string_alg)
        else:
            string_alg = str(vetor[algarismos] * -1)
            string_alg.strip('-')
            string_alg = string_alg[::-1]
            int_alg = int(string_alg)
            int_alg *= -1
        valor_invertido.append(int_alg)
    return valor_invertido


def inverter_vetor(vetor: list) -> list:
    if vetor:
        j = len(vetor) - 1
        for i in range(int(len(vetor)/2)):
            vetor[i], vetor[j] = vetor[j], vetor[i]
            j -= 1
        vetor = inverter_valores(vetor)
        barra_carregar()
        print(f'|====\ O vetor e seus valores foram invertidos! {vetor} /====|')
        return vetor
    else:
        print('|====\ Digite os valores primeiro! /====|')


def barra_carregar():
    print('Computando...')
    time.sleep(2)
    print('[     ] Calculando a velocidade da luz...')
    time.sleep(2)
    print('[|    ] Perguntado para o chatGPT...')
    time.sleep(2)
    print('[||   ] Lendo sua mente...')
    time.sleep(2)
    print('[|||  ] Escrevendo uma carta para minha amada...')
    time.sleep(2)
    print('[|||| ] Ponderando sobre a vida...')
    time.sleep(2)
    print('[|||||] Tentando lembrar o que era para fazer...')
    time.sleep(2)
    print('Computado!')


primeira_vez = True
vetor_total = []
while Deus:
    escolha_inicial, primeira_vez = tela_incial(primeira_vez)
    match escolha_inicial.strip(' '):
        case '1':
            case1(vetor_total)
        case '2':
            soma_total = somatorio(vetor_total)
            print(f'|====\ O valor de todos os digitos do vetor somados é igual a: {soma_total} /====|')
        case '3':
            encontra_media(vetor_total)
        case '4':
            substituir_negativos(vetor_total)
        case '5':
            substituir_repetidos(vetor_total)
        case '6':
            inverter_vetor(vetor_total)
        case _:
            print('|====\ Digite um valor válido! /====|')

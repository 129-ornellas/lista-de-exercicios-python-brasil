"""
Exercício 42 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes
intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.

    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[-1, 10, 15, 20, 50, 13, 78, 22, 14, 16]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    7 número(s) entre o intervalo de zero a 25
    1 número(s) entre o intervalo de 26 a 50
    1 número(s) entre o intervalo de 76 a 100
    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[14, -5, 10, 2, 80, 99]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    2 número(s) entre o intervalo de zero a 25
    2 número(s) entre o intervalo de 76 a 100
    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[-55, 144, 5, 32, 18, 43, 12, 26, 76]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    3 número(s) entre o intervalo de zero a 25
    3 número(s) entre o intervalo de 26 a 50
    1 número(s) entre o intervalo de 76 a 100
    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[3, 5, 100, -5, 70, 88, 28, 12]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    1 número(s) entre o intervalo de zero a 25
    1 número(s) entre o intervalo de 26 a 50
    1 número(s) entre o intervalo de 51 a 75
    1 número(s) entre o intervalo de 76 a 100

"""


def listar_numeros_para_avaliacao():
    """Escreva aqui em baixo a sua solução"""
    
    lista_0_25 = []
    lista_26_50 = []
    lista_51_75 = []
    lista_76_100 = []


    
    while True:
        numeros = int(input('digite os numeros: '))
        
        if numeros > 0 and numeros < 26:
            lista_0_25.append(numeros)
        
        elif numeros > 25 and numeros < 51:
            lista_26_50.append(numeros)
        
        elif numeros > 50 and numeros < 76:
            lista_51_75.append(numeros)
        
        elif numeros > 75 and numeros < 101:
            lista_76_100.append(numeros)
        
        else:
            break
        
    if len(lista_0_25) > 0:
        print(f'{len(lista_0_25)} número(s) entre o intervalo de zero a 25')
    if len(lista_26_50) > 0:
        print(f'{len(lista_26_50)} número(s) entre o intervalo de 26 a 50')
    if len(lista_51_75)> 0:
        print(f'{len(lista_51_75)} número(s) entre o intervalo de 51 a 75')
    if len(lista_76_100)> 0:
        print(f'{len(lista_76_100)} número(s) entre o intervalo de 76 a 100')
    
        


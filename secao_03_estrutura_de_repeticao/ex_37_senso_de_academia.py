"""
Exercício 37 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais 
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu nome, sua altura e 
seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo nome. Ao encerrar o programa 
também deve ser informados os nomes e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além
da média das alturas e dos pesos dos clientes
 
    >>> from secao_03_estrutura_de_repeticao import ex_37_senso_de_academia
    >>> entradas = ['0', '81', '162', 'Renzo']  # Um aluno apenas
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Renzo, com 162 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Renzo, com 81 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 162.0 centímetros
    Media de peso dos clientes: 81.0 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 177.0 centímetros
    Media de peso dos clientes: 80.5 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.7 centímetros
    Media de peso dos clientes: 103.7 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota', '50', '172', 'Seco']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Seco, com 50 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.0 centímetros
    Media de peso dos clientes: 90.2 kilos

"""


from statistics import mean

def rodar_senso():
    """Escreva aqui em baixo a sua solução"""
    def printar(nomes_clientes, cliente_alto, cliente_baixo, cliente_magro, cliente_gordo):
        print(f'Cliente mais alto: {nomes_clientes[0]}, com {cliente_alto} centímetros')
        print(f'Cliente mais baixo: {nomes_clientes[1]}, com {cliente_baixo} centímetros')
        print(f'Cliente mais magro: {nomes_clientes[2]}, com {cliente_magro} kilos')
        print(f'Cliente mais gordo: {nomes_clientes[3]}, com {cliente_gordo} kilos')

    def medias(media_altura, media_peso):
        print('--------------------------------------------------')
        print(f'Media de altura dos clientes: {media_altura:.1f} centímetros')
        print(f'Media de peso dos clientes: {media_peso:.1f} kilos')

    lista_de_nomes = []
    lista_de_alturas = []
    lista_de_pesos = []
    
    nome = str(input('digite nome: '))
    while nome != '0':
        lista_de_nomes.append(nome)
        altura = int(input('digite altura: '))
        lista_de_alturas.append(altura)
        peso = int(input('digite peso: '))
        lista_de_pesos.append(peso)
        nome = str(input('digite nome: '))

    # variaveis de maior e menor
    maior_altura = max(lista_de_alturas)
    menor_altura = min(lista_de_alturas)
    magro = min(lista_de_pesos)
    gordo = max(lista_de_pesos)
    
    diferenciados = []
    diferenciados.append(lista_de_nomes[lista_de_alturas.index(max(lista_de_alturas))])
    diferenciados.append(lista_de_nomes[lista_de_alturas.index(menor_altura)])
    diferenciados.append(lista_de_nomes[lista_de_pesos.index(magro)])
    diferenciados.append(lista_de_nomes[lista_de_pesos.index(gordo)])

    media_de_alturas = mean(lista_de_alturas)
    media_de_pesos = mean(lista_de_pesos)

    printar(diferenciados, maior_altura, menor_altura, magro, gordo)
    medias(media_de_alturas, media_de_pesos)

from random import randint

# Receber informação se o usuario quer ou não jogar
# caso seja positiva a resposta jogar dado da escolha de lados que ele quiser
# caso seja negativa fechar programa

positivas = ['sim', 's', 'quero', 'vamos', 'bora', 'pode ser']

negativas = ['não', 'n', 'quero não', 'nao quero', 'nao']


a = ''

while a != 'sair':
    info = input('Você quer jogar dados??')


    try:
        a = positivas.index(info)

        if a != ValueError:
            dado = int(input('Dado de quantos lados você quer jogar?\n por favor digite apenas numeros - '))
            print('O seu dado deu {}'.format(randint(1, dado)))


    except ValueError:
        try:
            negativas.index(info)
            print('tchauzim, precisando tamo ai!')
            a = 'sair'

        except ValueError:
            print('Desculpe não entendi sua resposta por favor tente uma dessas:\n')

            print('Se voce digitou um numero escrito por favor tente utlizar numerais')
            print('EX: em vez de escrever um, escreva: 1\n')
            print('Caso você queira:')
            for item in positivas:
                print(item)

            print('\n')

            print('se sua resposta negativa tente alguma dessas:')

            for item in negativas:
                print(item)
            print('\n')

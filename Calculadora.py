from math import sqrt, factorial

print('*' * 15, 'Python Calculadora', '*' * 15)
print()
print('Selecione o número da operação desejada:')
while True:
    print('''
    1 - ADIÇÃO
    2 - SUBTRAÇÃO
    3 - MULTIPLICAÇÃO
    4 - DIVISÃO
    5 - RAÍZ QUADRADA
    6 - FACTORIAL''')
    print()
    opcao = int(input('Digite sua opção (1/2/3/4/5/6): '))
    print()
    if opcao == 1:
        op1 = int(input('Digite o primeiro número: '))
        op2 = int(input('Digite o segundo número: '))
        print(f'{op1} + {op2} = {op1 + op2}')
        continuar = ''
        while continuar != 'S' and continuar != 'N':
            continuar = str(input('Deseja continuar? [S/N]')).upper()[0]
        if continuar == 'N':
            break

    elif opcao == 2:
        op1 = int(input('Digite o primeiro número: '))
        op2 = int(input('Digite o segundo número: '))
        print(f'{op1} - {op2} = {op1 - op2}')
        continuar = ''
        while continuar != 'S' and continuar != 'N':
            continuar = str(input('Deseja continuar? [S/N]')).upper()[0]
        if continuar == 'N':
            break

    elif opcao == 3:
        op1 = int(input('Digite o primeiro número: '))
        op2 = int(input('Digite o segundo número: '))
        print(f'{op1} * {op2} = {op1 * op2}')
        continuar = ''
        while continuar != 'S' and continuar != 'N':
            continuar = str(input('Deseja continuar? [S/N]')).upper()[0]
        if continuar == 'N':
            break

    elif opcao == 4:
        op1 = int(input('Digite o primeiro número: '))
        op2 = int(input('Digite o segundo número:'))
        print(f'{op1} / {op2} = {op1 / op2}')
        continuar = ''
        while continuar != 'S' and continuar != 'N':
            continuar = str(input('Deseja continuar? [S/N]')).upper()[0]
        if continuar == 'N':
            break

    elif opcao == 5:
        op1 = int(input('Por favor, digite o número que deseja saber a raiz²: '))
        print(f'A raíz quadrada de {op1} é {sqrt(op1)}')
        continuar = ''
        while continuar != 'S' and continuar != 'N':
            continuar = str(input('Deseja continuar? [S/N]')).upper()[0]
        if continuar == 'N':
            break

    elif opcao == 6:
        op1 = int(input('Porfavor, digite o número para saber o seu factorial: '))
        print(f'O factorial de {op1} é {factorial(op1)}')
        continuar = ''
        while continuar != 'S' and continuar != 'N':
            continuar = str(input('Deseja continuar? [S/N]')).upper()[0]
        if continuar == 'N':
            break

    elif opcao != 1 and opcao != 2 and opcao != 3 and opcao !=4:
        print('Opção inválida, tente novamente.')
    print('-='*20)
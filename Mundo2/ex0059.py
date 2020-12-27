n1 = float(input('Digite o Primeiro Valor: '))
n2 = float(input('Digite o Segundo Valor: '))
op = 0
while not op == 5:
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos numeros')
    print('[5] Sair do Programa')
    op = int(input('Qual é a sua Opção: '))
    if op == 1:
        print('A soma entre os numeros {} e {} é {}'.format(n1,n2,(n1+n2)))
    elif op == 2:
        print('A multiplicação dos numeros {} e {} é {}'.format(n1,n2,(n1*n2)))
    elif op == 3:
        if n1 > n2:
            print(' O numero {} é maior que o numero {}'.format(n1,n2))
        elif n2 > n1:
            print(' O numero {} é maior que o numero {}'.format(n2, n1))
        elif n1 == n2:
            print('Os numeros são iguais')
    elif op == 4:
        print('informe os numeros novamente')
        n1 = float(input('Digite o Primeiro Valor: '))
        n2 = float(input('Digite o Segundo Valor: '))
    elif op < 1 or op > 5:
        print('Opção invalida, escolha novamente.')
print('Finalizando o Programa....')
print('Obrigada e volte sempre!')
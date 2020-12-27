n = int(input('Digite um numero inteiro: '))
print('[  1  ] Converter para BINÁRIO')
print('[  2  ] Converter para OCTAL')
print('[  3  ] Converter para HEXADECIMAL')
b = int(input('Escolha uma das Bases para conversão:'))

if b == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n, bin(n)))
elif b == 2:
    print('{} convertido para BINÁRIO é igual a {}'.format(n, oct(n)))
elif b == 3:
    print('{} convertido para BINÁRIO é igual a {}'.format(n, hex(n)))
else:
    print('Opção inválida, tente novamente.')

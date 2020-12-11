s = 0
cont = 0
n = 0
q = 'S'
maior = 0
menor = 0
while q == 'S':
    n = int(input('Digite um numero: '))
    if cont == 0:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    s += n
    cont += 1
    q = str(input('Deseja Continuar? [S/N] ')).upper().strip()[0]
print('Você digitou {} numeros e a média foi {}'.format(cont,(s/cont)))
print('O maior valor foi {} e o menor valor foi {}'.format(maior,menor))


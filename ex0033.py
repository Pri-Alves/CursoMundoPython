a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor: '))
menor = a
if b<a and b<c:
    menor = b
if c<b and c<a:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O Menor valor digitado foi {}'.format(menor))
print('O Maior valor digitado foi {}'.format(maior))

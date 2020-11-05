print('Analisador de Triangulos')
a = float(input('Primeiro Segmento: '))
b = float(input('Segundo Segmento: '))
c = float(input('Terceiro Segmento: '))
if (b - c) < a and a < (b+a) and (a - c) < b and b < (a + c) and (a - b) < c and c < (a + b):
    print('Os segmentos acima podem formar um Triangulo!')
else:
    print('Os seguimentos acima nao podem formar um triangulo!')
print('Analisador de Triangulos')
a = float(input('Primeiro Segmento: '))
b = float(input('Segundo Segmento: '))
c = float(input('Terceiro Segmento: '))
if (b - c) < a and a < (b+a) and (a - c) < b and b < (a + c) and (a - b) < c and c < (a + b):
    if a == b and a == c:
        print('Os segmentos acima podem formar um Triangulo EQUILÁTERO!')
    elif a==b and a != c or a==c and a != b or b == c and b != a:
        print('Os segmentos acima podem formar um Triangulo ISÓSCELES!')
    elif a != b and a != c and b != c:
        print('Os segmentos acima podem formar um Triangulo ESCALENO!')
else:
    print('Os seguimentos acima nao podem formar um triangulo !')
from math import pow, sqrt
co = float(input('Comprimento cateto oposto: '))
ca = float(input('Comprimento cateto adjacente: '))
print('A hipotenusa vai medir {}'.format(sqrt(pow(co,2)+pow(ca,2))))
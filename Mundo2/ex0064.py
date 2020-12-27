n = 0
s = 0
cont = 0
while not n == 999:
    n = int(input('Digite uma numero [999 para parar] : '))
    if n != 999:
        s += n
        cont += 1
print('voce digitou {} numero e a soma é {}'.format(cont,s))
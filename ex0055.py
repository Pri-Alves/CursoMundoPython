maiorpeso=0
menorpeso=0
for q in range (1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(q)))
    if q == 1:
        maiorpeso = peso
        menorpeso = peso
    if peso > maiorpeso:
        maiorpeso = peso
    elif peso < menorpeso:
        menorpeso = peso
print('O menor peso digitado foi {}'.format(menorpeso))
print('O maior peso digitado foi {}'.format(maiorpeso))
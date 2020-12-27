n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
m = (n1+n2)/2
print('Para as notas de {} e {} sua média é de {}'.format(n1,n2,m))
if m >= 7:
    print('Você esta Aprovado!')
elif m >= 5 and m < 7:
    print('Você esta em Recuperação!')
elif m < 5:
    print('Você esta Reprovado!')
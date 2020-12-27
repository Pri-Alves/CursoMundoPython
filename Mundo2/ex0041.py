from datetime import date
nasc = int(input('Ano de Nascimento: '))
anoatual = date.today().year
idade = anoatual - nasc
print('O atleta tem {} anos'.format(idade))
if idade > 25:
    print('Classificação: MASTER')
elif idade > 19 and idade <= 25:
    print('Classificação: SÊNIOR')
elif idade > 14 and idade <= 19:
    print('Classificação: JUNIOR')
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 9:
    print('Classificação: MIRIM')
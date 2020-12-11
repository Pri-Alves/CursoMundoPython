from datetime import date
contmaior = 0
contmenor = 0
anoatual = date.today().year
for n in range(1,8):
    ano = int(input('Em que ano a {}ª pessoa nasceu: '.format(n)))
    if (anoatual-ano) >= 18:
        contmaior += 1
    else:
        contmenor +=1
print('Ao todo tivemos {} pessoas na maiores de idade'.format(contmaior))
print('E tambem tivemos {} pessoas menores de idade'.format(contmenor))
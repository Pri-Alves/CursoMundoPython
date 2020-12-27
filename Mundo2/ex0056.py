soma = 0
homemnome = ''
homemvelho = 0
mulheresmenos20 = 0

for q in range(1,5):
    print('======{} Pessoa======'.format(q))
    n = str(input('Nome: '))
    i = int(input('Idade: '))
    s = str(input('Sexo [F/M]: '))
    soma += i
    if s == 'm':
        if homemvelho < i:
            homemvelho = i
            homemnome = n
    if s == 'f':
        if i < 20:
            mulheresmenos20 += 1
print('A média de idade do Grupo é de {}'.format(soma/4))
print('O homem mais velho tem {} e se chama {}'.format(homemvelho,homemnome))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(mulheresmenos20))


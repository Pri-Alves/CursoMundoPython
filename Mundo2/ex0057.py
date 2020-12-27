s = str(input('Digite seu sexo [F/M]: ')).upper()
while s !='F' and s !='M':
    s = str(input('Dados invalidos! por favor digite seu sexo: '))
print('sexo {} registrado com sucesso!'.format(s))
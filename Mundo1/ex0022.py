nome = str(input('Digite o seu nome: '))
print('Analisando o seu nome...')
print('Seu nome em maiusculas é: {}'.format(nome.upper()))
print('Seu nome em minusculas é: {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(''.join(nome.split()))))
print('Seu primeiro nome é {} e tem {} letras'.format((nome.split()[0]),(len(nome.split()[0]))))
s = float(input('Qual é o salario do funcionario? R$'))
if s <= 1250.00:
    print('Quem ganhava R${:.2f}, passa a ganhar R${:.2f}'.format(s,s*1.15))
else:
    print('Quem ganhava R${:.2f}, passa a ganhar R${:.2f}'.format(s,s*1.10))
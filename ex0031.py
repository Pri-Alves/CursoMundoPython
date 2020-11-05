d = float(input('Qual é a distancia da sua viagem: '))
if d <= 200:
    print('Você esta prestes a começar uma viagem de {}Km'.format(d))
    print('O preço da sua passagem é R$ {:.2f}'.format(d*0.5))
else:
    print('Você esta prestes a começar uma viagem de {}Km'.format(d))
    print('O preço da sua passagem é R$ {:.2f}'.format(d*0.45))
v = float(input('Qual é a velocidade atual do carro? '))
if v > 80:
    multa = (v-80)*7
    print('Multado! você excedeu o limite de velocidade de 80KM/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com Segurança')
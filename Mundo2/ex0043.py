p = float(input('Digite seu peso (kg): '))
a = float(input('Digite sua altura (M): '))
imc = p / (a * a)
print('O IMC dessa pessoa é de {:.2f}'.format(imc))
if imc > 40:
    print('Você esta acima do seu peso ideal e com Obesidade Mórbida')
elif imc > 30 and imc <=40:
    print('Você esta acima do seu peso ideal e com Obesidade')
elif imc > 25 and imc <= 30:
    print('Você esta sobrepeso!')
elif imc >=18.5 and imc <= 25:
    print('Parabéns, voce esta no seu peso ideal')
elif imc < 18.5:
    print('Você esta abaixo do seu peso ideal')
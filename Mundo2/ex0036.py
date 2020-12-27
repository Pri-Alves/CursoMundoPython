c = float(input('Valor da casa: R$ '))
s = float(input('Salario do Comprador: R$'))
pz = float(input('Quantos anos de financiamento:'))
p = (c / pz)/12
print('Para pagar um financiamento de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(c,pz,p))
if p <= s * 0.3:
    print('Emprestimo pode ser CONCEDIDO!!')
else:
    print('Emprestimo NEGADO!!')
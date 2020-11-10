print('========== LOJA PANDAS ==========')
p = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] A vista no Dinheiro/Cheque')
print('[ 2 ] A vista Cartão')
print('[ 3 ] Em 2x no Cartão')
print('[ 4 ] Em 3x ou mais no Cartão')
op = int(input('Qual é a opção: '))
if op == 1:
    print('Sua compra de R${} vai custar R${} no final.'.format(p,p*0.9))
elif op == 2:
    print('Sua compra de R${} vai custar R${} no final.'.format(p,p*0.95))
elif op == 3:
    print('Sua compra de R${} será dividida em 2 parcelas de R${} cada.'.format(p, p/2))
elif op == 4:
    pc = int(input('Quantas parcelas: '))
    jr = p + (p*0.2)
    print('Sua compra será parcela em {}X de R${} COM JUROS'.format(pc,jr/pc))
    print('Sua compra de R$ {} vai custar {} no final.'.format(p,jr))

print('=*='*10)
print('SUPERMERCADO SUPER BARATO')
print('=*='*10)
s = 0
contmil = 0
nome = ''
menor = 0
while True:
    n = str(input('Nome do Produto: ')).upper().strip()
    p = float(input('Preço: '))
    e = str(input('Deseja Continuar? [S/N] ')).upper().strip()
    if s == 0:
        nome = n
        menor = p
    if p < menor:
        nome = n
        menor = p
    s += p
    if p > 1000.00:
        contmil += 1
    if e == 'N':
        break
print('=*='*10)
print ('FIM DO PROGRAMA')
print('=*='*10)
print(f'O total da compra foi de R${s:.2f}')
print(f'temos {contmil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {nome} custando R${menor:.2f}')
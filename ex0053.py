f = str(input('Digite uma Frase: ')).strip().upper()
palavras = f.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
print('o inverso de {} é {}'.format(junto,inverso))
if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo!')

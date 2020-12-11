while True:
    n = int(input('Quer ver a Tabuada de qual numero? '))
    if n < 1:
        break
    for c in range (1,11):
        print (f'{n:3} x {c:3} = {n*c:3}')
print('O programa foi encerrado')
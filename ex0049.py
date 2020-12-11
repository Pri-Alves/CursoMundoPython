n = int(input('Digite um numero para ver a tabuada: '))
for t in range(1,11):
    s = n * t
    print('{:3} x {:3} = {:3}'.format(n,t,s))
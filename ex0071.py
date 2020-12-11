import math
print('='*30)
print('BANCO CEV')
print('='*30)
total = 0
ced = 50
totalced = 0
v = int(input('Quanto dinheiro você quer sacar? '))
total = v
while True:
   if total >= ced:
      total -= ced
      totalced += 1
   else:
       if totalced > 0:
            print(f'Total de {totalced} cédulas de {ced}')
       if ced == 50:
           ced = 20
       elif ced == 20:
           ced = 10
       elif ced == 10:
           ced = 1
       totalced = 0
       if total == 0:
           break
print('='*30)
print('VOLTE SEMPRE!!')




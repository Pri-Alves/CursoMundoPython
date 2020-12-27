maiores = 0
homem = 0
mulher = 0
while True:
    print('=' * 25)
    print('Cadastre uma Pessoa')
    print('-' * 25)
    i = int(input('Idade: '))
    s = str(input('Sexo [F/M]: ')).upper().strip()
    print('-' * 25)
    if i > 18:
       maiores += 1
    if s == 'M':
        homem += 1
    if s == 'F' and i < 20:
        mulher += 1
    e = str(input('Quer Continuar? [S/N] ')).upper().strip()
    if e == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher} mulheres com menos de 20 anos')
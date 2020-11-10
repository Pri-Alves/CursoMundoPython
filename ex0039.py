from datetime import date
an = int(input('Ano de nascimento: '))
aa = date.today().year
id = aa-an
al = aa + (18-id)
print('Quem nasceu em {} tem {} anos em {}'.format(an,id,aa))
if id < 18:
    al = aa + (18-id)
    print('Ainda faltam {} anos para o seu alistamento'.format(18-id))
    print('Seu alistamento será em {}'.format(al))
elif id > 18:
    la = aa - (id-18)
    print('Você ja deveria ter se alistado a {} anos'.format(id-18))
    print('Seu alistamento foi em {}'.format(la))
elif id == 18:
    print('Você deve se alistar IMEDIATAMENTE:')

l = float(input('Largura da Parede: '))
a = float(input('Altura da Parede: '))
print('Sua parede de tem a dimensão de {}x{} e sua area é de {}m².\nPara pintar esta parede, você precisará de {:.4f} litros de tinta'.format(l,a,(l*a),((l*a)/2)))
peso = float(input('Digite seu peso: '))
print('-'*20)
altura = float(input('Digite sua altura: '))
imc = peso / altura ** 2
print('-'*20)
print(f'{imc:.2f}')
print('-'*20)

sit = ''

if imc < 20:
    sit = 'Abaixo do peso'
elif imc < 25:
    sit = 'Normal'
elif imc < 30:
    sit = 'Excesso de peso'
elif imc < 35:
    sit = 'Obesidade'
else:
    sit = 'Obsidade mórbida'

print(sit)

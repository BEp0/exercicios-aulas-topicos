import modulo

valor = int(input('Digite um valor inteiro:'))
operacao = input('Você quer dobrar ou triplicar este número:').upper()
if operacao == 'DOBRAR':
    print(f'O {valor} com valor dobrado é {modulo.dobro(valor)}')
elif operacao == 'TRIPLICAR':
    print(f'O {valor} com valor triplicado é {modulo.triplo(valor)}')  
else:
    print('Reinicie o programa, algo deu errado!')

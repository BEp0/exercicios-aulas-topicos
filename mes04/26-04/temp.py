class operacoes:
    
    
    class mais:
        def __init__ (self, n1, n2, soma):
            self.n1 = n1
            self.n2 = n2
            self.soma = n1 + n2

        def __str__(self):
            print('\n< ADIÇÃO >\n')
            return str(f'{self.n1} + {self.n2} = {self.soma}\n') and self.soma

    
    class menos:
        def __init__ (self, n1, n2, sub):
            self.n1 = n1
            self.n2 = n2
            self.sub = self.n1 - self.n2

        def __str__ (self):
            print('\n< SUBTRAÇÃO >\n')
            return str(f'{self.n1} - {self.n2} = {self.sub}\n') and self.sub


    class multiplicar:
        def __init__(self, n1, n2):
            self.n1 = n1
            self.n2 = n2

        def __str__(self):
            print('\n< MULTIPLICAÇÃO >\n')
            return str(f'{self.n1} X {self.n2} = {self.n1 * self.n2}\n')


    class dividir:
        def __init__(self, n1, n2):
            self.n1 = n1
            self.n2 = n2

        def __str__(self):
            print('\n< DIVISÃO >\n')
            return str(f'{self.n1} / {self.n2} = {self.n1 / self.n2}\n')


    class resto:
        def __init__ (self, n1, n2):
            self.n1 = n1
            self.n2 = n2

        def __str__ (self):
            print('\n< RESTO >\n')
            return str(f'{self.n1} % {self.n2} = {self.n1 % self.n2}\n')


def aplicar_operacao(a, b, operation):
    if operation == '+':
        c = operacoes.mais(a, b, 0)
        print(c)

    
    elif operation == '-':
        c = operacoes.menos(a, b, 0)
        print(c)

    
    elif operation == '*' or operation == 'X':
        c = operacoes.multiplicar(a, b)
        print(c)


    elif operation == '%' or operation == 'RESTO':
        c = operacoes.resto(a, b)
        print(c)
    


def main():


    a = int(input('\nDigite o 1º valor: '))
    b = int(input('\nDigite o 2º valor: '))
    
    operation = str(input('\nQual a operação: ')).strip().upper()

    aplicar_operacao(a, b, operation)



if __name__ == "__main__":
    main()

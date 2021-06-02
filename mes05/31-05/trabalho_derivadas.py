import sympy as sym

# Declaro as variáveis
x, y, z = sym.symbols('x y z')

# criei as duas expressões que serão derivadas
e1 = x**7 - 8*x**5 + 4*x**3 - 4*x + 9
e2 = 5*x**6 - 8*x**4 + 4*x**2 - 5*x - 8

# calculo da derivada 1º função
derivada_primeira_em_e1 = sym.diff(e1, x)
print('1º derivada de x^7 - 8*x^5 + 4*x^3 - 4*x + 9: ', derivada_primeira_em_e1)

# calculo da derivada 2º função
derivada_primeira_em_e2 = sym.diff(e2, x)
print('1º derivada de  5*x^6 - 8*x^4 + 4*x^2 - 5*x - 8: ', derivada_primeira_em_e2)

# 2º derivada função 1
derivada_segunda_em_e1 = sym.diff(e1, x, 2)
print('2º derivada de x^7 - 8*x^5 + 4*x^3 - 4*x + 9: ', derivada_segunda_em_e1)

# 2º derivada função2
derivada_segunda_em_e2 = sym.diff(e2, x, 2)
print('2º derivada de 5*x^6 - 8*x^4 + 4*x^2 - 5*x - 8: ', derivada_segunda_em_e2)

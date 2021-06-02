# Importo a biblioteca
import sympy as sym
  
# Declaro as variáveis
x, y, z = sym.symbols('x y z')

# crio a expressão que será derivada
exp = x**3 * y + y**3 + z

# Encontro a derivada segunda da expressão com relação a x
derivada_segunda_em_x = sym.diff(exp, x, 2)
print('derivada segunda em relacao a x: ', 
      derivada_segunda_em_x)
  
# Encontro a derivada segunda da expressão com relação a y
derivada_segunda_em_y = sym.diff(exp, y, 2)
print('derivada segunda em relacao a y: ', 
      derivada_segunda_em_y)

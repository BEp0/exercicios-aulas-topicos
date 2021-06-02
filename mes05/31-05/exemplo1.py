# Importo a biblioteca
import sympy as sym
  
# Declaro as variáveis
x, y, z = sym.symbols('x y z')
  
# crio a expressão que será derivada
exp = x**3 * y + y**3 + z
  
# calculo a derivada com relação a x
derivada_primeira_em_x = sym.diff(exp, x)
print('derivada em relacao a x: ', 
      derivada_primeira_em_x)

# calculo a derivada com relação a y
derivada_primeira_em_y = sym.diff(exp, y)
print('derivada em relacao a y: ', 
      derivada_primeira_em_y)

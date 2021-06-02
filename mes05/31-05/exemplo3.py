# Importo a biblioteca
import sympy as sym
  
# Declaro as variáveis
x, y, z = sym.symbols('x y z')

# Integração indefinida de cos (x) dx
integral1 = sym.integrate(sym.cos(x), x)
print('integral indefinida de cos(x): ', 
      integral1)
  
# integração definida de cos (x) dx entre -1 a 1
integral2 = sym.integrate(sym.cos(x), (x, -1, 1))
print('integral definida de cos(x) entre -1 e 1: ', 
      integral2)
  
# definte integration of exp(-x) w.r.t. dx between 0 to ∞
integral3 = sym.integrate(sym.exp(-x), (x, 0, sym.oo))
print('integral definida de cos(x) entre 0 e ∞: ', 
      integral3)
  


# Importo a biblioteca
import sympy as sym
  
# Declaro as variáveis
x, y, z = sym.symbols('x y z')

# Calculando o limite de f(x) = x com x->∞
limit1 = sym.limit(x, x, sym.oo)
print(limit1)
  
# Calculando o limite de f(x) = 1/x com x->∞
limit2 = sym.limit(1/x, x, sym.oo)
print(limit2)
  
# Calculando o limite de f(x) = sin(x)/x com x->0
limit3 = sym.limit(sym.sin(x)/x, x, 0)
print(limit3)


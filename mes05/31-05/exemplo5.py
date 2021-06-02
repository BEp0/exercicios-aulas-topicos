# Importo a biblioteca
import sympy as sym
  
# Declaro as variáveis
x, y, z = sym.symbols('x y z')

# Determina a serie
series1 = sym.series(sym.cos(x), x)
print(series1)
  
# Determina a serie
series2 = sym.series(1/sym.cos(x), x, 0, 4)
print(series2)

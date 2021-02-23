txt = "lorem isp de"
de = "de"
lista = txt.split()
x = 0
for i in lista:
    if i == de:
        x += 1
print(x)
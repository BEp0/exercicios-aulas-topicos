
def classifica(n):
    ouro = ['', 99]
    prata = ['', 99]
    bronze = ['', 99]
    for i in n:
        if (i[1]<ouro[1]):
            bronze, prata, ouro=prata, ouro, i
        elif (i[1] < prata[1])
        # terminar...
def main():
    print(classifica([('Joao', 8), ('Jose', 9.2), ('Maria', 7), ('Ana', 9.5), ('Pedro', 7.1)]))
   

if __name__ == "__main__":
    main()
# exemplo de recursividade
def fatorial(n):
  print(f"Empilhando um registro na pilha para fatorial ({str(n)})\n" )
  if (n<2):
    print("Desempilhando um registro da pilha para fatorial(1)\n" )
    return 1
  else:
    f = n * fatorial(n-1)
    print(f"Desempilhando um registro da pilha para fatorial ({str(n)}) \n" )
    return f

def main():
	a = input("informe um número:")
	x = int(a)
	y = fatorial(x)
	print(f"O fatorial é: {y}")
if __name__ == "__main__":
	main()
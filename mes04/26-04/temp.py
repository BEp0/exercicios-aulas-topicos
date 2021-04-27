class mais:
    def __init__ (self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    def __str__(self):
        return str(self.n1 + self.n2) 

def main():
    a = mais(1, 2)
    print(a)


if __name__ == "__main__":
    main()

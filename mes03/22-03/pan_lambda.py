# exemplo dado

def classifica(atletas):
    ordenados = sorted(atletas, key=lambda x: x[1])

    return tuple(x[0] for x in ordenados[:3])

def main():
    podio = classifica([
        ('John', 9.2),
        ('Timoshenko', 9.8),
        ('Usain', 8.9),
        ('Ze', 9.5),
    ])

    print(podio)

if __name__ == '__main__':
    main()
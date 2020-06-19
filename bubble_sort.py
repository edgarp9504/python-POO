import random

def ordenamiento_de_burbuja(lista):
    
    n = len(lista)
    print(f'Este es el numero de iteracciones {n}')
    for i in range(n):
        print(f'Esta es la letra i = {i}')
        for j in range(0, n - i - 1):
            print(f'Esta es la letra j = {j}')
            if lista[j] > lista[j +1]:
                lista[j], lista[j +1] = lista[j + 1], lista[j]
                print(f'esta es la lista{lista}')
    return lista

if __name__ == '__main__':
    tamano_lista = int(input('De que tamaño sera la lista?: '))

    lista = [random.randint(0,100) for i in range(tamano_lista)]

    print(lista)

    lista_ordenamiento = ordenamiento_de_burbuja(lista)

    print(lista_ordenamiento)
import random

def buscaCega(array):
    lugarA = random.randrange(len(array))
    print(f"lugar aleatório escolhido: {lugarA}, valor: {array[lugarA]}")

    while True:
        esquerda = array[lugarA - 1] if lugarA > 0 else float('-inf')
        direita = array[lugarA + 1] if lugarA < len(array) - 1 else float('-inf')
        valorA = array[lugarA]

        if valorA >= esquerda and valorA >= direita:
            return valorA
        
        if esquerda > direita:
            lugarA -= 1
            print(f"lugar atual: {lugarA}, valor: {array[lugarA]}")
        else:
            lugarA += 1
            print(f"lugar atual: {lugarA}, valor: {array[lugarA]}")

 
lugar = [7, 4, 5, 3, 3, 12, 9, 16, 44, 32, 67, 8, 15, 14, 13, 11, 22, 20, 10, 5, 1, 69, 8, 4, 3 ,2, 2, 10, 74]
print(f"Array completo: {lugar}")

resultado = buscaCega(lugar)
print(f"otimo local: {resultado}")

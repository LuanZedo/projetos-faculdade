# status dos monstros, pode adicinar mais ou alterar existentes
monstros = [
    {"nivel": 1, "vida": 12, "dano": 2},
    {"nivel": 2, "vida": 15,"dano": 4},
    {"nivel": 3, "vida": 20,"dano": 6},
    {"nivel": 4, "vida": 25,"dano": 8}
]

#status do personagem, pode ser alterado
personagem = {"vida": 100, "dano": 10}

turno = 0

#le os monstros individualmente do array monstros
for monstro in monstros:

    #enquanto o turno for menor ou igual a 10 e a vida do personagem for maior que 0
    while turno <= 10 and personagem["vida"] > 0:
        print(f"status do monstro atual: {monstro}\n")

        #diminui a vida do monstro atual com base no dano do personagem
        monstro["vida"] -= personagem["dano"]
        print(f"dano dado ao monstro: {personagem["dano"]}\n")
        print(f"vida do monstro: {monstro["vida"]}\n")

        #se a vida do monstro atual estiver menor ou igual a 0 seguira para o proximo monstro ou acabara com o for
        if monstro["vida"] <= 0:
            print(">>>MONSTRO DERROTADO!<<<\n")
            #adiciona um turno
            turno += 1
            print(f"turno: {turno}\n")
            break

        print(f"vida do personagem: {personagem["vida"]}\n")
        #diminui a vida do personagem com base no dano do monstro atual
        personagem["vida"] -= monstro["dano"]
        print(f"dano recebido: {monstro["dano"]}\n")
        print(f"vida personagem: {personagem["vida"]}\n")

        #adiciona um turno
        turno += 1
        print(f"turno: {turno}\n")

#se o turno for menor que 10 e a vida dos monstros forem menor ou igual a 0 o jogador vence
if turno < 10 and monstro["vida"] <= 0:
    print(">>>VOÇÊ DERROTOU TODOS OS MONSTROS!<<<\n")

#se o turno for maior que 10 o jogador perde
if turno > 10:
    print(">>>ACABARAM SEUS TURNOS<<<\n")

#se a vida do personagem for menor ou igual a zero o jogador perde
if personagem["vida"] <= 0:
    print(">>>SEU PERSONAGEM MORREU<<<\n")

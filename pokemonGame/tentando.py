import random

caverna = ["Zubat", "Geodude", "Aaron", "Onix"]
mato = ["Weedle", "Caterpie", "Metapod", "Bellsprout"]
pokedex = []
prob_capt_mato = 0.5
prob_capt_caverna = 0.35
extras = 3

def introducao():
    print(60 * "-")
    print("                            |MUNDO POKÉMON|")
    print(60 * "-")
    print("Olá!\nÉ um prazer conhecê-lo(a)!\nBem-vindo ao fabuloso mundo POKéMON!\nEu sou o professor Carvalho!\nMas primeiro, me fale um pouco sobre você! Então diga-me:")

def saber_nome():
    while True:
        nome = input("Como se chama? ")
        if nome.isalpha():
            print(f"Certo, {nome}!\nA sua própria lenda POKéMON está prestes a começar!\nUm mundo de sonhos e aventuras o aguarda! Então, vamos lá!")
            break
        else:
            print("Por favor, insira um nome válido.")

def pokemon_inicial():
    primeiro_pokemon = random.choice(caverna + mato)
    pokedex.append(primeiro_pokemon)

def menu():
    print("Escolha o que deseja fazer!")
    print("Essas são suas escolhas!:")
    print('''
[1] Caverna
[2] Mato
[3] Mostrar Pokédex
[4] Sair''')

def escolha_opcao():
    escolha = int(input("Escolha uma opção: "))
    print(60 * "-")
    if escolha == 4:
        print(f"Até logo! Espero te reencontrar novamente.")
        return escolha
    elif escolha < 1 or escolha > 4:
        print("Escolha incorreta, digite novamente!")
        return escolha
    else:
        return escolha

def escolha_1():
    while True:
        print("Você está adentrando a caverna...")
        pokemon_aleatorio = random.choice(caverna)
        print(f"Você entrou na caverna e encontrou um {pokemon_aleatorio}!")
        while True:
            if pokemon_aleatorio in pokedex:
                print(f"Você já tem o {pokemon_aleatorio} em sua pokédex!")
                break
            resposta = input("Deseja tentar capturar esse pokémon (S/N): ")
            if resposta.lower() == "s":
                if random.random() <= prob_capt_caverna:
                    pokedex.append(pokemon_aleatorio)
                    print(f"Parabéns!\nVocê capturou o {pokemon_aleatorio}!")
                    print("Voltando para o menu...")
                    break
                else:
                    print(f"O {pokemon_aleatorio} escapou!")
                    if extras > 0:
                        resposta2 = input(f"Quer tentar capturar o {pokemon_aleatorio} novamente(S/N): ")
                        if resposta2.lower() == "s":
                            extras -= 1
                            if random.random() <= prob_capt_caverna:
                                pokedex.append(pokemon_aleatorio)
                                print(f"Parabéns!\nVocê capturou o {pokemon_aleatorio}!")
                                print(f"Você tem {extras} tentativas extras!")
                                print("Voltando para o menu...")
                                break
                            else:
                                print(f"O {pokemon_aleatorio} escapou!")
                                print(f"Você tem {extras} tentativas extras!")
                                print("Voltando para o menu...")
                                break
                        else:
                            print("Voltando para o menu...")
                            break
                    else:
                        print("Você não tem mais tentativas extras.")
                        print("Voltando para o menu...")
                        break
            elif resposta.lower() == "n":
                print("Voltando para o menu...")
                break
            else:
                continue

def escolha_2():
    while True:
        print("Você está adentrando o mato...")
        pokemon_aleatorio = random.choice(mato)
        print(f"Você entrou no mato e encontrou um {pokemon_aleatorio}!")
        while True:
            if pokemon_aleatorio in pokedex:
                print(f"Você já tem o {pokemon_aleatorio} em sua pokédex!")
                break
            resposta = input("Deseja tentar capturar esse pokémon (S/N): ")
            if resposta.lower() == "s":
                if random.random() <= prob_capt_mato:
                    pokedex.append(pokemon_aleatorio)
                    print(f"Parabéns!\nVocê capturou o {pokemon_aleatorio}!")
                    print("Voltando para o menu...")
                    break
                else:
                    print(f"O {pokemon_aleatorio} escapou!")
                    if extras > 0:
                        resposta2 = input(f"Quer tentar capturar o {pokemon_aleatorio} novamente(S/N): ")
                        if resposta2.lower() == "s":
                            extras -= 1
                            if random.random() <= prob_capt_mato:
                                pokedex.append(pokemon_aleatorio)
                                print(f"Parabéns!\nVocê capturou o {pokemon_aleatorio}!")
                                print(f"Você tem {extras} tentativas extras!")
                                print("Voltando para o menu...")
                                break
                            else:
                                print(f"O {pokemon_aleatorio} escapou!")
                                print(f"Você tem {extras} tentativas extras!")
                                print("Voltando para o menu...")
                                break
                        else:
                            print("Voltando para o menu...")
                            break
                    else:
                        print("Você não tem mais tentativas extras.")
                        print("Voltando para o menu...")
                        break
            elif resposta.lower() == "n":
                print("Voltando para o menu...")
                break
            else:
                continue

def escolha_3():
    print("===POKÉDEX===")
    for pokemon_cap in pokedex:
        print(f"- {pokemon_cap}")

######      programa principal    #######

while True:
    introducao()
    saber_nome()
    pokemon_inicial()
    menu()
    opcao = escolha_opcao()
    if opcao == 1:
        escolha_1()
    elif opcao == 2:
        escolha_2()
    elif opcao == 3:
        escolha_3()
    elif opcao == 4:
        break

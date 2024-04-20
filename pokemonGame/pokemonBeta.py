import random

# Apresentação do Professor Carvalho e solicitação do nome do jogador
print("Olá! Bem-vindo ao mundo dos Pokémon!")
nome = input("Eu sou o Professor Carvalho. Antes de começarmos, qual é o seu nome? ")
print(f"Ótimo, {nome}! Prepare-se para uma grande aventura!")

# Lista de possíveis Pokémon que podem ser encontrados
pokemons = ['pikachu','zemadera','lobo']
pokeimg = ['''⣿⣿⣿⣿⣿⡇⣬⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡇⣿⣿⣮⡛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡇⢹⣿⣿⣿⣦⡛⢈⠛⠙⠿⣛⣩⣥⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠟⢀⣝⡻⢿⣿⢸⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣇⣈⠉⣽⣿⣿⣿⠿⠿⣿⣿⣿
⡇⠼⣿⣿⣶⣌⠈⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⡶⢒⣴
⣿⣧⠹⣿⣿⣿⣾⣿⡿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣴⣿⣿
⣿⣿⣧⠙⣹⣿⣿⡿⢱⡆⢿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⢿⠟⣫⣴⣿⣿⣿⣿
⣿⣿⣿⢰⣿⣿⠹⣧⠻⣇⡘⣿⣿⣿⣿⡿⠟⣩⡄⣿⣿⣿ ⡚⠻⠿⠿⠿⣿⣿
⣿⣿⡇⣾⣿⣿⢰⡜⠳⣦⣥⣿⣿⣟⠩⢤⣿⠟⣰⣿⣿⣿⣸⣿⣿⣿⣿⡦⠜⣻
⣿⣿⡇⢿⣿⣿⣌⢡⣷⡄⣉⣛⠻⠿⠷⠶⠶⠞⢫⣿⣿⡿⣿⣿⠿⢛⣩⣥⣿⣿
⣿⣿⢃⠸⣿⣿⣿⣦⣙⠡⢿⣿⡿⢰⣿⡇⠜⣡⣿⣿⣿⢃⣥⣴⣾⣿⣿⣿⣿⣿
⣿⡏⢸⣦⣿⣿⣿⣿⣿⣿⣶⣦⣥⣭⣥⣶⣿⣿⣿⣿⢃⣾⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡘⢿⣿⡟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣦⠉⠉ ⣝⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣶⣿⣿⣿⣦⡀⠌⣡⣌⢻⣿⣿⣿⡿⢡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣆⠻⠿⢛⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿''', 'i', 'i']

# Loop principal do jogo
while True:
    escolha = input("\nOnde você gostaria de explorar? (caverna/matagal/sair) ").lower()
    if escolha == "caverna":
        print("Você entrou na caverna...")
        pokemon_data = random.choice(list(zip(pokemons, pokeimg))) if random.randint(1, 3) >= 1 else (None, None)
        pokemon, pokemon_img = pokemon_data
        if pokemon:
            print(f"Você encontrou um {pokemon} na caverna!\n{pokemon_img}")
        else:
            print("Você não encontrou nenhum Pokémon na caverna desta vez.")
    elif escolha == "matagal":
        print("Você entrou no matagal...")
        pokemon = random.choice(pokemons) if random.randint(1, 10) == 1 else None
        if pokemon:
            print(f"Você encontrou um {pokemon} no matagal!")
        else:
            print("Você não encontrou nenhum Pokémon no matagal desta vez.")
    elif escolha == "sair":
        print("Obrigado por jogar! Até a próxima!")

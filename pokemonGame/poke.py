import random

# Apresentação do Professor Carvalho e solicitação do nome do jogador
print("Olá! Bem-vindo ao mundo dos Pokémon!")
nome = input("Eu sou o Professor Carvalho. Antes de começarmos, qual é o seu nome? ")
print(f"Ótimo, {nome}! Prepare-se para uma grande aventura!")

# Lista de possíveis Pokémon que podem ser encontrados
pokemonsCa = ['Gengar','Zubat','squirtle']
pokeimgCa = ['''⣿⣿⣿⣿⣿⡇⣬⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
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
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣆⠻⠿⢛⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿''',

'''⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢻⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⣄⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⠁⠀⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⣿⣿⣿⡇⢸⣿⣧⡀⠀⠈⢻⣿⣿⣿⣿⡇⠀⢀⣤⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⢹⣿⣿⡇⢸⣿⣿⣷⡄⠀⠀⠙⣿⣿⣿⠃⠀⣿⣿⢸⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⡇⢸⡿⠛⠛⠿⡄⠀⠀⠘⣿⣿⠀⠀⢿⣛⢸⣿⡟⠋⠻⣿⣿
⣿⣿⣿⣿⣿⣿⡟⠁⠀⢀⣴⣶⣿⣿⣿⣶⣄⠀⠀⢻⣿⢸⢃⣾⣿⣿⡦⠀⠀⠀⠈⠛⠀⠀⣿⣿⠸⠏⠀⠀⠀⢻⣿
⣿⣿⣿⣿⣿⠋⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠻⣇⢸⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠙⣿⠀⠀⠀⠀⠀⠘⣿
⣿⣿⣿⡿⠁⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⠋⠀⣀⣤⣄⠀⠹⡌⠻⠋⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠘⠀⠀⠀⣶⣆⠀⣿
⣿⣿⡿⠁⠀⢀⣾⣿⣿⣿⣿⣿⣿⡟⠁⣠⣾⣿⣿⣿⣧⡀⠱⡀⠀⠀⠀⠀⠀⢰⣧⣼⣧⠎⠀⠀⠀⠀⣸⣿⣿⠀⣿
⣿⣿⠃⠀⢀⣾⣿⣿⣿⣿⣿⣿⠏⢀⣴⣿⣿⣿⣿⣿⣿⠷⠀⠀⠀⠀⠀⠀⠀⣿⢿⣿⡿⡆⠀⠀⠀⢀⣿⣿⣿⠀⢹
⣿⡟⠀⠀⣼⣿⣿⣿⣿⣿⣿⠏⢠⣾⣿⣿⡿⠟⠋⠉⢀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠛⠀⠁⢀⠀⠀⣸⣿⣿⣿⠀⣾
⣿⠃⠀⣸⣿⣿⣿⣿⣿⣿⠋⣰⣿⡿⠟⠉⠀⢀⣤⡶⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠀⠀⣿⣿⣿⣿⠀⣿
⣿⠀⢠⣿⣿⣿⣿⣿⡿⠃⣰⠟⠋⠀⢀⣤⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⠀⢸⣿⣿⣿⡏⠀⣿
⡟⠀⣼⣿⠿⠟⠛⠛⠁⠀⠁⢀⣴⣾⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡘⢿⠃⠀⣿⣿⣿⣿⠇⢰⣿
⡇⠀⠟⠁⠀⣀⣀⣀⡀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⡄⠀⢰⣿⣿⣿⡿⠀⣸⣿
⡇⢀⣤⣶⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⢀⣴⣤⣀⡀⠀⠀⢀⣴⣾⣿⣿⣿⡇⠀⠈⠙⣿⣿⠃⢠⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⢀⣴⣿⣿⣿⡟⠀⢀⣴⣿⣿⣿⣿⣿⣿⣴⣶⣶⡀⢸⠇⢠⣾⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⢀⣴⣿⣿⣿⣿⠏⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣠⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣠⣾⣿⣿⣿⣿⡿⠁⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣼⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣉⣴⣾⣿⣿⣿⣿⣿⠋⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⠟⣡⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿''',

'''⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣷⣾⣿⣿⣷⣿⣟⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⢺⣿⣿⣿⣿⣿⡿⣛⡻⣿⣿⣾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠘⣿⣿⣿⣿⣿⣿⠁⠙⠁⢸⣿⣿⣏⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣧⣸⣿⣿⣿⣿⣿⣇⠠⠤⢾⣸⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣹⡻⠿⣛⣛⣛⣛⣻⡿⠿⠿⣛⣿⣿⡞⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡝⡥⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⢿⣿⣧⢍⣛⡻⠯⠷⡿⠿⠽⣓⣡⣚⠙⣮⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⢿⣿⣽⣿⣿⡿⣵⣿⣿⣿⣿⣿⣷⢯⣾⣿⣿⣿⣷⠠⣕⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣷⢻⡏⣿⣿⣿⡿⣾⣿⣿⣿⣽⣻⣛⣋⣾⣿⣿⣿⣿⣿⢀⣯⣗⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣷⣛⣛⣾⣟⣟⢃⣿⣿⣿⣿⡇⣿⡿⣻⣷⣞⡿⡿⡿⣣⡗⣾⣿⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣹⡞⣿⣿⣿⣧⣿⣯⣭⣛⠿⣟⣡⣵⣿⡇⣯⠿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⢏⣻⣿⣿⣶⣶⣿⣿⣿⣿⣼⢿⣿⡇⣿⡇⡍⡃⣼⣿⣻⣷⣿⣿⣿⣾⡝⣿
⣿⣿⣿⣿⣿⣻⣿⣝⣿⣿⣿⡿⣿⣿⣿⣿⣟⣶⣾⣿⣷⣕⠸⢱⢟⣾⣿⣿⠟⣛⠻⣿⣿⣹
⣿⣿⣿⣿⡟⣿⣿⣿⣮⡛⣿⣥⣟⡿⢿⣏⣾⣿⣿⣿⣿⣿⡄⣵⣿⣿⣿⢡⣿⣿⣿⣿⣿⢸
⣿⣿⣿⣿⡏⣿⣿⣿⣿⣿⢪⣽⣿⣛⣟⡂⢿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣽⣦⠻⢿⡿⡷⣫⣿
⣿⣿⣿⣯⠻⡟⣿⠿⣋⣯⣿⣿⣿⣿⣿⣿⣯⢿⣿⣿⣿⣿⡗⣾⣭⣽⣯⣿⣿⣦⣴⣿⣿⣿
⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡼⣟⢿⡿⢞⡷⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿''']

pokemonsMa = ['Bellsprout','Lugia','pikachu']
pokeimgMa = ['''⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠁⠀⠀⠀⠀⠈⠉⠛⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⣴⣿⡆⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠈⠉⠀⠀⠀⠀⠸⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰
⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿
⣿⡿⠿⠿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿
⠋⢠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⡾⠿⣿⣿⣿
⠀⢸⡏⠀⠈⠛⢷⣦⡀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⣶⣿⣿⣿⠋⠁⠀⠀⣿⣿⣿
⣇⠈⢿⣆⠀⠀⠀⠙⢿⣆⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⢀⣿⣿⣿
⣿⣧⡀⠻⣷⣄⠀⠀⠀⠻⣧⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⣾⣿⣿⣿
⣿⣿⣿⣦⡈⠛⢷⣦⣀⣀⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣶⣄⣈⠉⠉⠉⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⣻⣿⣿⣿''',

'''⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠙⠻⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⣻⠇⠀⠀⠈⢫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡜⢿⣷⣄⡀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠙⠊⢛⡀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠈⠻⡟⠀⠀⢠⣄⣸⠟⢁⣿⣿⣿⡟⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠳⢤⠠⠀⠀⠘⠓⠤⡖⠋⣹⣿⣿⡇⠸⡟⠛⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠖⠁⠀⠀⠀⠀⠀⠀⠈⠋⢤⣿⣿⡿⠁⣧⣾⣿⣿
⣿⣿⣿⣿⣿⠟⠁⠀⣠⡄⡀⠀⠀⣴⣶⣶⡀⠀⠈⠫⡀⣸⣿⣿⣿⣿
⣿⣿⣿⡿⠃⠀⠀⣰⣿⢿⣿⣷⣾⣿⣿⣿⠟⢆⠀⠀⠈⠻⣿⣿⣿⣿
⣿⣿⠟⠀⠀⠀⢠⣿⣿⡀⠻⣿⣿⣿⣿⣋⡀⢈⡆⠀⠀⠀⠈⢻⣿⣿
⣿⡏⠀⠀⠀⠀⢸⣿⣿⣿⣶⠀⢱⣶⣤⣤⣄⣀⡷⠀⠀⠀⠀⠀⢻⣿
⣿⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠈⣿
⢿⠀⠀⢠⠀⢰⡄⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⡀⣼⠀⠀⡀⠀⠀⣥
⣿⣀⠀⢸⡄⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢀⣇⣀⣷⣿
⣿⣿⣷⣾⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿''',

'''⣿⣿⣿⣿⣿⣿⠏⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠏⣠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿
⣿⣿⣿⣿⡿⣾⣿⣸⣿⣿⣿⣿⣿⣿⣿⡿⣿⣛⣿⣭⠉⠉⣹⣿⣿⡿⣫⣾⡟⣿
⣿⣿⣿⣿⣧⡿⣃⣛⣿⣿⣿⣻⢟⣯⣷⣿⣿⣿⣿⢏⣠⣾⣿⡿⣫⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡣⢾⣿⣿⣿⠩⠙⣿⣿⣛⠛⣻⣯⣽⣾⣿⣿⡿⣫⣾⣿⣿⣿⣿⣿⢸
⣿⣿⣿⢇⣈⡾⢿⡿⢿⣷⡶⣛⡻⣿⣷⢿⣿⣿⣿⣿⠫⢾⣻⣻⣿⣿⡿⣟⣽⣾
⣿⣿⡟⡄⣿⣆⠀⣀⢸⣿⣞⣫⣣⣿⣿⡾⣿⣿⣿⣿⡞⣿⣿⡿⣻⣵⣾⣿⣿⣿
⣿⣿⣿⣔⢿⣿⣯⣛⣼⣿⣿⣿⣿⡿⣿⣿⡽⣿⣿⣿⣿⡼⣿⣇⣿⣿⣿⣿⣿⣿
⡿⣟⣯⣽⣶⣝⣿⢿⣿⣿⣿⣿⣩⣶⣶⣿⣿⡘⢿⣿⢟⣭⣿⢟⣿⣿⣿⣿⣿⣿
⡇⢧⣿⣿⣿⣿⡝⣷⣽⣿⣿⣿⣧⡛⠻⠛⣻⣿⣷⡵⣝⠟⠱⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣶⣿⣭⣭⣿⡜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣨⠁⣀⣹⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢈⣻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣧⢿⣿⣿⣿⠿⠿⣿⣿⡿⠿⢿⣛⡵⣹⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣯⣝⡛⠚⣭⣶⣶⣮⣽⣟⣛⢛⡅⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡤⣿⣿⣿⣿⣿⣿⣿⣯⡁⣿⣿⣿⣿⣿⣿⣿⣿⣿''']

# Loop principal do jogo
Pokemons_Pokedex = []
tentativas_extra = 3

while True:
    escolha = input("\nOnde você gostaria de explorar? (caverna/matagal/sair) ").lower()
    if escolha == "sair":
        print("Obrigado por jogar! Até a próxima!")
        break
    elif escolha == "caverna":
        print("Você entrou na caverna...")
        pokemon_dataCa = random.choice(list(zip(pokemonsCa, pokeimgCa)))
        pokemon, pokemon_img = pokemon_dataCa
        if pokemon in Pokemons_Pokedex :
            print("Você já capturou este Pokémon antes!")
            pokedex = input("Você deseja visualizar seus Pokemóns capturados?").lower()
            if pokedex == "sim" :
                print(Pokemons_Pokedex)
                continue
            else:
                continue
        if pokemon:
            print(f"Você encontrou um {pokemon} na caverna!\n{pokemon_img}")
            if pokemon not in Pokemons_Pokedex:
                capturar = input("Você deseja tentar capturar este Pokémon? (sim/não) ").lower()
                if capturar == "sim":
                    probabilidade_captura = 0.35  # Probabilidade de captura na caverna
                    if random.random() <= probabilidade_captura:
                        print(f"Parabéns! Você capturou o {pokemon}! Ele foi adicionado a sua pokedex!")
                        Pokemons_Pokedex.extend(pokemon)
                    else:
                        print(f"Oops! Você não conseguiu capturar o {pokemon}.")
                        tentativas_extra -= 1
                        if tentativas_extra <= 0:
                            print("Você usou todas as suas tentativas extras de captura.")
                            continue
                        tentar_novamente = input("Você deseja tentar capturar novamente? (sim/não) ").lower()
                        if tentar_novamente == "não":
                            continue
                else:
                    print("Você decidiu não capturar o Pokémon.")

                
#matagal 
    elif escolha == "matagal":
        pokemon_dataCa = random.choice(list(zip(pokemonsCa, pokeimgCa)))
        pokemon, pokemon_img = pokemon_dataCa
        if pokemon in Pokemons_Pokedex :
            print("Você já capturou este Pokémon antes!")
            pokedex = input("Você deseja visualizar seus Pokemóns capturados?").lower()
            if pokedex == "sim" :
                print(Pokemons_Pokedex)
                continue
            else:
                continue
        if pokemon:
            print(f"Você encontrou um {pokemon} na caverna!\n{pokemon_img}")
            if pokemon not in Pokemons_Pokedex:
                capturar = input("Você deseja tentar capturar este Pokémon? (sim/não) ").lower()
                while capturar == 'sim':
                    probabilidade_captura = 0.5 # Probabilidade de captura na caverna
                    if random.random() <= probabilidade_captura:
                        print(f"Parabéns! Você capturou o {pokemon}!")
                        Pokemons_Pokedex.extend(pokemon)
                    else:
                        print(f"Oops! Você não conseguiu capturar o {pokemon} :( .")
                        tentativas_extra -= 1
                        tentar_novamente = input(f"você deseja tentar capturar novamente?").lower()
                        if tentar_novamente == 'sim':
                            if tentativas_extra <= 0:
                                print("chances i

                        else:
                            print(f"você decidiu não tentar novamente")
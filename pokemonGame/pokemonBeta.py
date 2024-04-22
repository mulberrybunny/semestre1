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

Pokemons_Pokedex = []
tentativas_extra = 3
# Loop principal do jogo
while True:
    escolha = input("\nO que você gostaria de explorar? \ncaverna \nmatagal \npokedex \nsair \n").lower()
    if escolha == "caverna":
        print("Você entrou no caverna...")
        pokemon_dataCa = random.choice(list(zip(pokemonsCa, pokeimgCa))) 
        pokemon, pokemon_img = pokemon_dataCa
        if random.randint(1, 2) == 1:
            print(f"você tem {tentativas_extra} tentativas para capturar o pokemon.")
            print(f"Você encontrou um {pokemon} no caverna!\n{pokemon_img}") 
            if pokemon in Pokemons_Pokedex :
                print("Você já tem esse Pokemón.") 
                continue
            else:
                while tentativas_extra > 0 and tentativas_extra < 4 and pokemon not in Pokemons_Pokedex: #Se ainda tiver tentativas e okemon não estiver na pokedex
                        capturar = input("Você deseja tentar capturar este Pokémon? (sim/não) ").lower()
                        if capturar == "sim":
                            probabilidade_captura = 0.35 # Probabilidade de captura na caverna
                            if random.random() <= probabilidade_captura:
                                print(f"Parabéns! Você capturou o {pokemon}!")
                                Pokemons_Pokedex.append(pokemon)
                                tentativas_extra -= 1
                            else:
                                
                                print(f"Oops! Você não conseguiu capturar o {pokemon} :( .")
                                tentativas_extra -= 1
                                tentar_novamente = input("Você deseja tentar capturar novamente? (sim/não)\n").lower()
                                if tentar_novamente == "sim" or pokemon not in Pokemons_Pokedex and tentativas_extra > 1:
                                    probabilidade_captura = 0.35  # Probabilidade de captura na caverna
                                    if random.random() <= probabilidade_captura and pokemon not in Pokemons_Pokedex:
                                        print(f"Parabéns! Você conseguiu capturar o {pokemon}! Ele foi adicionado a sua pokedex!")
                                        Pokemons_Pokedex.append(pokemon)
                                        break
                                    else:
                                        print(f"Oops! Você não conseguiu capturar o {pokemon}.")  
                                        tentativas_extra -= 1
                                        continue
                                else:
                                    print(f"você decidiu não tentar novamente")
                                    continue
                        else:
                            print(f"vc decidiu não capturar o pokemon")
        else:
            print("Você não encontrou nenhum Pokémon no caverna desta vez.")

    elif escolha == "matagal":
        print("Você entrou no matagal...")
        pokemon_dataMa = random.choice(list(zip(pokemonsMa, pokeimgMa))) 
        pokemon, pokemon_img = pokemon_dataMa
        if random.randint(1, 2) == 1:
            print(f"você tem {tentativas_extra} tentativas para capturar o pokemon.")
            print(f"Você encontrou um {pokemon} no matagal!\n{pokemon_img}") 
            if pokemon in Pokemons_Pokedex :
                print("Você já tem esse Pokemón.") 
                continue
            else:
                while tentativas_extra > 0 and tentativas_extra < 5 and pokemon not in Pokemons_Pokedex: #Se ainda tiver tentativas e okemon não estiver na pokedex
                        capturar = input("Você deseja tentar capturar este Pokémon? (sim/não) ").lower()
                        if capturar == "sim":
                            probabilidade_captura = 0.5 # Probabilidade de captura na caverna
                            if random.random() <= probabilidade_captura:
                                print(f"Parabéns! Você capturou o {pokemon}!")
                                Pokemons_Pokedex.append(pokemon)
                                tentativas_extra -= 1
                            else:
                                
                                print(f"Oops! Você não conseguiu capturar o {pokemon} :( .")
                                tentativas_extra -= 1
                                tentar_novamente = input("Você deseja tentar capturar novamente? (sim/não)\n").lower()
                                if tentar_novamente == "sim" or pokemon not in Pokemons_Pokedex and tentativas_extra > 1:
                                    if random.random() <= probabilidade_captura and pokemon not in Pokemons_Pokedex:
                                        print(f"Parabéns! Você conseguiu capturar o {pokemon}! Ele foi adicionado a sua pokedex!")
                                        Pokemons_Pokedex.append(pokemon)
                                        break
                                    else:
                                        print(f"Oops! Você não conseguiu capturar o {pokemon}.")  
                                        tentativas_extra -= 1
                                        continue
                                else:
                                    print(f"você decidiu não tentar novamente")
                                    continue
                        else:
                            print(f"vc decidiu não capturar o pokemon")
        else:
            print("Você não encontrou nenhum Pokémon no matagal desta vez.")
    elif escolha == "pokedex":
            print(Pokemons_Pokedex)
    elif escolha == "sair":
        print("Obrigado por jogar! Até a próxima!")
        break
    else:
        print(f"invalido")

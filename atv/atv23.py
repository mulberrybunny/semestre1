print("Enquete de jogos!")
votos = {'CS2': 0, 'Dota 2': 0, 'LOL': 0, 'Valorant': 0}
idades = []
totalVotantes = 0

while True:
    idade = int(input("Qual sua idade? "))
    if idade < 0:
        print("Idade inválida. Tente novamente.")
        continue

    opcao = int(input("Selecione uma opção:\n 1 - CS2\n 2 - Dota 2\n 3 - LOL\n 4 - Valorant\n 5 - Sair\n"))

    if opcao == 5:
        break

    if opcao in [1, 2, 3, 4]:
        totalVotantes += 1
        idades.append(idade)
        if opcao == 1:
            votos['CS2'] += 1
        elif opcao == 2:
            votos['Dota 2'] += 1
        elif opcao == 3:
            votos['LOL'] += 1
        elif opcao == 4:
            votos['Valorant'] += 1
    else:
        print("Opção inválida. Tente novamente.")

# idade media
if totalVotantes > 0:
    mediaIdades = sum(idades) / totalVotantes
else:
    mediaIdades = 0

# resultados
for jogo, votosjogo in votos.items():
    mediaJogo = mediaIdades if totalVotantes > 0 else 0
    print(f"[{jogo}, {votosjogo}, {mediaJogo:.2f}]")

maisVotado = max(votos, key=votos.get)
menosVotado = min(votos, key=votos.get)
print(f"Mais Votado: {maisVotado} com {votos[maisVotado]} votos.")
print(f"Menos Votado: {menosVotado} com {votos[menosVotado]} votos.")
print(f"Total de votantes: {totalVotantes}, média de idade: {mediaIdades:.2f}")

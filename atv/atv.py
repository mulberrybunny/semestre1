for i in range(1, 51):
    print(i)

#ex 2

for i in range(2, 101, 2):
    print(i)

#Ex 3

valor = int(input("Digite um valor entre 1 e 10: "))
if 1 <= valor <= 10:
    for i in range(1, 11):
        print(f"{valor} x {i} = {valor * i}")
else:
    print("Valor fora do interval")

#Ex 4

soma_idades = 0
quantidade = 0
while True:
    idade = int(input("Digite uma idade (digite 0 para parar): "))
    if idade == 0:
        break
    soma_idades += idade
    quantidade += 1

if quantidade != 0:
    media = soma_idades / quantidade
    print(f"A média das idades é: {media}")
else:
    print(f"\nInvalido")

#Ex 5

pares = impares = 0
for _ in range(10):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")

#Ex 6

intervalo = fora_intervalo = 0
for _ in range(10):
    num = int(input("Digite um número: "))
    if 10 <= num <= 20:
        intervalo += 1
    else:
        fora_intervalo += 1
print(f"Números no intervalo [10, 20]: {intervalo}")
print(f"Números fora do intervalo: {fora_intervalo}")


#Ex 7

soma_pares = 0
contador = 0
for i in range(2, 101, 2):
    soma_pares += i
    contador += 1
    if contador == 50:
        break
print(f"Soma dos 50 primeiros números pares: {soma_pares}")


#Ex 8

numero = int(input("Digite um número positivo: "))
print("Divisores:")
for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)

#Ex 9

numeros = []
for _ in range(10):
    num = int(input("Digite um número inteiro: "))
    numeros.append(num)
numeros.sort()
print("Números em ordem crescente:", numeros)

#Ex 10

lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
repetidos = set()
unicos = set()
for num in lista:
    if num in unicos:
        repetidos.add(num)
    else:
        unicos.add(num)
print("Número que se repete:", repetidos)



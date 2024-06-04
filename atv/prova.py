#1 resultado: 5
"""
a = 20
b = 4
c = 3
soma = 0
if a%b == 0:
    soma+=5 #não funciona
soma += 5
if soma%c == 0 and soma < a:
    soma += 4
else:
    soma -= 4
if soma <= a and soma %2 == 0:
    soma += 5
else:
    soma-=9
if not(soma/2>c) or (True and False):
    soma +=5
else:
    soma -= 5

print(f"o valor de soma é: {soma}")
"""
#2

listaNotas = []
listaAltas = []
listaMedias = []
listabaixas = []
cont = 0
somaA = 0
somaB = 0
somaM = 0
media = 0
alunos = 25

for i in 25:
    listaNotas[i] = int(input("digite  a notas ou um número negativo caso queira interromper o processo: "))
    if listaNotas[i] >= 0 and listaNotas[i] <= 10:
        if listaNotas[i] >= 7:
            
    else:
        break
"""
numeros = [5,7,12,2,9,21]
cont = 0
while cont < len(numeros):
    numeros[1] = 17
    numeros[2] = 1
    numeros[3] = 22
    numeros[4] = 29
    soma=numeros[5] + numeros[4]
    sub=numeros[3] - numeros[1]
    div=numeros[3] / numeros[2]
    mult=numeros[0]*numeros[5]
    print(soma, sub, div, mult)
    print(numeros[cont])
    print(numeros[cont]*2)
    cont+=1


import random

mega = [random.randint(1,6)for _ in range(6)]
aposta = []
cont = 0

while cont < 6:
    numero = input(f"aposte seu numero: ")
    aposta.append(numero)
    cont+=1

print(f"você apostou {aposta} o resultado pe {mega}")


for i in range(0,11):
    if i %2!=0:
        print(f"impar{i}")
    else:
        print(f"par{i}")


letras = ['a','b','c','d','e']

for letra in letras:
    print(letra)
"""
'''
numeros = []

for i in  range(0,11):
    numero = i
    numeros.append(numero)
    print(numero)
    


contador = 1
while contador <=200:
    if contador %4!=0:
        contador+=1
        continue
    else:
        print(contador)
    contador+=1


for i in range(0,201):
    if i%2 != 0:
        print(i)
    else:
        continue
'''
A = 35
B = 7
C = 3
soma = 0
if A%B != 0:
    soma += 10
else:
    
    if (A+B)%C == 0:
        soma += 15
    else:
        soma += 5
if soma%C == 0 and soma < A:
    soma += 4
else:
    soma -= 4
if soma <= A and soma % 2 == 0:
    soma += 5
else:
    soma -= 9
if not(soma/2 > B) or (True and False):
    soma += 5
else:
    soma -= 5
print(f"O valor de soma é: {soma}")
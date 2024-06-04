import cmath
def menu():
    return "escolha sua opção:\n1. Conjuntos numéricos\n2. Funções do segundo grau\n3.Funções exponenciais\n4. Matrizes\n5.Sair "

escolha = int(input(menu()))

def menu1():
    def subconj(A, B):
        return A.issubset(B) #verifica se A é subconj de B

    def uniao(A,B):
        return A | B #faz a uniao

    def inter(A,B):
        return A & B #interssecção
    
    def dif(A,B):
        return A - B #diferença

    A = {1, 2, 3, 4, 5}
    B = {2, 3,5,7,8}
    print(f"a:{A} b:{B}")

    escolha1 = int(input("escolha a opção"))
    if escolha1 == 1:
        print("A é subconjunto de B?",subconj(A, B)) 
    elif escolha1 ==2:
        print("União de A e B é:",uniao(A,B))
    elif escolha1 ==3:
        print("Interssecção de A e B é:",inter(A,B))
    elif escolha1 == 4:
        print("Difereça de A e B é:",dif(A,B))
    elif escolha1 == 5:
        global escolha
        escolha = int(input(menu()))
    else:
        print("invalido tente novamente")
        menu1()

def menu2():
    def raiz(a,b,c):
        delta = a**2 - 4*a*c
        raiz1 = (-b + cmath.sqrt(delta))/(2*a)
        raiz2 = (-b - cmath.sqrt(delta))/(2*a)
        return raiz1, raiz2
    
    def fun(x,a,b,c):
        return a*x**2+b*x+c
    
    def verti(a,b,c):
        x_vertice = -b / (2*a)
        y_vertice = (a*x_vertice**2) + (b*x_vertice) + c
        tipo_vertice = "mínimo" if a > 0 else "máximo"
        return (x_vertice, y_vertice), tipo_vertice
    
    def grafi(a,b,c):
        import matplotlib.pyplot as plt
        import numpy as np

        valorX = []
        for i in range(-10, 11):
            valorX.append(i)

        valorY = []
        for x in valorX:
            y = a * x ** 2 + b * x + c
            valorY.append(y)

        plt.plot(valorX, valorY)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Gráfico da Função do Segundo Grau')
        plt.grid(True)
        plt.show()

    escolha2 = int(input("Escolha a opção: "))
    if escolha2 == 1:
        a = float(input("Digite o coeficiente a: "))
        b = float(input("Digite o coeficiente b: "))
        c = float(input("Digite o coeficiente c: "))
        print("Raízes:", raiz(a, b, c))
    elif escolha2 == 2:
        a = float(input("Digite o coeficiente a: "))
        b = float(input("Digite o coeficiente b: "))
        c = float(input("Digite o coeficiente c: "))
        x = float(input("Digite o valor de x: "))
        print(f"f({x}) =", fun(x, a, b, c))
    elif escolha2 == 3:
        a = float(input("Digite o coeficiente a: "))
        b = float(input("Digite o coeficiente b: "))
        c = float(input("Digite o coeficiente c: "))
        vertice, tipo_vertice = verti(a, b, c)
        print("Vértice:", vertice, "- Tipo:", tipo_vertice)
    elif escolha2 == 4:
        a = float(input("Digite o coeficiente a: "))
        b = float(input("Digite o coeficiente b: "))
        c = float(input("Digite o coeficiente c: "))
        grafi(a, b, c)
    elif escolha2 == 5:
        global escolha
        escolha = int(input(menu()))
    else:
        print("Opção inválida, tente novamente")
        menu2()
    
def menu3():
    def CrDr(a,b):
        return "crescente" if a * b > 0 else "decrescente"
    
    def calcfun(a,b,x):
        return a*b**x
    
    def grafi3(a,b):
        import matplotlib.pyplot as plt
        import numpy as np

        valorX = range(-10, 11)
        valorY = [a * b * x for x in valorX]

        plt.plot(valorX, valorY)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Gráfico da Função Linear')
        plt.grid(True)
        plt.show()

    a = float(input("Digite o coeficiente a: "))
    b = float(input("Digite o coeficiente b: "))

    escolha3 = int(input("Escolha a opção:\n1. Verificar se é crescente ou decrescente\n2. Calcular função em x pedido\n3. Gerar gráfico da função\n4.voltar"))

    if escolha3 == 1:
        print("A função é",CrDr(a,b))
    elif escolha3 == 2:
        x = float(input("Digite o valor de x: "))
        print(f"f({x}) =",calcfun(a,b,x))
    elif escolha3 == 3:
        grafi3(a,b)
    elif escolha3 == 4:
        global escolha
        escolha = int(input(menu()))
    else:
        print("Opção inválida")
        menu3()

def menu4():
    def formMatriz():
        linhas = int(input("Informe o número de linhas da matriz: "))
        colunas = int(input("Informe o número de colunas da matriz: "))
        matriz = []

        print("Informe os elementos da matriz linha por linha:")
        for i in range(linhas):
            linha = []
            for j in range(colunas):
                elemento = float(input(f"Elemento [{i+1},{j+1}]: "))
                linha.append(elemento)
            matriz.append(linha)
        
        return matriz, linhas, colunas

    def imprimir_matriz(matriz):
        for linha in matriz:
            print(linha)

    def verificar_quadrada(matriz, linhas, colunas):
        return linhas == colunas

    def determinante_2x2(matriz):
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    def determinante_3x3(matriz):
        a, b, c = matriz[0]
        d, e, f = matriz[1]
        g, h, i = matriz[2]

        return a * e * i + b * f * g + c * d * h - c * e * g - a * f * h - b * d * i

    def multiplicacao_matrizes(matriz1, linhas1, colunas1, matriz2, linhas2, colunas2):
        if colunas1 != linhas2:
            return "A multiplicação não é possível, número de colunas da primeira matriz não é igual ao número de linhas da segunda matriz."
        
        resultado = []
        for i in range(linhas1):
            linha = []
            for j in range(colunas2):
                elemento = 0
                for k in range(colunas1):
                    elemento += matriz1[i][k] * matriz2[k][j]
                linha.append(elemento)
            resultado.append(linha)
        
        return resultado

    def matriz_transposta(matriz):
        return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

    matriz1, linhas1, colunas1 = formMatriz()
    print("Matriz informada:")
    imprimir_matriz(matriz1)

    opcao = int(input("Escolha uma opção:\n1. Determinante\n2. Multiplicação\n3. Matriz transposta\n"))

    if opcao == 1:
        if verificar_quadrada(matriz1, linhas1, colunas1):
            if linhas1 == 2:
                print("Determinante da matriz:", determinante_2x2(matriz1))
            elif linhas1 == 3:
                print("Determinante da matriz:", determinante_3x3(matriz1))
            else:
                print("Apenas matrizes 2x2 e 3x3 são suportadas para o cálculo do determinante.")
        else:
            print("A matriz não é quadrada, não é possível calcular o determinante.")
    elif opcao == 2:
        matriz2, linhas2, colunas2 = formMatriz()
        print("Matriz informada:")
        imprimir_matriz(matriz2)
        resultado = multiplicacao_matrizes(matriz1, linhas1, colunas1, matriz2, linhas2, colunas2)
        if isinstance(resultado, str):
            print(resultado)
        else:
            print("Resultado da multiplicação:")
            imprimir_matriz(resultado)
    elif opcao == 3:
        print("Matriz transposta:")
        imprimir_matriz(matriz_transposta(matriz1))
    else:
        print("Opção inválida.")
        menu4()


while escolha  != 5:
    if escolha == 1:
        menu1()

    elif escolha == 2:
        menu2()

    elif escolha == 3:
        menu3()

    elif escolha == 4:
        menu4()
    
    else:
        print("invalido, tente novamente")
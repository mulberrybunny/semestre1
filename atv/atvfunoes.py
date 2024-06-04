listacs2 = ['cs',0,0]
listaDota = ['dota',0,0]
listalol = ['lol',0,0]
listavalorant = ['vava',0,0]
while True:
    idade = int(input("sua idade"))
    escolha = int(input("a"))
    if escolha == 1:
        listacs2[1] +=1
        listacs2[2] += idade
    elif escolha == 2:
        listaDota[1] +=1
        listaDota[2] += idade

    elif escolha == 3:
        listalol[1] +=1
        listalol[2] += idade
    elif escolha == 4:
        listavalorant[1] +=1
        listavalorant[2] += idade
    elif escolha == 5:

        print(listacs2)
        print(listalol)
        print(listaDota)
        print(listavalorant)

        break
    else:
        print("invalido")
                    
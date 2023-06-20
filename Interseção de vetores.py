import os

def entrada():
    x = []; y = []
    print("Entre com 10 valores para o vetor X:")
    for i in range(10):
        x.append(int(input()))
    print("Entre com 10 valores para o vetor Y:")
    for i in range(10):
        y.append(int(input()))
    return x, y

def intersec(x, y):
    xy = []
    for i in x:
        for j in y:
            if i == j and i not in xy:
                xy.append(i)
                break
    print(xy)

def check(vet):
    if vet == 0:
        print("Por favor entre com os vetores primeiro.")
        input()
        return True
    else:
        os.system('clear')

def main():
    x = 0
    while True:
        os.system('clear')
        print("1. Entre com os dois vetores de 10 inteiros X e Y.")
        print("2. Mostrar os vetores X e Y.")
        print("3. Mostrar o vetor criado com a intersecção dos vetores X e Y.")
        print("0. Sair")
    
        n = int(input())
        match n:
            case 1:
                os.system('clear')
                x, y = entrada()
            case 2:
                if check(x):
                    continue
                print("X =", x)
                print("Y =", y)
                input()
            case 3:
                if check(x):
                    continue
                intersec(x, y)
                input()
            case 0: break

main() 
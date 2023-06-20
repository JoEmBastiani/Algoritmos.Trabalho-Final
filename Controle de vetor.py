import os

def entrada():
    print("Entre com um vetor de 10 inteiros:")
    vet = []
    for i in range(10):
        vet.append(int(input()))
    return vet

def soma(vet):
    soma = 0
    for i in vet:
        soma += i
    print("A soma dos valores do vetor é", soma)

def bullying(vet):
    n = int(input("Entre com o número a ser comparado:"))
    count = 0
    m = False
    for i in vet:
        if i > n:
            m = True
            print(i, end = ', ')
            count += 1
    if m:
        print("são maiores que %d, um total de %d valores maiores."%(n, count))
    else:
        print("Não há valores maiores que %d."%n)

def mostrar_intervalos(vet):
    print("Do 5º ao 1º:", [vet[i] for i in range(4, -1, -1)])
    print("Do 10º ao 5º:", [vet[i] for i in range(9, 4, -1)])

def check(vet):
    if vet == 0:
        print("Por favor entre com um vetor primeiro.")
        input()
        return True
    else:
        os.system('clear')

def main():
    vet = 0
    while True:
        os.system('clear')
        print("1. Entre com um vetor de 10 inteiros.")
        print("2. Mostrar o vetor.")
        print("3. Mostrar vetor de traz para frente.")
        print("4. Mostrar a soma de todos os valores do vetor.")
        print("5. Informar um número e mostrar apenas os valores maiores e quantos são.")
        print("6. Mostrar o vetor do quinto índice ao primeiro e do décimo ao quinto.")
        print("7. Sair do programa.")
        
        n = int(input())
        match n:
            case 1:
                os.system('clear')
                vet = entrada()
            case 2:
                if check(vet):
                    continue
                print(vet)
                input()
            case 3:
                if check(vet):
                    continue
                print([vet[i] for i in range(-1, -11, -1)])
                input()
            case 4:
                if check(vet):
                    continue
                soma(vet)
                input()
            case 5:
                if check(vet):
                    continue
                bullying(vet)
                input()
            case 6:
                if check(vet):
                    continue
                mostrar_intervalos(vet)
                input()
            case 7: break

main()
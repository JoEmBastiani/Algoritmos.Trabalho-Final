def compress(vet):
    vet2 = []
    pos = 0
    index = 0
    while pos < len(vet):
        vet2.append(0)
        for i in range(pos, len(vet)):
            if vet[i] == 0:
                vet2[index] += 1
            else:
                pos = i
                break
        vet2.append(0)
        for i in range(pos, len(vet)):
            if vet[i] == 1:
                vet2[index] += 1
            else:
                pos = i
                break
    print(vet2)

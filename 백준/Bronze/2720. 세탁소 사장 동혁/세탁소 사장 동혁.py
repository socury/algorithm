for i in range(int(input())):
    li1 = []
    li2 = []
    n = int(input())
    li1.append(n // 25)
    li2.append(n % 25)

    li1.append(li2[-1] // 10)
    li2.append(li2[-1] % 10)

    li1.append(li2[-1] // 5)
    li2.append(li2[-1] % 5)

    li1.append(li2[-1] // 1)
    li2.append(li2[-1] % 1)

    for j in li1:
        print(j, end=' ')
    print()
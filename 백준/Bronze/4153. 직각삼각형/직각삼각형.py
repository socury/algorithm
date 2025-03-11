while 1:
    li = list(map(int, input().split()))

    li.sort()

    if li[0] == 0 or li[1] == 0 or li[2] == 0:
        break

    if li[0]**2 + li[1]**2 == li[2]**2:
        print("right")
    else:
        print("wrong")
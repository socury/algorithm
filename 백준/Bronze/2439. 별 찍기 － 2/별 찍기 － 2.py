n = int(input())
m = n-1
for i in range(1, n+1):
    print(" "*m, end="")
    print("*"*i)
    m -= 1
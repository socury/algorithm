n = int(input())
s = 1
for i in range(n-1, 0, -1):
    print(" "*i, end="")
    print("*"*s)
    s += 2
print("*"*(2*n-1))
s = 2*n-3
for i in range(1, n):
    print(" "*i, end="")
    print("*"*s)
    s -= 2
    
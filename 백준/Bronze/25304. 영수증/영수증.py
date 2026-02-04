x = int(input())
s = 0
for i in range(int(input())):
    n, m = map(int, input().split())
    s += (n*m)
print("Yes" if x == s else "No")
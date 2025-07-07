def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return int(a * b / gcd(a, b))

for i in range(int(input())):
    n, m = map(int, input().split())
    print(lcm(n, m))

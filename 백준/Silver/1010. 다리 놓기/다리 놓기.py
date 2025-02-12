import math
# 고등수학 조합 사용
for i in range(int(input())):
    n, m = map(int, input().split())
    print(math.comb(m, n))
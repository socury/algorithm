result = []
s = input()
for i in range(ord('a'), ord('z')+1):
    result.append(s.find(chr(i)))
print(*result)
s = input().upper()
dict = {}

for i in s:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

max_value = max(dict.values())
max_keys = [k for k, v in dict.items() if v == max_value]

if len(max_keys) == 1:
    print(max_keys[0])
else:
    print("?")
s1 = input()
s2 = input()
p = int(input())
pos = p - 1
result = s1[:pos] + s2 + s1[pos:]
print(result)
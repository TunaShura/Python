s = input().strip()
if s[0] == '-':
    s = s[1:]

count = 0

while len(s) > 1:
    total = sum(int(c) for c in s)
    s = str(total)
    count += 1

print(count)
r = []
for _ in range(10):
    n = int(input())
    r.append(n%42)

s = set(r)
print(len(s))
N, M = map(int, input().split())

ball = [0 for _ in range(N)]

for q in range(1, M+1):
    i, j, k = map(int, input().split())
    for s in range(i-1, j):
        ball[s] = k

print(*ball)
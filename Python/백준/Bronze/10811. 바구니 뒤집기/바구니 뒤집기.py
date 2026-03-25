N, M = map(int, input().split())

ball = [_+1 for _ in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    
    while(i<j):
        ball[j-1], ball[i-1] = ball[i-1], ball[j-1]
        i += 1
        j -= 1

print(*ball)
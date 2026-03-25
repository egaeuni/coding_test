N, M = map(int, input().split())

ball = [_+1 for _ in range(N)]

for _ in range(1, M+1):
    i, j = map(int, input().split())
  
    tempt = ball[i-1]
    ball[i-1]=ball[j-1]
    ball[j-1]=tempt

print(*ball)
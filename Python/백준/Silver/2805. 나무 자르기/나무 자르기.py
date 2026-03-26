import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

low, high = 0, max(trees)

while low <= high:
    mid = (low+high) // 2
    total = 0
  
    for t in trees:
      if t >= mid:
        total += (t - mid)

    if total >= M:
        low = mid + 1
    else:
        high = mid -1

print(high)
def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    unique_topics = len(set(a))
    
    if unique_topics < m:
        print("Yes")
    else:
        print("No")

t = int(input())
for _ in range(t):
    solve()
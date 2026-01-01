# Average Flex solution

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    count = 0
    for x in a:
        le = 0
        for y in a:
            if y <= x:
                le += 1
        if 2 * le > n:
            count += 1
    
    print(count)
# Average Flex solution
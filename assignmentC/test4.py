candies = list(map(int, input().split()))
extra = int(input())
max_candies = max(candies)
for i in range(len(candies)):
    if candies[i] == max_candies:
        print(1)
        continue
    else:
        if candies[i] + extra >= max_candies:
            print(1)
        else:
            print(0)
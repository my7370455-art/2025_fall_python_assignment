# numbers that have nothing to do with 7
def unrelated_to_seven(n) -> int:
    no_related = 0
    for i in range(1, n + 1):
        if '7' not in str(i) and i % 7 != 0:
            no_related += i**2
    return no_related

n = int(input())
print(unrelated_to_seven(n))

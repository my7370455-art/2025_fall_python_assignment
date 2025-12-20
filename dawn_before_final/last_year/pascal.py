code = list(input().strip().split(";"))
code.pop()
lis = [0] * 3
for item in code:
    var, val = item.split(":=")
    if var == "a":
        lis[0] = int(val)
    elif var == "b":
        lis[1] = int(val)
    elif var == "c":
        lis[2] = int(val)

print(" ".join(map(str, lis)))


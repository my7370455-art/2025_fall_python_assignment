num = int(input())
string = bin(num)[2:]
reversed_string = string[::-1]
if reversed_string == string:
    print("Yes")
else:
    print("No")
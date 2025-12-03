def generate_message(message, phone_number) -> bool:
    dict_words = {2: ["a", "b", "c"],
                    3: ["d", "e", "f"],
                    4: ["g", "h", "i"],
                    5: ["j", "k", "l"],
                    6: ["m", "n", "o"],
                    7: ["p", "q", "r", "s"],
                    8: ["t", "u", "v"],
                    9: ["w", "x", "y", "z"]}
    if len(message) != len(phone_number):
        return False
    message = message.lower()
    number_lis = list(phone_number)
    number_lis = [int(i) for i in number_lis]
    if 0 in number_lis or 1 in number_lis:
        return False
    for i in range(len(message)):
        if message[i] in dict_words[number_lis[i]]:
            continue
        else:
            return False
    return True

cases = int(input())
for _ in range(cases):
    msg, num = map(str, input().split())
    if generate_message(msg, num):
        print("Y")
    else:
        print("N")


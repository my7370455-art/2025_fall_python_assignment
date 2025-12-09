from collections import deque

cipher = list(input().strip())
cipher_list = []
alpha_lis = [chr(i) for i in range(ord('a'), ord('z') + 1)]
alpha_lis.remove("j")
for ch in cipher:
    if ch == 'j':
        ch = 'i'
    if ch not in cipher_list:
        cipher_list.append(ch)
for j in alpha_lis:
    if j not in cipher_list:
        cipher_list.append(j)
n = int(input().strip())
for _ in range(n):
    word_lis = deque(input().strip())
    group_lis = []
    while word_lis:
        i = word_lis.popleft()
        if i == 'j':
            i = 'i'
        if word_lis:
            j = word_lis.popleft()
            if j == 'j':
                j = 'i'
            if i == j:
                if i != 'x':
                    group_lis.append(i + 'x')
                    word_lis.appendleft(j)
                else:
                    group_lis.append(i + 'q')
                    word_lis.appendleft(j)
            else:
                group_lis.append(i + j)
        else:
            if i != 'x':
                group_lis.append(i + 'x')
            else:
                group_lis.append(i + 'q')
    output = ""
    for group in group_lis:
        first_index = cipher_list.index(group[0])
        second_index = cipher_list.index(group[1])
        row1 = first_index // 5
        col1 = first_index % 5
        row2 = second_index // 5
        col2 = second_index % 5
        if row1 == row2:
            output += cipher_list[first_index + 1] if col1 != 4 else cipher_list[first_index - 4]
            output += cipher_list[second_index + 1] if col2 != 4 else cipher_list[second_index - 4]
        elif col1 == col2:
            output += cipher_list[first_index + 5] if row1 != 4 else cipher_list[first_index - 20]
            output += cipher_list[second_index + 5] if row2 != 4 else cipher_list[second_index - 20]
        else:
            output += cipher_list[row1 * 5 + col2]
            output += cipher_list[row2 * 5 + col1]
    print(output)
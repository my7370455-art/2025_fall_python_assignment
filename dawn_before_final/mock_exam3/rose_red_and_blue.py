original_string_list = list(input().strip())
string_list = original_string_list.copy()
count = 0
group_number = 1
state = string_list[0]
for i in range(1, len(string_list)):
    if string_list[i] != state:
        if i == len(string_list) - 1:
            if string_list[i] == 'B':
                count += 1
                continue
            state = string_list[i]
            group_number += 1
            continue
        if string_list[i+1] == state:
            count += 1
            continue
        else:
            group_number += 1
            state = string_list[i]
    else:
        continue

if state == 'R':
    count += (group_number - 1)
else:
    count += group_number

print(count)
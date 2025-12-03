def judge_func(str):
    standard = "qwertyuiopasdfghjklzxcvbnm"
    lis = list(standard)
    bucket = []
    chr_set = set(lis)
    for char in str:
        if char in chr_set:
            bucket.append(char)
    length = len(bucket)
    if length == 0:
        return True
    elif length % 2 == 0:
        pointer1 = length // 2 - 1
        pointer2 = length // 2
        while pointer1 >= 0 and pointer2 < length:
            if bucket[pointer1] != bucket[pointer2]:
                return False
            pointer1 -= 1
            pointer2 += 1
        return True
    else:
        left = length // 2 - 1
        right = length // 2 + 1
        while left >= 0 and right < length:
            if bucket[left] != bucket[right]:
                return False
            left -= 1
            right += 1
        return True
    
string = str(input().strip())
if judge_func(string):
    print("True")
else:
    print("False")
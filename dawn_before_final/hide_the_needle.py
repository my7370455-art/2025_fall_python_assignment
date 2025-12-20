def hide_string(s: str, hide: str) -> str:
    s_lis = list(s)
    hide_lis = list(hide)
    pointer = 0
    for char in s_lis:
        try:
            hide_lis.remove(char)
        except ValueError:
            return "Impossible"

    hide_lis.sort()
    ans = []
    for char in s_lis:
        for i in range(len(hide_lis)):
            if hide_lis[i] < char:
                ans.append(hide_lis[i])
                if i == len(hide_lis) - 1:
                    hide_lis = []
            else:
                hide_lis = hide_lis[i:]
                break
        ans.append(char)
    ans.extend(hide_lis)
    return ''.join(ans)

t = int(input().strip())
for _ in range(t):
    s = input().strip()
    hide = input().strip()
    result = hide_string(s, hide)
    print(result)
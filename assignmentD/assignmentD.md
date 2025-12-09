# Assignment #D: Mock Exam 下元节

Updated 1729 GMT+8 Dec 4, 2025

2025 fall, Complied by <mark>苗越 数学科学学院</mark>

> **说明：**
>
> 1.  Dec ⽉考： AC4<mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。
>
> 2.  解题与记录：对于每一个题目，请提供其解题思路（可选），并附上使用 Python 或 C++编写的源代码（确保已在 OpenJudge， Codeforces，LeetCode 等平台上获得 Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用 Typora https://typoraio.cn 进行编辑，当然你也可以选择 Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
> 3.  提交安排：提交时，请首先上传 PDF 格式的文件，并将.md 或.doc 格式的文件作为附件上传至右侧的“作业评论”区。确保你的 Canvas 账户有一个清晰可见的本人头像，提交的文件为 PDF 格式，并且“作业评论”区包含上传的.md 或.doc 附件。
>
> 4.  延迟提交：如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。
>
> 请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。

## 1. 题目

### E29945:神秘数字的宇宙旅行

implementation, http://cs101.openjudge.cn/practice/29945

思路：

代码

```python
n = int(input())
if n == 1:
    print("End")
else:
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            print(f"{n*2}/2={n}")
        else:
            n = 3 * n + 1
            print(f"{(n-1)//3}*3+1={n}")
    print("End")
```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![](https://github.com/my7370455-art/2025_fall_python_assignment/blob/main/assignmentD/images/Screenshot%202025-12-09%20170600.png?raw=true)

### E29946:删数问题

monotonic stack, greedy, http://cs101.openjudge.cn/practice/29946

思路：

代码

```python
def remove_k_digits(num: str, k: int) -> str:
    stack = []
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    final_stack = stack[:-k] if k else stack
    result = ''.join(final_stack).lstrip('0')
    return result if result else '0'

num = str(input().strip())
k = int(input().strip())
print(remove_k_digits(num, k))
```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![](https://github.com/my7370455-art/2025_fall_python_assignment/blob/main/assignmentD/images/Screenshot%202025-12-09%20170600.png?raw=true)

### E30091:缺德的图书馆管理员

greedy, http://cs101.openjudge.cn/practice/30091

思路：

代码

```python
l = int(input())
n = int(input())
stu_lis = list(map(int, input().strip().split()))
max_time = max(max(i, l-i+1) for i in stu_lis)
min_time = max(min(i, l-i+1) for i in stu_lis)
print(min_time, max_time)
```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![](https://github.com/my7370455-art/2025_fall_python_assignment/blob/main/assignmentD/images/Screenshot%202025-12-09%20170600.png?raw=true)

### M27371:Playfair 密码

simulation，string，matrix, http://cs101.openjudge.cn/practice/27371

思路：

代码

```python
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
```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![](https://github.com/my7370455-art/2025_fall_python_assignment/blob/main/assignmentD/images/Screenshot%202025-12-09%20170600.png?raw=true)

### T30201:旅行售货商问题

dp,dfs, http://cs101.openjudge.cn/practice/30201

思路：

代码

```python
def flight_problem(matrix: list):
    n = len(matrix)
    visited = [False] * n
    min_cost = float('inf')

    def dfs(city: int, count: int, cost: int, start_city):
        nonlocal min_cost
        if count == n and matrix[city][0] > 0:
            min_cost = min(min_cost, cost + matrix[city][start_city])
            return
        for next_city in range(n):
            if not visited[next_city]:
                visited[next_city] = True
                dfs(next_city, count + 1, cost + matrix[city][next_city], start_city)
                visited[next_city] = False

    for start_city in range(n):
        visited[start_city] = True
        dfs(start_city, 1, 0, start_city)
        visited[start_city] = False
    return min_cost

n = int(input().strip())
matrix = []
for _ in range(n):
    row = list(map(int, input().strip().split()))
    matrix.append(row)

print(flight_problem(matrix))
```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![](https://github.com/my7370455-art/2025_fall_python_assignment/blob/main/assignmentD/images/Screenshot%202025-12-09%20170629.png?raw=true)

### T30204:小 P 的 LLM 推理加速

greedy, http://cs101.openjudge.cn/practice/30204

思路：

代码

```python
core_num, battery_life = map(int, input().strip().split())
x_list = []
x_y_sum = []
for _ in range(core_num):
    x, y = map(int, input().strip().split())
    x_list.append(x)
    x_y_sum.append(x + y)

x_list.sort()
using_x_y_sum = min(x_y_sum)
max_rounds = 0
for i in range(core_num):
    if x_list[i] >= using_x_y_sum:
        max_rounds = max(max_rounds, rounds)
        break
    current_life = battery_life
    rounds = 0
    for j in range(i):
        if current_life >= x_list[j]:
            current_life -= x_list[j]
            rounds += 1
        else:
            max_rounds = max(max_rounds, rounds)
            break
    if current_life > 0:
        rounds += current_life // using_x_y_sum * 2
        max_rounds = max(max_rounds, rounds)
print(max_rounds)
```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![](https://github.com/my7370455-art/2025_fall_python_assignment/blob/main/assignmentD/images/Screenshot%202025-12-09%20170710.png?raw=true)

## 2. 学习总结和收获

如果作业题目简单，有否额外练习题目，比如：OJ“计概 2025fall 每日选做”、CF、LeetCode、洛谷等网站题目。
practicing some dfs, however this week i didn't write a summary about them. also finish daily assignment problems.

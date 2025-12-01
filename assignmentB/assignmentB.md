# Assignment #B: dp

Updated 1448 GMT+8 Nov 18, 2025

2025 fall, Complied by <mark>苗越 数学学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### LuoguP1255 数楼梯

dp, bfs, https://www.luogu.com.cn/problem/P1255

思路：



代码：

```python
def dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else
        dp_table = [0] * (n + 1)
        dp_table[1] = 1
        dp_table[2] = 2
        for i in range(3, n + 1):
            dp_table[i] = dp_table[i-1] + dp_table[i-2]
        return dp_table[-1]

n = int(input())
print(dp(n))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![](C:\Users\Shu_Pang\Pictures\Screenshots\Screenshot 2025-11-21 142720.png)




### 27528: 跳台阶

dp, http://cs101.openjudge.cn/practice/27528/

思路：
走上n级台阶 每一步可以走的台阶数不定 如何使用dp？
只用1长度来走 加上2长度 这样下去？
或者说每下一个等于之前的总和 这样有没有重复或者漏掉的情况？
漏掉是不会的 重复呢？可以这么说 最后一步的步数是不一样的
代码：

```python
def dp(n):
    dp_table = [0] * (n + 1)
    dp_table[0] = 1
    for i in range(1, n + 1):
        dp_table[i] = sum(dp_table[:i])
    return dp_table[n]

n = int(input())
print(dp(n))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![](C:\Users\Shu_Pang\Pictures\Screenshots\Screenshot 2025-11-21 134353.png)




### M23421:《算法图解》小偷背包问题

dp, http://cs101.openjudge.cn/pctbook/M23421/

思路：
为什么要从后往前遍历呢？因为我们要保证你计算使用的前面项是没有被修改过的。


代码：

```python
def cal_func(n, b,price_lis, weight_lis):
    dp_table = [0] * (b+1)
    for i in range(n):
        current_weight = weight_lis[i]
        current_price = price_lis[i]
        for checking in range(b, current_weight-1, -1):
            dp_table[checking] = max(dp_table[checking],
                                     dp_table[checking - current_weight]
                                     + current_price)
    return dp_table[b]

n, b = map(int, input().split())
price_lis = list(map(int, input().split()))
weight_lis = list(map(int, input().split()))
print(cal_func(n, b, price_lis, weight_lis))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![](C:\Users\Shu_Pang\Pictures\Screenshots\Screenshot 2025-11-21 135152.png)




### M5.最长回文子串

dp, two pointers, string, https://leetcode.cn/problems/longest-palindromic-substring/

思路：
虽然我没看出来双指针为什么是一个中等的内容
当然dp版本的也要尝试一下

代码：

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = []
        for i in range(len(s)):
            solution = [s[i]]
            c1, c2 = i-1, i+1
            while c1 >= 0 and c2 < len(s) and s[c1] == s[c2]:
                solution.append(s[c2])
                solution.insert(0, s[c1])
                c1 -= 1
                c2 += 1
            if len(solution) > len(output):
                output = solution[:]
            
        for j in range(len(s)-1):
            if s[j] == s[j+1]:
                solution = [s[j], s[j+1]]
                c1, c2 = j-1, j+2
                while c1 >= 0 and c2 < len(s) and s[c1] == s[c2]:
                    solution.append(s[c2])
                    solution.insert(0, s[c1])
                    c1 -= 1
                    c2 += 1
                if len(solution) > len(output):
                    output = solution[:]
            else:
                continue
        return "".join(output)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![](C:\Users\Shu_Pang\Pictures\Screenshots\Screenshot 2025-11-21 141102.png)






### 474D. Flowers

dp, 1700 https://codeforces.com/problemset/problem/474/D

思路：
前缀和 直接计算前缀和而非dp表
一次读取很多行

代码：

```python
import sys

def compute_prefix_sum(max_b, k, mod=1000000007):
    """Compute prefix sum using sliding window for DP values.
    Memory: O(max_b) for prefix array + O(k) for DP window = saves O(max_b) vs original."""
    if max_b == 0:
        return [0]
    
    prefix = [0] * (max_b + 1)
    # Circular buffer: store last k+1 DP values
    dp_window = [0] * (k + 1)
    
    # Initialize: dp[i] = 1 for i < k
    for i in range(min(k, max_b + 1)):
        dp_window[i] = 1
        prefix[i] = (prefix[i-1] + 1) % mod if i > 0 else 1
    
    # Compute for i >= k: dp[i] = dp[i-k] + dp[i-1]
    for i in range(k, max_b + 1):
        # Get dp[i-k] and dp[i-1] from circular buffer
        dp_ik = dp_window[(i - k) % (k + 1)]
        dp_i1 = dp_window[(i - 1) % (k + 1)]
        dp_i = (dp_ik + dp_i1) % mod
        
        # Store in circular buffer
        dp_window[i % (k + 1)] = dp_i
        prefix[i] = (prefix[i-1] + dp_i) % mod
    
    return prefix

# Read input
lines = sys.stdin.read().splitlines()
t, k = map(int, lines[0].split())
data = [tuple(map(int, line.split())) for line in lines[1:]]
max_b = max(b for _, b in data)

# Compute prefix sum (optimized: saves ~max_b integers by not storing full DP table)
prefix = compute_prefix_sum(max_b, k)

# Process queries
for a, b in data:
    print((prefix[b] - prefix[a-1]) % 1000000007)    
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![](C:\Users\Shu_Pang\Pictures\Screenshots\Screenshot 2025-11-25 081803.png)




### M198.打家劫舍

dp, https://leetcode.cn/problems/house-robber/

思路：
和小偷背包没什么区别


代码：

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            dp_table = [0] * (len(nums) + 1)
            dp_table[1] = nums[0]
            for i in range(2, len(nums) + 1):
                dp_table[i] = max(dp_table[i-1], dp_table[i-2]+nums[i-1])
            return dp_table[-1]
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![](C:\Users\Shu_Pang\Pictures\Screenshots\Screenshot 2025-11-21 141742.png)




## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>






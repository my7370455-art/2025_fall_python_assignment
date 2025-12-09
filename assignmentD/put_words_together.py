# give you a string and a word dict, determine if the string can be formed by words in the dict
# you can use one word multiple times
def word_break(s: str, word_dict: set) -> bool:
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # empty string can be formed

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break

    return dp[n]
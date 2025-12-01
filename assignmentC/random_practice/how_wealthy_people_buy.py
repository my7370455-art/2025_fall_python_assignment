#Given a sequence of integers, where each number represents the value of a commodity (which can be negative). The rich man's method of buying is 'I will take all the commodities from the nth to the kth!' (n<=k). In other words, the rich man will definitely buy several consecutive commodities. After buying, the rich man will decide based on his mood to put back at most one commodity (he can choose not to return it). However, the rich man cannot return empty-handed; he must take at least one commodity. How much is the maximum total value of the commodities the smart (?) rich man can buy?
#use dp to solve this
#nth isn't necessarily the first item in the sequence, it can be any item in the sequence
"""Given a sequence of integers, where each number represents the value of a commodity (which can be negative). The rich man's method of buying is 'I will take all the commodities from the nth to the kth!' (n<=k). In other words, the rich man will definitely buy several consecutive commodities. After buying, the rich man will decide based on his mood to put back at most one commodity (he can choose not to return it). However, the rich man cannot return empty-handed; he must take at least one commodity. How much is the maximum total value of the commodities the smart (?) rich man can buy?
use dp to solve this
nth isn't necessarily the first item in the sequence, it can be any item in the sequence
"""

def max_wealthy_purchase(sequence):
    n = len(sequence)
    if n == 0:
        return 0

    # Initialize dp arrays
    dp_no_return = [0] * n  # Max sum ending at i without returning any item
    dp_with_return = [float('-inf')] * n  # Max sum ending at i with returning one item

    dp_no_return[0] = sequence[0]

    max_value = sequence[0]

    for i in range(1, n):
        dp_no_return[i] = max(dp_no_return[i - 1] + sequence[i], sequence[i])
        dp_with_return[i] = max(dp_with_return[i - 1] + sequence[i], dp_no_return[i - 1])

        max_value = max(max_value, dp_no_return[i], dp_with_return[i])

    return max_value


if __name__ == '__main__':
    sequence = list(map(int, input().split(",")))
    result = max_wealthy_purchase(sequence)
    print(result)
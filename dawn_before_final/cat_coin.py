import sys

def solve():
    """
    Solves a single test case for the Cat Coin problem.
    """
    try:
        n_str = sys.stdin.readline()
        if not n_str: return
        n = int(n_str)
        coins = list(map(int, sys.stdin.readline().split()))
    except (IOError, ValueError):
        return

    odds = sorted([c for c in coins if c % 2 != 0], reverse=True)
    evens = sorted([c for c in coins if c % 2 == 0], reverse=True)

    # Create prefix sums for quick calculations
    odd_prefix_sum = [0] * (len(odds) + 1)
    for i in range(len(odds)):
        odd_prefix_sum[i + 1] = odd_prefix_sum[i] + odds[i]

    even_prefix_sum = [0] * (len(evens) + 1)
    for i in range(len(evens)):
        even_prefix_sum[i + 1] = even_prefix_sum[i] + evens[i]

    final_scores = []
    # Iterate for each number of actions k from 1 to n
    for k in range(1, n + 1):
        max_score = -1  # Sentinel for no possible odd sum

        # i = number of even coins to take
        for i in range(min(k, len(evens)) + 1):
            # j = number of odd coins to take
            j = k - i

            # To get a non-zero score, we must take an odd number of odd coins.
            # Also, we must have enough odd coins to take.
            if j > len(odds) or j % 2 == 0:
                continue

            current_score = even_prefix_sum[i] + odd_prefix_sum[j]
            if current_score > max_score:
                max_score = current_score
        
        # If no combination results in an odd sum, the score is 0.
        final_scores.append(max_score if max_score != -1 else 0)

    print(' '.join(map(str, final_scores)))

def main():
    """
    Main function to handle multiple test cases.
    """
    try:
        num_test_cases_str = sys.stdin.readline()
        if not num_test_cases_str: return
        num_test_cases = int(num_test_cases_str)
        for _ in range(num_test_cases):
            solve()
    except (IOError, ValueError):
        return

if __name__ == "__main__":
    main()

        


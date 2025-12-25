number_of_stones = int(input())
costs_of_stones = list(map(int, input().split()))
prefix_sums = [0]
for cost in costs_of_stones:
    prefix_sums.append(prefix_sums[-1] + cost)
costs_of_stones.sort()
non_decreasing_prefix_sums = [0]
for cost in costs_of_stones:
    non_decreasing_prefix_sums.append(non_decreasing_prefix_sums[-1] + cost)
number_of_questions = int(input())
for _ in range(number_of_questions):
    question_type, l, r = map(int, input().split())
    if question_type == 1:
        print(prefix_sums[r] - prefix_sums[l - 1])
    else:
        print(non_decreasing_prefix_sums[r] - non_decreasing_prefix_sums[l - 1])
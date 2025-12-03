"""Given a numeric string, insert the operators +, - and * between digits
(or join digits) to form expressions that evaluate to the target value.

This module provides `count_expressions(num_str, target)` which returns
the number of distinct expressions that evaluate to `target`.

Example:
	num_str = "123", target = 6 -> 2 ways: "1+2+3" and "1*2*3"
"""

from typing import List


def count_expressions(num_str: str, target: int) -> int:
	"""Return the number of ways to insert +, -, * to get `target`.

	Args:
		num_str: string consisting of digits '0'-'9'.
		target: integer target value.

	Returns:
		Integer count of distinct valid expressions.
	"""

	n = len(num_str)
	if n == 0:
		return 0

	count = 0

	def dfs(index: int, current_value: int, last_operand: int) -> None:
		nonlocal count
		if index == n:
			if current_value == target:
				count += 1
			return

		# Try all possible next numbers by extending the substring
		for i in range(index, n):
			# Avoid numbers with leading zeros (like "05") except single '0'
			if i > index and num_str[index] == '0':
				break
			part = num_str[index : i + 1]
			operand = int(part)

			if index == 0:
				# First number in the expression — it sets the running value
				dfs(i + 1, operand, operand)
			else:
				# '+' operator
				dfs(i + 1, current_value + operand, operand)
				# '-' operator
				dfs(i + 1, current_value - operand, -operand)
				# '*' operator: undo last_operand and apply multiplication
				dfs(i + 1, current_value - last_operand + last_operand * operand, last_operand * operand)

	dfs(0, 0, 0)
	return count

string = str(input().strip())
target = int(input().strip())
result = count_expressions(string, target)
print(result)
# this time we repeat test 9 using dfs and backtracking
def calcu_methods(string : str, target : int) -> int:
    '''please be merciful on test case since you give no restraint on it'''
    # start dfs in no time
    count = 0
    n = len(string)
    def dfs(index, current_value, last_operand):
        nonlocal count
        if index == n:
            if current_value == target:
                count += 1
            return
        else:
            for i in range(index, n):
                if i > index and string[index] == "0":
                    break
                else:
                    part = string[index:i+1]
                    operand = int(part)
                
                if index == 0:
                    dfs(i+1, operand, operand)
                else:
                    # +
                    dfs(i+1, current_value + operand, operand)
                    # -
                    dfs(i+1, current_value - operand, -operand)
                    # *
                    dfs(i+1, current_value - last_operand + last_operand * operand, last_operand * operand)
    dfs(0, 0, 0)
    return count
string = str(input().strip())
target = int(input().strip())
result = calcu_methods(string, target)
print(result)
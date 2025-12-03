# find the longest mutual prefix in a str sequence
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

n = int(input().strip())
sequence = list(map(str, input().strip().split()))
print(longest_common_prefix(sequence))
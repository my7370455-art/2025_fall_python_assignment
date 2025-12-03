# give you a sequence, find the subsequence with the largest multiplicative sum and return the sum
# dp required
# the start point don't need to be the first element
def max_product_subsequence(seq):
    if not seq:
        return 0

    n = len(seq)
    max_product = [0] * n
    min_product = [0] * n

    max_product[0] = seq[0]
    min_product[0] = seq[0]
    result = seq[0]

    for i in range(1, n):
        if seq[i] > 0:
            max_product[i] = max(seq[i], max_product[i - 1] * seq[i])
            min_product[i] = min(seq[i], min_product[i - 1] * seq[i])
        else:
            max_product[i] = max(seq[i], min_product[i - 1] * seq[i])
            min_product[i] = min(seq[i], max_product[i - 1] * seq[i])

        result = max(result, max_product[i])

    return result

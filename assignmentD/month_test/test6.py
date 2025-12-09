# give you a bunch of NPU cores with different battery usage levels,
# for one core, the battery usage level is represented by two integers a, b, in a periodic task, which means it will firstly
# use a units of battery to perform one task, then it will use b units of battery to perform the next task, and then it will repeat this process.
# now you have a total battery capacity of C units, you want to know the maximum number of tasks you can perform using these cores without exceeding the battery capacity.
# each core can be used multiple times, and you can switch between cores at any time, including in the middle of a core's periodic task.
import sys

def max_tasks(cores, m):
    # cores: list of (x, y) pairs, m: total energy
    n = len(cores)
    xs = [x for x, y in cores]
    pair_costs = [x + y for x, y in cores]

    xs_sorted = sorted(xs)
    pref = [0]  # prefix sums: pref[k] = sum of k smallest x
    for v in xs_sorted:
        pref.append(pref[-1] + v)

    min_pair = min(pair_costs)
    min_task_cost = min(min(xs), min(y for x, y in cores))

    # upper bound for tasks: each task至少消耗 min_task_cost
    lo, hi = 0, m // min_task_cost
    ans = 0

    def feasible(T):
        # return True if can finish T tasks within energy m
        # S ranges from parity = T%2 to min(n, T), step 2
        maxS = min(n, T)
        parity = T & 1
        best = 10**30
        # enumerate S with same parity as T
        for S in range(parity, maxS + 1, 2):
            P = (T - S) // 2
            cost = P * min_pair + pref[S]
            if cost < best:
                best = cost
                # small pruning: if best already <= m we can return True
                if best <= m:
                    return True
        return best <= m

    # binary search maximum T
    while lo <= hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return ans

if __name__ == "__main__":
    # 读入 (与题目输入格式相符)
    data = sys.stdin.read().strip().split()
    it = iter(data)
    try:
        n = int(next(it))
        m = int(next(it))
    except StopIteration:
        print(0)
        sys.exit(0)
    cores = []
    for _ in range(n):
        x = int(next(it)); y = int(next(it))
        cores.append((x, y))
    print(max_tasks(cores, m))
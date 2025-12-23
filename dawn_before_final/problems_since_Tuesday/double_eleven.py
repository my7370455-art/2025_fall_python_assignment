import sys

# Increase recursion depth just in case, though n is small
sys.setrecursionlimit(2000)

def solve():
    # Read n and m
    line = sys.stdin.readline()
    while line and not line.strip(): # Skip empty leading lines if any
        line = sys.stdin.readline()
    
    if not line:
        return
        
    try:
        n, m = map(int, line.split())
    except ValueError:
        return

    # Read items
    items = []
    for _ in range(n):
        line = sys.stdin.readline().strip()
        parts = line.split()
        item_options = []
        for part in parts:
            if ':' in part:
                shop_str, price_str = part.split(':')
                item_options.append((int(shop_str), int(price_str)))
        items.append(item_options)

    # Read coupons
    # coupons[shop_id] = list of (q, x)
    coupons = {}
    for i in range(1, m + 1):
        line = sys.stdin.readline().strip()
        shop_coupons = []
        if line:
            parts = line.split()
            for part in parts:
                if '-' in part:
                    q_str, x_str = part.split('-')
                    shop_coupons.append((int(q_str), int(x_str)))
        coupons[i] = shop_coupons

    min_total_cost = float('inf')
    
    # shop_totals[i] stores the total price of items selected from shop i
    shop_totals = [0] * (m + 1)

    def dfs(item_idx):
        nonlocal min_total_cost
        
        if item_idx == n:
            # Calculate final cost
            total_marked_price = sum(shop_totals)
            
            # 1. Cross-shop discount
            # "每满300，可以减去50"
            cross_shop_discount = (total_marked_price // 300) * 50
            
            # 2. Shop coupons
            shop_discounts = 0
            for s in range(1, m + 1):
                current_shop_total = shop_totals[s]
                best_coupon_cut = 0
                for q, x in coupons[s]:
                    if current_shop_total >= q:
                        if x > best_coupon_cut:
                            best_coupon_cut = x
                shop_discounts += best_coupon_cut
            
            final_cost = total_marked_price - cross_shop_discount - shop_discounts
            
            if final_cost < min_total_cost:
                min_total_cost = final_cost
            return

        # Try buying current item from each available shop
        for shop_id, price in items[item_idx]:
            shop_totals[shop_id] += price
            dfs(item_idx + 1)
            shop_totals[shop_id] -= price # Backtrack

    dfs(0)
    print(min_total_cost)

if __name__ == '__main__':
    solve()

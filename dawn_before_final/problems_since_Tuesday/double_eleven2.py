n, m = map(int, input().split())
commodity_infos = [[] for _ in range(n)]
coupon_infos = [[] for _ in range(m)]
for j in range(n):
    information = input().split()
    for i in information:
        shop_id, price = map(int, i.split(':'))
        commodity_infos[j].append((shop_id - 1, price))
for j in range(m):
    coupon_info = input().split()
    for coupon in coupon_info:
        q, x = map(int, coupon.split('-'))
        coupon_infos[j].append((q, x))

total_min_cost = float('inf')
cost_list_for_each_shop = [0] * m
def dfs(item_index):
    global total_min_cost
    if item_index == n:
        total_price = sum(cost_list_for_each_shop)
        cross_shop_discount = (total_price // 300) * 50
        shop_discount = 0
        for shop_index in range(m):
            current_shop_total = cost_list_for_each_shop[shop_index]
            best_coupon_cut = 0
            for q, x in coupon_infos[shop_index]:
                if current_shop_total >= q:
                    if x > best_coupon_cut:
                        best_coupon_cut = x
            shop_discount += best_coupon_cut
        final_price = total_price - cross_shop_discount - shop_discount
        if final_price < total_min_cost:
            total_min_cost = final_price
        return
    for shop_index in range(m):
        for shop_id, price in commodity_infos[item_index]:
            if shop_id == shop_index:
                cost_list_for_each_shop[shop_index] += price
                dfs(item_index + 1)
                cost_list_for_each_shop[shop_index] -= price

dfs(0)
print(total_min_cost)
    
'''2 2
1:100 2:120
1:300 2:350
200-30 400-70
100-80'''
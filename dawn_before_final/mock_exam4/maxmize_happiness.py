plan_number = int(input())
for _ in range(plan_number):
    start_date, end_date, happiness = map(str, input().split())
    if float(end_date) > 2.20:
        continue
    if ha
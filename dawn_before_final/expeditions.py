import heapq

num_of_fuel_stations = int(input().strip())
fuel_stations_inf = []
for _ in range(num_of_fuel_stations):
    position, fuel = map(int, input().strip().split())
    fuel_stations_inf.append((position, -fuel))

fuel_stations_inf.sort(reverse = True)
distance, total_fuel = map(int, input().strip().split())
pointer = 0
reachable_stations = []
count = 0
while True:
    while pointer < num_of_fuel_stations and distance - fuel_stations_inf[pointer][0] <= total_fuel:
        heapq.heappush(reachable_stations, fuel_stations_inf[pointer][1])
        pointer += 1
    if total_fuel < distance:
        if not reachable_stations:
            count = -1
            break
        total_fuel += -heapq.heappop(reachable_stations)
        count += 1
    else:
        break
print(count)
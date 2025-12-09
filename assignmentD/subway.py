# give you coordinates of your home and school, you walk at a speed of 10km per hour, one unit stands for 1m.
# you can take subway at certain stations, subway speed is 40km per hour.
# given the coordinates of subway stations, find the shortest time to get to school.
# you can switch between walking and subway at any subway station.
# there are different subway lines, stations will be given resp
import math
from typing import List, Tuple
def calculate_time(distance: float, speed_kmh: float) -> float:
    speed_mps = speed_kmh * 1000 / 3600  # convert km/h to m/s
    return distance / speed_mps
def shortest_time(home: Tuple[int, int], school: Tuple[int, int], stations: List[Tuple[int, int]]) -> float:
    points = [home] + stations + [school]
    n = len(points)
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distance = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
                walk_time = calculate_time(distance, 10)
                subway_time = calculate_time(distance, 40)
                dist[i][j] = min(walk_time, subway_time) if i != 0 and j != n - 1 else walk_time
    dp = [float('inf')] * n
    dp[0] = 0
    for i in range(n):
        for j in range(i + 1, n):
            dp[j] = min(dp[j], dp[i] + dist[i][j])
    return dp[-1]
home_x, home_y = map(int, input().strip().split())
school_x, school_y = map(int, input().strip().split())
num_stations = int(input().strip())
stations = []
for _ in range(num_stations):
    station_x, station_y = map(int, input().strip().split())
    stations.append((station_x, station_y))

result = shortest_time((home_x, home_y), (school_x, school_y), stations)
print(round(result, 6))
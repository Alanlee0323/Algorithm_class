def min_overtime(n, d, r, morning_routes, evening_routes):
    # 對路線長度排序
    morning_routes.sort()
    evening_routes.sort(reverse=True)  # 晚班車路線反向排序

    overtime_cost = 0

    # 將最短早班車路線與最長晚班車路線配對分配給每位司機
    for i in range(n):
        total_route_length = morning_routes[i] + evening_routes[i]
        if total_route_length > d:
            overtime_cost += (total_route_length - d) * r

    return overtime_cost

results = []

while True:
    n, d, r = map(int, input().split())
    if n == 0 and d == 0 and r == 0:
        break
    morning_routes = list(map(int, input().split()))
    evening_routes = list(map(int, input().split()))
    result = min_overtime(n, d, r, morning_routes, evening_routes)
    results.append(result)

for result in results:
    print(result)
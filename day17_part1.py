sizes = []
target = 150
with open("day17.txt") as file:
    for size in file.readlines():
        sizes.append(int(size.strip()))

def min_containers_and_ways(sizes, target):
    min_containers = [float('inf')] * (target + 1)
    min_containers[0] = 0
    dp = [0] * (target + 1)
    dp[0] = 1
    for size in sizes:
        for i in range(size, target + 1):
            if min_containers[i - size] + 1 < min_containers[i]:
                min_containers[i] = min_containers[i - size] + 1
                dp[i] = dp[i - size]
            elif min_containers[i - size] + 1 == min_containers[i]:
                dp[i] += dp[i - size]
    return min_containers[target], dp[target]

min_containers, ways = min_containers_and_ways(sizes, target)
print(f"Minimum number of containers: {min_containers}")
print(f"Number of ways to fill that number of containers: {ways}")

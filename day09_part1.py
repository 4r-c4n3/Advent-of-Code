from itertools import permutations

with open("2015_day9.txt") as file:
    distances = {}

    for line in file.readlines():
        parts = line.split(" ")
        a = parts[0]
        b = parts[2]
        cost = int(parts[4])
        distances[(a, b)] = cost
        distances[(b, a)] = cost  


def calculate_total_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances[(route[i], route[i + 1])]
    return total_distance


def find_shortest_route():
    locations = set(location for pair in distances.keys() for location in pair)
    shortest_distance = float('inf')
    shortest_route = None

    for route in permutations(locations):
        current_distance = calculate_total_distance(route)
        if current_distance < shortest_distance:
            shortest_distance = current_distance
            shortest_route = route

    return shortest_route, shortest_distance


if __name__ == "__main__":
    shortest_route, shortest_distance = find_shortest_route()

    print(f"The shortest distance is {shortest_distance}.")

from itertools import permutations

with open("2015_day9.txt") as file:
    distances = {}

    for line in file.readlines():
        parts = line.split(" ")
        a = parts[0]
        b = parts[2]
        cost = int(parts[4])
        distances[(a, b)] = cost
        distances[(b, a)] = cost  # Assuming distances are symmetric


def calculate_total_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances[(route[i], route[i + 1])]
    return total_distance


def find_longest_route():
    locations = set(location for pair in distances.keys() for location in pair)
    longest_distance = float('-inf')
    longest_route = None

    for route in permutations(locations):
        current_distance = calculate_total_distance(route)
        if current_distance > longest_distance:
            longest_distance = current_distance
            longest_route = route

    return longest_route, longest_distance


if __name__ == "__main__":
    longest_route, longest_distance = find_longest_route()

    print(f"The longest route is {longest_route} with a total distance of {longest_distance}.")

def sum_signed_integers(data):
    if isinstance(data, list):
        return sum(sum_signed_integers(item) for item in data)

    elif isinstance(data, dict):
        if "red" in data.values():
            return 0
        return sum(sum_signed_integers(value) for value in data.values())

    elif isinstance(data, int):
        return data

    return 0

with open("day12.txt") as file:
    text = file.read()

import json
input_data = json.loads(text)

result_sum = sum_signed_integers(input_data)

print(result_sum)

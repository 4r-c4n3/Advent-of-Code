data = []
cookie = {}
with open("day15.txt") as file:
	for line in file.readlines():
		score = 0
		chunks = line.split()
		cookie['name'] = chunks[0].rstrip(":")
		for i in range(0,10,2):
			cookie[chunks[i+1]] = int(chunks[i+2].rstrip(","))
		data.append(cookie)
		cookie = {}

target_sum = 100
result = []
total_score = []
for num1 in range(target_sum + 1):
    for num2 in range(target_sum - num1 + 1):
        for num3 in range(target_sum - num1 - num2 + 1):
            num4 = target_sum - num1 - num2 - num3
            if num4 >= 0:
                result.append([num1, num2, num3, num4])
for i in result:
	TS = i
	C = (data[0]["capacity"] * TS[0]) + (data[1]["capacity"] * TS[1]) +(data[2]["capacity"] * TS[2]) +(data[3]["capacity"] * TS[3]) 
	D = (data[0]["durability"] * TS[0]) + (data[1]["durability"] * TS[1]) +(data[2]["durability"] * TS[2]) +(data[3]["durability"] * TS[3]) 
	F = (data[0]["flavor"] * TS[0]) + (data[1]["flavor"] * TS[1]) +(data[2]["flavor"] * TS[2]) +(data[3]["flavor"] * TS[3]) 
	T = (data[0]["texture"] * TS[0]) + (data[1]["texture"] * TS[1]) +(data[2]["texture"] * TS[2]) +(data[3]["texture"] * TS[3]) 

	if C < 0 or D < 0 or F < 0 or T < 0 :
		score = 0
	else:
		score = C * D * F * T
	if score != 0:
		total_score.append(score) 
print(max(total_score))
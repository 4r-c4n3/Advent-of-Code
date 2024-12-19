data = []
target = {"children": 3,"cats": 7,"samoyeds": 2,"pomeranians": 3,"akitas": 0,"vizslas": 0,"goldfish": 5,"trees": 3,"cars": 2,"perfumes": 1}
sue= {}
with open("day16.txt") as file:
	for line in file.readlines():
		chunks = line.split()
		sue[chunks[2][:-1]] = int(chunks[3][:-1])
		sue[chunks[4][:-1]] = int(chunks[5][:-1])
		sue[chunks[6][:-1]] = int(chunks[7])
		data.append(sue)
		if sue[chunks[2][:-1]] == target[chunks[2][:-1]] and sue[chunks[4][:-1]] == target[chunks[4][:-1]] and sue[chunks[6][:-1]] == target[chunks[6][:-1]]:
			print(chunks[0] + chunks[1])
		sue = {}


	
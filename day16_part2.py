target = {"children": 3,"cats": 7,"samoyeds": 2,"pomeranians": 3,"akitas": 0,"vizslas": 0,"goldfish": 5,"trees": 3,"cars": 2,"perfumes": 1}
up = ["cats","trees"]
down = ["pomeranians","goldfish"]
sue= {}
with open("day16.txt") as file:
	for line in file.readlines():
		chunks = line.split()
		one = two = three = False
		sue[chunks[2][:-1]] = int(chunks[3][:-1])
		sue[chunks[4][:-1]] = int(chunks[5][:-1])
		sue[chunks[6][:-1]] = int(chunks[7])
		if chunks[2][:-1] in up and sue[chunks[2][:-1]] >= target[chunks[2][:-1]]:
			one = True
		elif chunks[2][:-1] in down and sue[chunks[2][:-1]] <= target[chunks[2][:-1]]:
			one = True
		elif sue[chunks[2][:-1]] == target[chunks[2][:-1]]:
			one = True
		if chunks[4][:-1] in up and sue[chunks[4][:-1]] >= target[chunks[4][:-1]]:
			two = True
		elif chunks[4][:-1] in down and sue[chunks[4][:-1]] <= target[chunks[4][:-1]]:
			two = True
		elif sue[chunks[4][:-1]] == target[chunks[4][:-1]]:
			two = True
		if chunks[6][:-1] in up and sue[chunks[6][:-1]] >= target[chunks[6][:-1]]:
			three = True
		elif chunks[6][:-1] in down and sue[chunks[6][:-1]] <= target[chunks[6][:-1]]:
			three = True
		elif sue[chunks[6][:-1]] == target[chunks[6][:-1]]:
			three = True
		if one and two and three:
			print(chunks[0] ,chunks[1])
		sue = {}


	
rows = 1000
cols = 1000
lights = [[0 for i in range(rows)] for j in range(cols)]
with open("day6.txt") as file:
	for line in file.readlines():
		chunks = line.split()
		if chunks[0] + chunks[1] == "turnon" :
			start = chunks[2].split(",")
			end = chunks[4].split(",")
			for i in range(int(start[0])-1,int(end[0])):
				for j in range(int(start[1])-1,int(end[1])):
					lights[i][j] += 1

		elif chunks[0] + chunks[1] == "turnoff" :
			start = chunks[2].split(",")
			end = chunks[4].split(",")
			for i in range(int(start[0])-1,int(end[0])):
				for j in range(int(start[1])-1,int(end[1])):
					if lights[i][j] >=1: 
						lights[i][j] -= 1

		elif chunks[0] == "toggle" :
			start = chunks[1].split(",")
			end = chunks[3].split(",")
			for i in range(int(start[0])-1,int(end[0])):
				for j in range(int(start[1])-1,int(end[1])):
						lights[i][j] = lights[i][j] + 2
					
count = 0
for i in range(0,rows):
	for j in range(0,cols):
		count = count + lights[i][j]
print(count)
reindeers = {}
respective_distance = []
distance = 0
seconds = 0
race_time = 2503
with open('day14.txt') as file:
	for line in file.readlines():
		chunks = line.split()
		reindeers[chunks[0]] = 0
		speed , time , rest =int(chunks[3]) , int(chunks[6]) , int(chunks[13])
		while True:
			if seconds >=race_time:
				break
			distance = distance + (speed * time)
			seconds = seconds + time
			if seconds >=race_time:
				distance = distance - ((seconds - race_time) * speed)
				break 
			seconds = seconds + rest
		reindeers[chunks[0]] =  distance
		distance = seconds = 0
print(max(list(reindeers.values())))
print(reindeers)

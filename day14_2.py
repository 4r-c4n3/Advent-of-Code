reindeers = {'Vixen': 0, 'Blitzen': 0, 'Rudolph': 0, 'Cupid': 0, 'Donner': 0, 'Dasher': 0, 'Comet': 0, 'Prancer': 0, 'Dancer': 0}
travelling = {'Vixen': True, 'Blitzen': True, 'Rudolph': True, 'Cupid': True, 'Donner': True, 'Dasher': True, 'Comet': True, 'Prancer': True, 'Dancer': True}
stop = {'Vixen': False, 'Blitzen': False, 'Rudolph': False, 'Cupid': False, 'Donner': False, 'Dasher': False, 'Comet': False, 'Prancer': False, 'Dancer': False}
seconds = {'Vixen': 0, 'Blitzen': 0, 'Rudolph': 0, 'Cupid': 0, 'Donner': 0, 'Dasher': 0, 'Comet': 0, 'Prancer': 0, 'Dancer': 0}
rewards = {'Vixen': 0, 'Blitzen': 0, 'Rudolph': 0, 'Cupid': 0, 'Donner': 0, 'Dasher': 0, 'Comet': 0, 'Prancer': 0, 'Dancer': 0}

with open('day14.txt') as file:
    lines = file.readlines()

for i in range(0, 2053):
    for line in lines:
        chunks = line.split()
        speed, time, rest = int(chunks[3]), int(chunks[6]), int(chunks[13])

        if travelling[chunks[0]]:
            if seconds[chunks[0]] == time:
                stop[chunks[0]] = True
                travelling[chunks[0]] = False
                seconds[chunks[0]] = 0
            reindeers[chunks[0]] += speed  

        if stop[chunks[0]]:
            if seconds[chunks[0]] == rest:
                travelling[chunks[0]] = True
                stop[chunks[0]] = False    
                seconds[chunks[0]] = 0

        seconds[chunks[0]] += 1

max_distance = max(reindeers.values())

for reindeer, distance in reindeers.items():
    if distance == max_distance:
        rewards[reindeer] += 1

print(reindeers)

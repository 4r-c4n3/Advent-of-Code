out = ""
sum = 0
with open("day12.txt") as file:
	line = file.readline()
	for i in line:
		if i.isdigit() or i == '-':
			out=out+str(i)
		else:
			out=out+" "
nums = out.split()
for i in nums:
	sum = sum + int(i)
print(sum)
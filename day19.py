with open("day19.txt") as file:
	for line in file.readlines():
		try:
			one , two = line.split("=>")
			print(one,two,)
		except:
			last_line = line 
			print(last_line)

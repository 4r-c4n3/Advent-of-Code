#make a dicttionary of all couples and their happiness...initialize happiness as 0.

name = ['Bob','Carol','David','Eric','Frank','George','Mallory','Alice']
dict = {}
var = ''
total_happpiness = 0
for i in name:
	for j in name:
		if i != j:
			var = i + '_' + j
			if var not in dict :
				dict[var] = 0


#reading data and adding happiness to dictionary.

with open('day13.txt') as file:
	for line in file:
		blocks = line.split()
		who , what ,how_much ,with_who =blocks[0],blocks[2],int(blocks[3]),blocks[10]
		pair = blocks[0] + '_' + blocks[10].strip(".")
		if what == 'gain':
			dict[pair] += how_much
		elif what == 'lose' :
			dict[pair] -= how_much

#addind happiness of symetric(repeating) couples like AB and BA ...

sets = list(dict.keys())
for i in sets:
	ready = i.split("_")
	go = ready[1] + "_" + ready[0]
	if go in sets :
		dict[i] += dict[go]
		del dict[go]
		sets.remove(go)

#getting couples with max happiness,also making sure one person should make bond with only two ...
#i.e circular table 

sitting = {'Bob':0,'Carol':0,'David':0,'Eric':0,'Frank':0,'George':0,'Mallory':0,'Alice':0}
couple = [""]* 8
happiness = [0] * 8
count = 0
for i in range(0,len(dict)):
	a =  [k for k, v in dict.items() if v == max(dict.values())]
	person = a[0].split("_")
	a = ""
	if sitting[person[0]] >= 2 or sitting[person[1]] >= 2 :
		del dict[person[0]+"_"+person[1]]
		continue
	couple[count] = max(dict, key= lambda x: dict[x])
	last = (couple[count]).split("_")[1]
	happiness[count] = max(dict.values())
	sitting[person[0]] += 1
	sitting[person[1]] += 1
	del dict[max(dict, key= lambda x: dict[x])]
	count += 1;
	if count == 8:
		break		

#calculating optimal happiness

total_happpiness = 0
for i in happiness:
	total_happpiness = total_happpiness + i

#(*_*)

print(couple)
print(happiness)
print(total_happpiness)

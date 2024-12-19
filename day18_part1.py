rows = 100
cols = 100
next_state = [['0'] * rows for _ in range(cols)]
initial_matrix = []
row = []

# creating given state
with open("day18.txt") as file:
    for line in file.readlines():
        row = []
        for letters in line:
            if letters == '.' or letters == '#':
                row.append(letters)
        initial_matrix.append(row)


#getting next state
def get_next(matrix):
    next_state = [['0'] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            on = 0
            for c in range(i - 1, i + 2):
                for d in range(j - 1, j + 2):
                    if 0 <= c < rows and 0 <= d < cols:
                        if matrix[c][d] == '#':
                            on += 1

            if matrix[i][j] == '#':
                on -= 1
                if on == 2 or on == 3:
                    next_state[i][j] = '#'
                else:
                    next_state[i][j] = '.'
            elif matrix[i][j] == '.':
                if on == 3:
                    next_state[i][j] = '#'
                else:
                    next_state[i][j] = '.'
    return next_state



# Getting state after 100 animations
old_state = initial_matrix
for _ in range(100):
    new_state = get_next(old_state)
    old_state = new_state

final_state = old_state
count = 0
for i in range(rows):
	for j in range(cols):
		if final_state[i][j]== '#':
			count += 1
print(count)

#getting no of on lights in final state

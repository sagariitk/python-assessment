

list1 = [[0 for i in xrange(3)] for i in xrange(3)]

for i in range(3):
	for j in range(3):
		x = int(input("Enter size of list: "))
		list1[i][j] = x

for i in range(3):
	index_a = i
	for j in range(3):
		index_b = j
		print(list1[i][j])
	for j in range(index_b):
		
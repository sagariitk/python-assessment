size_list1 = int(input("Enter size of list: "))
list1 = []
for i in range(size_list1):
	
	print("Input the tuple: ")

	numbers = raw_input()

	x = tuple(map(int, numbers.split()))
	list1.append(x)

print sorted(list1, key=lambda num:num[-1])

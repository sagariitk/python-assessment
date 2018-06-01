

def check_seq(list1):
	for i in range(0,len(list1)-3):
		if((list1[i] +list1[i+1]) != list1[i+2]):
			return False
	return True
print("Input the list: ")

numbers = raw_input()

list1 = list(map(int, numbers.split()))

abc = True
abc = check_seq(list1)

if abc ==True:
	print("In Sequence")

else:
	print("Not in Sequence")
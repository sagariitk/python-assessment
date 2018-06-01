# #binary search function

# def binary_search(list, left, right, key):
# 	mid = (left+right)/2

# #returning -1 because no key was found in the
	
# 	if(key == list[mid]):
# 		print(mid)
# 		return
# 	elif(key>list[mid]):
# 		left = mid+1
# 		binary_search(list, left, right, key)
# 	else:
# 		right = mid-1
# 		binary_search(list, left, right, key)


# list = [1,2,3,4,5,6,7,8,9,10]
# left =0
# right = len(list)-1
# key = raw_input()

# binary_search(list,left,right,key)


#binary search function

def binary_search(list1, left, right, key):
	
	mid = (left+right)/2

	if(left == right):
		print("Index is: -1")
		return

	if(key == list1[mid]):
		print("index is: %d" %mid)
		return
	elif(key > list1[mid]):
		left = mid+1
		binary_search(list1, left, right, key)
	else:
		right = mid-1
		binary_search(list1, left, right, key)


print("Input the list: ")

numbers = raw_input()

list1 = list(map(int, numbers.split()))

key = int(input("Enter a number: "))
left =0
right = len(list1)-1

binary_search(list1, left, right, key)
#first question to validate the password

#validate method for checking password conditions
def validate(pas):
	count = [0,0,0,0];
	for i in range(len(pas)):
		if(pas[i]>='A' and pas[i]<='Z'):
			count[0] += 1
		elif(pas[i]>='a' and pas[i]<='z'):
			count[1] += 1
		elif(pas[i]>='0' and pas[i]<='9'):
			count[2] += 1
		elif(pas[i] == '$'):
			count[3] += 1
		elif(pas[i] == '#'):
			count[3] += 1
		elif(pas[i] == '@'):
			count[3] += 1

	for i in range(len(count)):
		if(count[i] == 0):
			print("Invalid Password")
			return
	print("Valid Password")
	return

#takes password as input

def main():
	print("Input your password: ")
	pas = raw_input()


	#checking the condition of length of password 
	if(len(pas)<6 or len(pas)>12):
		print("Invalid password")

	#checking other conditions of password validation
	else:
		validate(pas)

if __name__ == '__main__':
    main()

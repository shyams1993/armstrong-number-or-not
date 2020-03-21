num=input("Enter a number: ")									#Get Input from the user (note: stored as string)
val=list(num) 													#convert input received to a list
for i in range(0, len(val)): 									#since list is stored as string, create a for loop to convert each number in list to int
    val[i] = int(val[i])
length=len(val)													#create a variable length that stores length of input, to act as counter
result=0														#Initialize result to 0
if (length == 3):												#for 3 digit armstrong numbers (if length = 3)
	for i in range(length):										#create a for loop that loops within the length
		result= result+(val[i]*val[i]*val[i])					#cubing of each digit inside the list
results = str(result)											#convert the answer back to string so it matches with the input user gave
if (length == 4):												#repeat the same logic for 4 digit numbers
	for i in range(length):
		result= result+(val[i]*val[i]*val[i]*val[i])
results = str(result)
if (num == results):											#if the calculated result equals user input, then armstrong number	
	print(num+" is an ArmStrong Number")						
else:
	print(num+" is not an ArmStrong Number")					#else, not an armstrong number

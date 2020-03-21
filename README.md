# armstrong-number-or-not
Python program to find out if input number is armstrong or not
Armstrong number is a number that equals to the sum of cubes of each of its digits
example: 153 is an armstrong number (1*1*1 =1 : 5*5*5=125 : 3*3*3=27 : 1+125+27=153)

Algorithm:

#Get Input from the user (note: stored as string)
#convert input received to a list
#since list is stored as string, create a for loop to convert each number in list to int
#create a variable length that stores length of input, to act as counter
#Initialize result to 0
#for 3 digit armstrong numbers (if length = 3)
#create a for loop that loops within the length
#cubing of each digit inside the list
#convert the answer back to string so it matches with the input user gave
#repeat the same logic for 4 digit numbers
#if the calculated result equals user input, then armstrong number	
#else, not an armstrong number

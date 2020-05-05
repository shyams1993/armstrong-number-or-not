num = [int(i) for i in str(input("Enter a number: "))]
ans = [num[x]**len(num) for x in range(len(num))]
print(f"{int(''.join(str(y) for y in num))} is an Armstrong number" if sum(ans) == int("".join(str(y) for y in num)) else f"{int(''.join(str(y) for y in num))} is not an Armstrong number") 

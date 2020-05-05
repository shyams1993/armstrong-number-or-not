num = input("Enter a num: ")
ans=0
for x in range(len(num)):
    ans = ans + int(str(num)[x])**len(num)
print(f"{num} is an Armstrong number.") if str(ans) == num else print(f"{num} is not an Armstrong number.")

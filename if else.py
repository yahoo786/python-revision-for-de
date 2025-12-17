n1=input("enter num1:")
n2=input("enter num2:")
n3=input("enter num3:")
sum= int(n1) + int(n2) + int(n3)
if sum> 0:
    print("positive")
elif sum < 0:
    print("negative")
elif sum >100:
    print("greater than 100")   
else:
    print("zero")
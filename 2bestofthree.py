a=int(input("enter a variable"))
b=int(input("enter a variable"))
c=int(input("enter a variable"))
sum = (a+b+c)
smallest=a
if (smallest>b):
	smallest=b
if (smallest>c):
	smallest=c
twobestofthree=sum-smallest
print("sum of best of twobestofthree is", twobestofthree)
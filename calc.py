def calc():
	print("Welcome to my calulator")
	var1=int(input("Enter value1:"))
	var2=int(input("Enter value2:"))
	choice=input("Enter 1 for add:\n Enter 2 for sub:\n Enter 3 for mul:\n Enter 4 for div:\n Enter 4 fo power:/n")
	if choice=='1':
		result= var1 + var2
		print("Result=",result)
	elif choice=='2':
		result= var1 - var2
		print("Result=",result)
	elif choice=='3':
		result= var1 * var2
		print("Result",result)
	elif choice=='4':
		result= var1 / var2
		print("Result",result)
	else:
		print("Entered wrong choice")
		calc()
		#function calling


		          
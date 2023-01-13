def takechoice():
	choice=input("Enter Y for yes and N for no:")
	if choice=="y" or choice=="Y":
		return True
	elif choice=="n" or choice=="N":
		return False
	else:
		print("Invalid choice")
		takechoice()
class student:
	def __init__(self):
		self.name=input("Enter Name:")
		self.course=input("Enter Course:")
		self.subject=input("Enter subject:")
	def show(self):
		print("Name:",self.name)
		print("Course",self.course)
		print("subject",self.subject)
s1=student()
s1.show()
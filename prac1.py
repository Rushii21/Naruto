class Employee:
	def __init__(self, number):
		self.number = number
		
	def getdata(self):
		self.name=input('enter name:  ')
		self.desig=input('enter designation:  ')
		self.gender=input('enter gender M/F ')
		self.doj=input("Enter date of joining")
		self.salary=int(input("Enter sal: "))			
				
	def putdata(self):
         		print(self.name,'    ',self.desig,'     ',self.gender,'      ',self.doj,'      ',self.salary)
	

t1=[]
j=0
male=0
female=0
for i in range(10):
    	t1.append(Employee(i))
while True:
    	print('\n Menu')
    	print('\n 1: Getdata')
    	print('\n 2: Display All Records')
    	print('\n 3: Display Total Employees')
    	print('\n 4: Display Genderwise Wise Details')
	print("\n5: Display Employees having sal greater than 10000")
    	print("\n6: Display Employees having designation as Manager")
	print('\n 7: Exit')
    	choice=int(input('Enter ur choice:  '))
    	if(choice==1):
        		t1[j].getdata()
        		j=j+1
    	elif(choice==2):
		print("Name    Designation	Gender 	Date of Joining 	Salary\n") 
		for i in range(0,j):
          			t1[i].putdata()
	elif(choice==3):
		print("Total no of employees are: ",j)
	elif(choice==4):
		for i in range(0,j):
			if(t1[i].gender=="M"):
				male=male+1
			else:
				female=female+1
		print("No of Males: ",male)
		print("No of Females: ",female)	

	elif(choice==5):
		print("Name    Designation	Gender 	Date of Joining 	Salary")
		for i in range(0,j):
			if(t1[i].salary>10000):
				t1[i].putdata()
  	elif(choice==6):
		print("Name    Designation	Gender 	Date of Joining 	Salary")						
		for i in range(0,j):
			if(t1[i].desig=="Manager"):
				t1[i].putdata()	
	
	elif(choice==7):
   		break;
	else:
        		print('Wrong choice') 




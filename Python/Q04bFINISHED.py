#   Q04b

#	write subprogram for menu option 1 here

def lessAttendance(dataset):
	for i in dataset:
		if(i[2] < 75):
			print(i[0],i[1],"Had less than 75% attendance")



#	write subprogram for menu option 2 here

def highAttendance(dataset):
	for i in dataset:
		if(i[2] >= 90):
			print(i[0],i[1],"Had more than 90% attendance")

#	menu program

pupilAttendance = [["Faroukh" , "Salah" , 70],
["Kelvin", "Glintode" , 85],
["Lara" , "Godfrey" , 90],
["Amara" , "Grzinski" , 70],
["Aaron" , "Grimshaw" , 90],
["Farihaa" , "Mohan" , 95],
["Taz" , "Grimstow" , 60],
["Ali" , "Aisha" , 95],
["Charlene" , "Hall" ,85],
["Asra" , "Ashiq" , 90],
["Sadia" , "Bhatti" , 65],
["Ria" , "Hall" , 90],
["Fernado" , "Askabat" , 60],
["Richard" , "Hawkins" , 80],
["Siyao" , "Wang" , 60],
["Marketta" , "Hosier" , 100]]

option = 0
print ("Attendance Menu Options")
print ("1 - Display names of low attendance")
print ("2 - Display number of high attendance")
option=int(input("Choose option: "))
print ('\n')

if option == 1:
    # complete the if statement
	lessAttendance(pupilAttendance)

elif option == 2:
    # complete the else if statement
	highAttendance(pupilAttendance)

else:
    print("Program complete")

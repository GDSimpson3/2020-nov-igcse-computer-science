#	Q02b

#	Set initial values of variables
fencePannel = 1
gap = 4


# 	Request input
length = int(input("Enter the length: "))
width = int(input("Enter the width: "))

# 	Calculate number of panels needed
PanelsNeeded = (2 * (length / fencePannel)) + (2 * (width / fencePannel)) - 4


# 	Print out number of panels needed

print(PanelsNeeded,"pannels needed")

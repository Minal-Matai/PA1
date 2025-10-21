#my_schedule = open("schedule.txt") #By default opens in read mode, can open in write or append mode
my_schedule = open("schedule.txt", "w") #write mode ...
my_schedule.write("Changing content!") #... overwrites all files content
my_schedule=open("schedule.txt", "a") #append mode...
my_schedule.write("\nAdding content!") #...adds to the end of the file contents           

'''
To create a new file in python, just open one that doesn't exist in an edit mode or "x" mode.
'''
#new_file = open("new_file.txt","x") #just creates new file
#new_file.write("HI")

new_file = open("new_file.txt","w") #just creates new file
new_file.write("HI")

'''
line = my_schedule.readline()

while line != "Mod 2:\n":
   line = my_schedule.readline() #advances cursor until we find Mod: 2
print(line) #Print the mod 2 label

for i in range(3): #now we are at the right place so...
   print(my_schedule.readline()) #print the next 3 lines
'''
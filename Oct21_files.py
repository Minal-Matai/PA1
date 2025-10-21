my_schedule = open("schedule.txt")

line = my_schedule.readline()

while line != "Mod 2:\n":
   line = my_schedule.readline() #advances cursor until we find Mod: 2
print(line) #Print the mod 2 label

for i in range(3): #now we are at the right place so...
   print(my_schedule.readline()) #print the next 3 lines
   
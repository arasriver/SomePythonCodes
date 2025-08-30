print("***Wecolme to TODO list project")

task=[]
i = 0
task_num = int(input("Enter number of tasks: "))

while (i < task_num) :
    a = input("Enter name of tasks: ")
    task.append(a.capitalize())
    i+=1

print("Your tasks are: ")

for j in range(len(task)):
  print(task.index(task[j])," ", task[j])


print("\nWhich funtion do you want to do? Enter its number: \n")
print("1. Tick Completed Task, 2. Remove Task \n")
function_num = int(input())




if function_num == 1:
   ex = " "
   while (ex.capitalize() !="Exit"):
    compeleted_num = int(input("Which tasks are completed, Write their numbers: "))
    task[compeleted_num] = task[compeleted_num] + " [DONE]"
    ex = input("write exit to end the program, otherwise enter anything to continue: ")


if function_num == 2:
   ex =" "
   while (ex.capitalize() !="Exit"):
     remove_num = int(input("Which tasks should be removed, Write their numbers: "))
     task[remove_num] = "Removed"
     ex = input("write exit to end the program, otherwise enter anything to continue: ")


for j in range(len(task)):
  print(task.index(task[j])," ", task[j])

print("End")

file = open("SecondLab_2.txt", 'r')
list = []
height = 0
position = 0
aim = 0
total = 0

for line in file:
    line = line.strip()
    list.append(line.split(" "))


for i in range(len(list)):
    
    if list[i][0] == "down":
        height += int(list[i][1])
        aim += int(list[i][1])
    elif list[i][0] == "forward":
        position += int(list[i][1])
        total = total + aim * int(list[i][1])
    elif list[i][0] == "up":
        height -= int(list[i][1])
        aim -= int(list[i][1])
    else:
        print("error")
    print(list[i][0], "\n","height: ", height, "Position: ", position, "Aim: ", aim , "Total: ", total, "\n")
print(position*total)
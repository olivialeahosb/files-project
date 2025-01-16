with open("students.txt", "r") as students:
    for line in students:
        print(line.strip())
 
with open("students.txt", "r") as students:
    for line in students:
        print(line[2])
 
with open("students.txt", "r") as students:
    for line in students:
        if len(line) > 6:
            print(line.strip())
 
userinp = input("Insert your own name into file: ")
 
with open("students.txt", "a") as students:
    students.write(userinp + "\n")
    print("Done")



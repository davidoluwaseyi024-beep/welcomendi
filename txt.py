f = open("demofile.txt")
print(f.read())


f = open("C:\\Users\\USER\\Desktop\\pythonprojects\\welcomendi\\demofile.txt")
print(f.read())

with open("demofile.txt", "a")as f:
    f.write("working on write and create file")

f = open("myfile.txt", "x")


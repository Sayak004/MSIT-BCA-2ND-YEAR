f = open("demofile.txt", "w")    #w stands for creating and writing file
f.write("Hello World 123")
f.close()

#open and read the file after the overwriting:
f = open("demofile.txt", "r")
print(f.read())
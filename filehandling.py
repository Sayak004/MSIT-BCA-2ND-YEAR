f = open("demofile.txt", "w")    #w stands for creating and writing file
f.write("Hello World 123")
f.close()

#open and read the file after the overwriting:
f = open("demofile.txt", "r")
print(f.read())



##delete file in python 


# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")
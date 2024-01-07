print("Hello World")   #To print in python

x, y, z = "Orange", "Banana", "Cherry"   # assigning multiple values
print(x)
print(y)
print(z)



#DataTypes in python

a=32
b=12.23
c=False
d=32+4j
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#arrays datatypes ~ list , set, tuple, dictionary

arr_1=[1,2,4,5,6,8,9,62,3,56]
arr_2=(1,2,4,5,6,8,9,62,3,56)
arr_3={1,2,4,5,6,8,9,62,3,56}
arr_4={
    "name":"python",
    "type":"oops",
    "concept":"class & object",
    "difficulty":"easy to learn",
    "year":"2024",
}
print(arr_1,type(arr_1))
print(arr_2,type(arr_2))
print(arr_3,type(arr_3))
print(arr_4,type(arr_4))



#Class and Function

class Main:
    def main():
        print("Hello World")
    def main_1():
        print("Hii, How are you")
Main.main()
Main.main_1()




class Test:
  x = 5

p1 = Test()   #p1 is the object
print(p1.x)



#loops in python

i=int(input("Enter initial value of range -> "))
j=int(input("Enter extreme value of range -> "))
for x in range(i,j+1):
    print(x,end=" ") 



i=int(input("Enter initial value of range -> "))
j=int(input("Enter extreme value of range -> "))
k=int(input("Enter iteration value of range -> "))
for x in range(i,j,k):
    print(x,end=" ")






# FUNCTION ARGUMENTS 

def my_function(name):
  print(name + " BCA")

my_function("Rahul")
my_function("Raj")
my_function("Pankaj")



# WHILE LOOP

i = 1
while i < 6:
  print(i)
  i += 1



i = 1
while i < 6:
  print(i)
  if i == 3:
    break         #BREAK STATEMENT
  i += 1


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue       #CONTINUE STATEMENT
  print(i)
# ##check database connection

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password=""
# )

# print(mydb)



# ##Create database in python


# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password=""
# )
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE msit_bca")





# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="msit_bca"
# )

# mycursor = mydb.cursor()

<<<<<<< HEAD
# mycursor.execute("CREATE TABLE subjects (digital_electronics VARCHAR(255),soft_engg VARCHAR(255),cyber_sec VARCHAR(255), c_data_structure VARCHAR(255))")



import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="msit_bca"
)
mycursor = mydb.cursor()
mycursor.execute("DROP TABLE students")
=======
# mycursor.execute("CREATE DATABASE python")


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
>>>>>>> ecd2289b22a120cbb116b281b68b3fcf5fab9428

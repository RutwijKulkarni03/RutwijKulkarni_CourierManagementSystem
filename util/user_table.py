import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='rutwij123',
    port='3306',
    database='courier_management_system'
)

mycursor = mydb.cursor()

UserID = input("Enter UserID: ")
Name = input("Enter Name: ")
Email = input("Enter Email: ")
Password = input("Enter Password: ")
ContactNumber = input("Enter Contact Number: ")
Address = input("Enter Address: ")

sql_query = "INSERT INTO user (UserID, Name, Email, Password, ContactNumber, Address) VALUES (%s, %s, %s, %s, %s, %s)"

values = (UserID, Name, Email, Password, ContactNumber, Address)

try:
    mycursor.execute(sql_query, values)
    mydb.commit()

    print("Data inserted successfully into the 'user' table.")

except mysql.connector.Error as error:
    print("Error inserting data into 'user' table:", error)

finally:
    mycursor.close()
    mydb.close()

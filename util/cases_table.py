import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='rutwij123',
    port='3306',
    database='crime_analysis_system'
)

mycursor = mydb.cursor()

case_id = int(input("Enter CaseID: "))
case_description = input("Enter Case Description: ")

sql = "INSERT INTO Cases (CaseID, CaseDescription) VALUES (%s, %s)"
val = (case_id, case_description)

try:
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "Record inserted successfully.")
except mysql.connector.Error as err:
    mydb.rollback()
    print("Error inserting data into Case table:", err)

mydb.close()

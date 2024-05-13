import mysql.connector

import DBConnUtil

def execute_query(query, params=None):
    connection = None
    try:
        connection = DBConnUtil.connect_to_mysql()
        if connection:
            mycursor = connection.cursor()

            if params:
                mycursor.execute(query, params)
            else:
                mycursor.execute(query)

            result = mycursor.fetchall()

            mycursor.close()
            connection.commit()

            return result
        else:
            print("Connection failed.")
            return None
    except Exception as e:
        print("Error executing query:", e)
        return None
    finally:
        if connection:
            connection.close()

# Task 2: Select,Where

# 1. List all customers
query1 = "SELECT * FROM user;"
customers = execute_query(query1)
if customers:
    print("1. List of all customers:")
    for customer in customers:
        print(customer)

# 2. List all orders for a specific customer
user_id = 1  # Replace this with the actual UserID
query2 = "SELECT * FROM orders WHERE UserID = %s;"
orders = execute_query(query2, (user_id,))
if orders:
    print("\n2. List of all orders for the customer with UserID =", user_id)
    for order in orders:
        print(order)

# 3. List all couriers
query3 = "SELECT * FROM courier;"
couriers = execute_query(query3)
if couriers:
    print("\n3. List of all couriers:")
    for courier in couriers:
        print(courier)

# 4. List all packages for a specific order
order_id = 1  # Replace this with the actual OrderID
query4 = "SELECT * FROM parcels WHERE OrderID = %s;"
packages = execute_query(query4, (order_id,))
if packages:
    print("\n4. List of all packages for the order with OrderID =", order_id)
    for package in packages:
        print(package)

# 5. List all deliveries for a specific courier
courier_id = 1  # Replace this with the actual CourierID
query5 = "SELECT * FROM parcels WHERE CourierID = %s;"
deliveries = execute_query(query5, (courier_id,))
if deliveries:
    print("\n5. List of all deliveries for the courier with CourierID =", courier_id)
    for delivery in deliveries:
        print(delivery)

# 6. List all undelivered packages
query6 = "SELECT * FROM parcels WHERE Status = 'Undelivered';"
undelivered_packages = execute_query(query6)
if undelivered_packages:
    print("\n6. List of all undelivered packages:")
    for package in undelivered_packages:
        print(package)

# 7. List all packages that are scheduled for delivery today
query7 = "SELECT * FROM parcels WHERE DeliveryDate = CURDATE();"
todays_deliveries = execute_query(query7)
if todays_deliveries:
    print("\n7. List of all packages scheduled for delivery today:")
    for delivery in todays_deliveries:
        print(delivery)

# 8. List all packages with a specific status
status = 'Delivered'  # Change status as needed
query8 = "SELECT * FROM parcels WHERE Status = %s;"
packages_with_status = execute_query(query8, (status,))
if packages_with_status:
    print(f"\n8. List of all packages with status '{status}':")
    for package in packages_with_status:
        print(package)

# 9. Calculate the total number of packages for each courier
query9 = "SELECT CourierID, COUNT(*) AS TotalPackages FROM parcels GROUP BY CourierID;"
total_packages_per_courier = execute_query(query9)
if total_packages_per_courier:
    print("\n9. Total number of packages for each courier:")
    for courier in total_packages_per_courier:
        print(courier)

# 10. Find the average delivery time for each courier
query10 = "SELECT CourierID, AVG(DATEDIFF(DeliveryDate, OrderDate)) AS AverageDeliveryTime FROM parcels GROUP BY CourierID;"
average_delivery_time_per_courier = execute_query(query10)
if average_delivery_time_per_courier:
    print("\n10. Average delivery time for each courier:")
    for courier in average_delivery_time_per_courier:
        print(courier)

# 11. List all packages with a specific weight range
min_weight = 10  # Change min_weight as needed
max_weight = 20  # Change max_weight as needed
query11 = "SELECT * FROM parcels WHERE Weight BETWEEN %s AND %s;"
packages_in_weight_range = execute_query(query11, (min_weight, max_weight))
if packages_in_weight_range:
    print("\n11. List of all packages within the weight range:")
    for package in packages_in_weight_range:
        print(package)

# 12. Retrieve employees whose names contain 'John'
query12 = "SELECT * FROM employee WHERE Name LIKE '%John%';"
employees_with_name_john = execute_query(query12)
if employees_with_name_john:
    print("\n12. List of employees whose names contain 'John':")
    for employee in employees_with_name_john:
        print(employee)

# 13. Retrieve all courier records with payments greater than $50
query13 = "SELECT c.* FROM courier c JOIN payment p ON c.CourierID = p.CourierID WHERE p.Amount > 50;"
courier_records_with_payments_gt_50 = execute_query(query13)
if courier_records_with_payments_gt_50:
    print("\n13. List of courier records with payments greater than $50:")
    for record in courier_records_with_payments_gt_50:
        print(record)



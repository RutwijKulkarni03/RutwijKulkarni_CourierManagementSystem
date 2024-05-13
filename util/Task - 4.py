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

# Task 4: Inner Join, Full Outer Join, Cross Join, Left Outer Join, Right Outer Join

# 23. Retrieve Payments with Courier Information
query23 = """
SELECT payment.*, c.*
FROM courier_management_system.payment 
INNER JOIN Courier c ON payment.CourierID = c.CourierID;
"""

results23 = execute_query(query23)
if results23:
    print("\n23. Payments with courier information:")
    for result in results23:
        print(result)

# 24. Retrieve Payments with Location Information
query24 = """
SELECT payment.*, l.*
FROM payment 
INNER JOIN Location l ON payment.LocationID = l.LocationID;
"""

results24 = execute_query(query24)
if results24:
    print("\n24. Payments with location information:")
    for result in results24:
        print(result)

# 25. Retrieve Payments with Courier and Location Information
query25 = """
SELECT payment.*, c.*, l.*
FROM payment
INNER JOIN Courier c ON payment.CourierID = c.CourierID
INNER JOIN Location l ON payment.LocationID = l.LocationID;
"""

results25 = execute_query(query25)
if results25:
    print("\n25. Payments with courier and location information:")
    for result in results25:
        print(result)

# 26. List all payments with courier details
query26 = """
SELECT payment.*, c.*
FROM payment
INNER JOIN Courier c ON payment.CourierID = c.CourierID;
"""

results26 = execute_query(query26)
if results26:
    print("\n26. All payments with courier details:")
    for result in results26:
        print(result)

# 27. Total payments received for each courier
query27 = """
SELECT CourierID, SUM(Amount) AS TotalPaymentsReceived
FROM payment
GROUP BY CourierID;
"""

results27 = execute_query(query27)
if results27:
    print("\n27. Total payments received for each courier:")
    for result in results27:
        print(result)

# 28. List payments made on a specific date
query28 = """
SELECT payment.PaymentID, payment.Amount, payment.PaymentDate, c.CourierID, c.SenderName
FROM payment
JOIN courier c ON payment.CourierID = c.CourierID
WHERE DATE(payment.PaymentDate) = '2024-04-13';
"""

results28 = execute_query(query28)
if results28:
    print("\n28. Payments made on a specific date:")
    for result in results28:
        print(result)

# 29. Get Courier Information for Each Payment
query29 = """
SELECT payment.PaymentID, payment.Amount, payment.PaymentDate, c.CourierID, c.SenderName
FROM payment
LEFT JOIN courier c ON payment.CourierID = c.CourierID;
"""

results29 = execute_query(query29)
if results29:
    print("\n29. Courier information for each payment:")
    for result in results29:
        print(result)

# 30. Get Payment Details with Location
query30 = """
SELECT payment.PaymentID, payment.Amount, payment.PaymentDate, l.LocationID, l.LocationName
FROM payment
LEFT JOIN courier c ON payment.CourierID = c.CourierID
LEFT JOIN Location l ON c.LocationID = l.LocationID;
"""

results30 = execute_query(query30)
if results30:
    print("\n30. Payment details with location:")
    for result in results30:
        print(result)

# 31. Calculating Total Payments for Each Courier
query31 = """
SELECT courier.CourierID, SenderName AS CourierName, SUM(payment.Amount) AS TotalPayments
FROM courier
LEFT JOIN payment ON courier.CourierID = payment.CourierID
GROUP BY courier.CourierID, SenderName;
"""

results31 = execute_query(query31)
if results31:
    print("\n31. Total payments for each courier:")
    for result in results31:
        print(result)

# 32. List Payments Within a Date Range
query32 = """
SELECT * FROM payment
WHERE PaymentDate BETWEEN '2024-04-01' AND '2024-04-20';
"""

results32 = execute_query(query32)
if results32:
    print("\n32. Payments within a date range:")
    for result in results32:
        print(result)

# 33. Retrieve a list of all users and their corresponding courier records, including cases where there are no matches on either side
query33 = """
SELECT * FROM `User` 
LEFT JOIN courier ON `User`.UserID = courier.UserID
UNION ALL
SELECT * FROM `User` 
RIGHT JOIN courier ON `User`.UserID = courier.UserID;
"""

results33 = execute_query(query33)
if results33:
    print("\n33. Users and their corresponding courier records:")
    for result in results33:
        print(result)

# 34. Retrieve a list of all couriers and their corresponding services, including cases where there are no matches on either side
query34 = """
SELECT * FROM courier
LEFT JOIN courierservices ON courier.CourierID = courierservices.CourierID
UNION ALL
SELECT * FROM courier
RIGHT JOIN courierservices ON courier.CourierID = courierservices.CourierID;
"""

results34 = execute_query(query34)
if results34:
    print("\n34. Couriers and their corresponding services:")
    for result in results34:
        print(result)

# 35. Retrieve a list of all employees and their corresponding payments, including cases where there are no matches on either side
query35 = """
SELECT * FROM employee
LEFT JOIN payment ON employee.EmployeeID = payment.EmployeeID
UNION ALL
SELECT * FROM employee
RIGHT JOIN payment ON employee.EmployeeID = payment.EmployeeID;
"""

results35 = execute_query(query35)
if results35:
    print("\n35. Employees and their corresponding payments:")
    for result in results35:
        print(result)

# 36. List all users and all courier services, showing all possible combinations
query36 = """
SELECT * FROM user
CROSS JOIN courierservices;
"""

results36 = execute_query(query36)
if results36:
    print("\n36. All users and all courier services:")
    for result in results36:
        print(result)

# 37. List all employees and all locations, showing all possible combinations
query37 = """
SELECT * FROM employee
CROSS JOIN location;
"""

results37 = execute_query(query37)
if results37:
    print("\n37. All employees and all locations:")
    for result in results37:
        print(result)

# 38. Retrieve a list of couriers and their corresponding sender information (if available)
query38 = """
SELECT * FROM courier c
LEFT JOIN parcels s ON c.SenderName = s.SenderName;      
"""

results38 = execute_query(query38)
if results38:
    print("\n38. Couriers and their corresponding sender information:")
    for result in results38:
        print(result)

# 39. Retrieve a list of couriers and their corresponding receiver information (if available)
query39 = """
SELECT * FROM courier c
LEFT JOIN parcels r ON c.ReceiverName = r.ReceiverName;
"""

results39 = execute_query(query39)
if results39:
    print("\n39. Couriers and their corresponding receiver information:")
    for result in results39:
        print(result)

# 40. Retrieve a list of couriers along with the courier service details (if available)
query40 = """
SELECT * FROM courier c
LEFT JOIN courierservices cs ON c.CourierID = cs.CourierID;
"""

results40 = execute_query(query40)
if results40:
    print("\n40. Couriers and their corresponding courier service details:")
    for result in results40:
        print(result)

# 41. Retrieve a list of employees and the number of couriers assigned to each employee
query41 = """
SELECT e.EmployeeID, e.Name, COUNT(c.CourierID) AS NumCouriersAssigned
FROM employee e
LEFT JOIN courier c ON e.EmployeeID = c.EmployeeID
GROUP BY e.EmployeeID, e.Name;
"""

results41 = execute_query(query41)
if results41:
    print("\n41. Employees and the number of couriers assigned to each:")
    for result in results41:
        print(result)

# 42. Retrieve a list of locations and the total payment amount received at each location
query42 = """
SELECT l.LocationID, l.LocationName, SUM(p.Amount) AS TotalPaymentAmount
FROM location l
LEFT JOIN payment p ON l.LocationID = p.LocationID
GROUP BY l.LocationID, l.LocationName;
"""

results42 = execute_query(query42)
if results42:
    print("\n42. Locations and the total payment amount received at each:")
    for result in results42:
        print(result)

# 43. Retrieve all couriers sent by the same sender (based on SenderName)
query43 = """
SELECT c1.* FROM courier c1
JOIN courier c2 ON c1.SenderName = c2.SenderName
WHERE c1.CourierID != c2.CourierID;
"""

results43 = execute_query(query43)
if results43:
    print("\n43. Couriers sent by the same sender:")
    for result in results43:
        print(result)

# 44. List all employees who share the same role
query44 = """
SELECT e1.* FROM employee e1
JOIN employee e2 ON e1.Role = e2.Role
WHERE e1.EmployeeID != e2.EmployeeID order by e1.Role ASC;
"""

results44 = execute_query(query44)
if results44:
    print("\n44. Employees who share the same role:")
    for result in results44:
        print(result)

# 45. Retrieve all payments made for couriers sent from the same location
query45 = """
SELECT * FROM payment p
JOIN courier c ON p.CourierID = c.CourierID
JOIN location l ON c.LocationID = l.LocationID;
"""

results45 = execute_query(query45)
if results45:
    print("\n45. Payments made for couriers sent from the same location:")
    for result in results45:
        print(result)

# 46. Retrieve all couriers sent from the same location (based on SenderAddress)
query46 = """
SELECT * FROM courier c1
JOIN courier c2 ON c1.SenderAddress = c2.SenderAddress
WHERE c1.CourierID != c2.CourierID;
"""

results46 = execute_query(query46)
if results46:
    print("\n46. Couriers sent from the same location:")
    for result in results46:
        print(result)

# 47. List employees and the number of couriers they have delivered
query47 = """
SELECT e.EmployeeID, e.Name, COUNT(c.CourierID) AS NumDeliveredCouriers
FROM employee e
LEFT JOIN courier c ON e.EmployeeID = c.EmployeeID
GROUP BY e.EmployeeID, e.Name;
"""

results47 = execute_query(query47)
if results47:
    print("\n47. Employees and the number of couriers they have delivered:")
    for result in results47:
        print(result)

# 48. Find couriers that were paid an amount greater than the cost of their respective courier services
query48 = """
SELECT * FROM payment p
JOIN courier c ON p.CourierID = c.CourierID
WHERE p.Amount > c.Cost;
"""

results48 = execute_query(query48)
if results48:
    print("\n48. Couriers paid an amount greater than the cost of their services:")
    for result in results48:
        print(result)

# Scope: Inner Queries, Non Equi Joins, Equi joins, Exist, Any, All

# 49. Find couriers that have a weight greater than the average weight of all couriers
query49 = """
SELECT CourierID, Weight, (SELECT AVG(Weight) FROM courier) AS avg_weight
FROM courier WHERE Weight > (SELECT AVG(Weight) FROM courier);
"""

results49 = execute_query(query49)
if results49:
    print("\n49. Couriers with weight greater than the average weight:")
    for result in results49:
        print(result)

# 50. Find the names of all employees who have a salary greater than the average salary
query50 = """
SELECT Name, Salary, (SELECT AVG(Salary) from employee) AS AVG_SALARY FROM Employee 
WHERE Salary > (SELECT AVG(Salary) FROM Employee);
"""

results50 = execute_query(query50)
if results50:
    print("\n50. Employees with salary greater than the average salary:")
    for result in results50:
        print(result)

# 51. Find the total cost of all courier services where the cost is less than the maximum cost
query51 = """
SELECT SUM(Cost) AS TotalCost FROM CourierServices
WHERE Cost < (SELECT MAX(Cost) FROM CourierServices);
"""

results51 = execute_query(query51)
if results51:
    print("\n51. Total cost of courier services where cost is less than maximum cost:")
    for result in results51:
        print(result)

# 52. Find all couriers that have been paid for
query52 = """
SELECT * FROM Courier WHERE CourierID 
IN (SELECT DISTINCT CourierID FROM Payment);
"""

results52 = execute_query(query52)
if results52:
    print("\n52. Couriers that have been paid for:")
    for result in results52:
        print(result)

# 53. Find the locations where the maximum payment amount was made
query53 = """
SELECT LocationName, MAX(Amount) AS MaxPayment
FROM Payment GROUP BY LocationName;
"""

results53 = execute_query(query53)
if results53:
    print("\n53. Locations where the maximum payment amount was made:")
    for result in results53:
        print(result)

# 54. Find all couriers whose weight is greater than the weight of all couriers sent by a specific sender (e.g., 'SenderName')
query54 = """
SELECT c.CourierID, c.Weight FROM Courier c
JOIN (SELECT MAX(Weight) AS MaxWeight FROM Courier WHERE SenderName = 'John Doe') AS max_weight
WHERE c.Weight > max_weight.MaxWeight;
"""

results54 = execute_query(query54)
if results54:
    print("\n54. Couriers with weight greater than weight of couriers sent by a specific sender:")
    for result in results54:
        print(result)



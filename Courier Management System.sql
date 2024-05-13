-- Task1 Database Design 
-- Design a SQL schema for a Courier Management System with tables for Customers, Couriers, Orders, 
-- Parcels, CourierServices, employee, location, payment and user. Define the relationships between 
-- these tables using appropriate foreign keys.

CREATE TABLE User (
    UserID INT PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255) UNIQUE,
    Password VARCHAR(255),
    ContactNumber VARCHAR(20),
    Address TEXT
);

CREATE TABLE Courier (
    CourierID INT PRIMARY KEY,
    SenderName VARCHAR(255),
    SenderAddress TEXT,
    ReceiverName VARCHAR(255),
    ReceiverAddress TEXT,
    Weight DECIMAL(5, 2),
    Status VARCHAR(50),
    TrackingNumber VARCHAR(20) UNIQUE,
    DeliveryDate DATE
);

CREATE TABLE CourierServices (
    ServiceID INT PRIMARY KEY,
    ServiceName VARCHAR(100),
    Cost DECIMAL(8, 2)
);

CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255) UNIQUE,
    ContactNumber VARCHAR(20),
    Role VARCHAR(50),
    Salary DECIMAL(10, 2)
);

CREATE TABLE Location (
    LocationID INT PRIMARY KEY,
    LocationName VARCHAR(100),
    Address TEXT
);

CREATE TABLE Payment (
    PaymentID INT PRIMARY KEY,
    CourierID INT,
    LocationID INT,
    Amount DECIMAL(10, 2),
    PaymentDate DATE,
    FOREIGN KEY (CourierID) REFERENCES Courier(CourierID),
    FOREIGN KEY (LocationID) REFERENCES Location(LocationID)
);

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255) UNIQUE,
    ContactNumber VARCHAR(20),
    Address TEXT
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE Parcels (
    ParcelID INT PRIMARY KEY,
    OrderID INT,
    SenderName VARCHAR(255),
    SenderAddress TEXT,
    ReceiverName VARCHAR(255),
    ReceiverAddress TEXT,
    Weight DECIMAL(5, 2),
    Status VARCHAR(50),
    TrackingNumber VARCHAR(20) UNIQUE,
    DeliveryDate DATE,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);


/*
INSERT INTO `courier_management_system`.`courier`(`CourierID`, `SenderName`, `SenderAddress`, `ReceiverName`, `ReceiverAddress`, `Weight`, `Status`, `TrackingNumber`, `DeliveryDate`) 
VALUES
(1, 'John Doe', '123 Main St, City, Country', 'Jane Smith', '456 Oak St, City, Country', 2.5, 'In transit', 'ABC123', '2024-04-05'),
(2, 'Michael Johnson', '789 Elm St, City, Country', 'Emily Brown', '321 Pine St, City, Country', 1.8, 'Delivered', 'DEF456', '2024-04-04'),
(3, 'David Wilson', '654 Cedar St, City, Country', 'Sarah Taylor', '987 Maple St, City, Country', 3.2, 'In transit', 'GHI789', '2024-04-06'),
(4, 'Christopher Martinez', '147 Walnut St, City, Country', 'Amanda White', '852 Birch St, City, Country', 1.0, 'Pending', 'JKL012', '2024-04-08'),
(5, 'Robert Lee', '369 Spruce St, City, Country', 'Jennifer Lopez', '963 Oakwood St, City, Country', 2.7, 'In transit', 'MNO345', '2024-04-07'),
(6, 'John Doe', '123 Main St, City, Country', 'Emily Brown', '321 Pine St, City, Country', 1.5, 'Delivered', 'PQR678', '2024-04-03'),
(7, 'Sarah Taylor', '987 Maple St, City, Country', 'Christopher Martinez', '147 Walnut St, City, Country', 2.0, 'In transit', 'STU901', '2024-04-08'),
(8, 'Amanda White', '852 Birch St, City, Country', 'Robert Lee', '369 Spruce St, City, Country', 3.5, 'Pending', 'VWX234', '2024-04-10'),
(9, 'Jennifer Lopez', '963 Oakwood St, City, Country', 'John Doe', '123 Main St, City, Country', 1.9, 'In transit', 'YZA567', '2024-04-09'),
(10, 'Jane Smith', '456 Oak St, City, Country', 'Michael Johnson', '789 Elm St, City, Country', 2.3, 'Pending', 'BCD890', '2024-04-11');

INSERT INTO courierservices (ServiceID, ServiceName, Cost)
VALUES
    (1, 'Standard Delivery', 10.00),
    (2, 'Express Delivery', 20.00),
    (3, 'Overnight Delivery', 30.00),
    (4, 'Same-Day Delivery', 25.00),
    (5, 'International Delivery', 50.00),
    (6, 'Special Handling', 15.00),
    (7, 'Fragile Items', 12.00),
    (8, 'Bulk Delivery', 40.00),
    (9, 'Document Delivery', 5.00),
    (10, 'Priority Delivery', 35.00);

INSERT INTO employee (EmployeeID, Name, Email, ContactNumber, Role, Salary) 
VALUES 
(101, 'John Doe', 'johndoe@example.com', '1234567890', 'Manager', 50000.00),
(102, 'Jane Smith', 'janesmith@example.com', '9876543210', 'Developer', 40000.00),
(103, 'Alice Johnson', 'alicejohnson@example.com', '5551234567', 'HR', 45000.00),
(104, 'Bob Brown', 'bobbrown@example.com', '6667891234', 'Accountant', 48000.00),
(105, 'Emma Wilson', 'emmawilson@example.com', '7774567890', 'Designer', 42000.00),
(106, 'Michael Clark', 'michaelclark@example.com', '5557891234', 'Analyst', 47000.00),
(107, 'Sarah Martinez', 'sarahmartinez@example.com', '3339876543', 'Sales', 43000.00),
(108, 'David Lee', 'davidlee@example.com', '2223456789', 'Project Manager', 55000.00),
(109, 'Jessica Garcia', 'jessicagarcia@example.com', '8882345678', 'Marketing', 46000.00),
(110, 'Matthew Rodriguez', 'matthewrodriguez@example.com', '7774567890', 'Consultant', 51000.00);

INSERT INTO location (LocationID, LocationName, Address)
VALUES
    (1, 'Head Office', '123 Main Street, CityA, CountryX'),
    (2, 'Warehouse A', '456 Park Avenue, CityB, CountryY'),
    (3, 'Branch Office 1', '789 Elm Street, CityC, CountryZ'),
    (4, 'Warehouse B', '101 Pine Street, CityD, CountryW'),
    (5, 'Branch Office 2', '222 Oak Street, CityE, CountryV'),
    (6, 'Warehouse C', '333 Maple Street, CityF, CountryU'),
    (7, 'Branch Office 3', '444 Cedar Street, CityG, CountryT'),
    (8, 'Warehouse D', '555 Birch Street, CityH, CountryS'),
    (9, 'Branch Office 4', '666 Walnut Street, CityI, CountryR'),
    (10, 'Warehouse E', '777 Cherry Street, CityJ, CountryQ');

INSERT INTO payment (PaymentID, CourierID, LocationID, Amount, PaymentDate)
VALUES
    (101, 1, 1, 50.00, '2024-04-10'),
    (102, 2, 2, 75.00, '2024-04-11'),
    (103, 3, 3, 100.00, '2024-04-12'),
    (104, 4, 4, 65.00, '2024-04-13'),
    (105, 5, 5, 80.00, '2024-04-14'),
    (106, 6, 1, 55.00, '2024-04-15'),
    (107, 7, 2, 70.00, '2024-04-16'),
    (108, 8, 3, 90.00, '2024-04-17'),
    (109, 9, 4, 85.00, '2024-04-18'),
    (110, 10, 5, 95.00, '2024-04-19');

INSERT INTO user (UserID, Name, Email, Password, ContactNumber, Address) 
VALUES 
(1, 'John Doe', 'johndoe@example.com', 'password123', '1234567890', '123 Main Street'),
(2, 'Jane Smith', 'janesmith@example.com', 'password456', '0987654321', '456 Elm Street'),
(3, 'Alice Johnson', 'alicejohnson@example.com', 'password789', '9876543210', '789 Oak Street'),
(4, 'Bob Brown', 'bobbrown@example.com', 'password101', '1234567890', '101 Pine Street'),
(5, 'Emma Wilson', 'emmawilson@example.com', 'password202', '0987654321', '222 Oak Street'),
(6, 'David Lee', 'davidlee@example.com', 'password303', '9876543210', '333 Elm Street'),
(7, 'Sarah Jones', 'sarahjones@example.com', 'password404', '1234567890', '444 Maple Street'),
(8, 'Michael Johnson', 'michaeljohnson@example.com', 'password505', '0987654321', '555 Pine Street'),
(9, 'Emily Davis', 'emilydavis@example.com', 'password606', '9876543210', '666 Oak Street'),
(10, 'Daniel Smith', 'danielsmith@example.com', 'password707', '1234567890', '777 Elm Street');

INSERT INTO parcels (ParcelID, OrderID, SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate)
VALUES 
(1, 1, 'John Doe', '123 Main Street', 'Jane Smith', '456 Elm Street', 5.0, 'In Transit', 'TN123456', '2024-04-15'),
(2, 2, 'Alice Johnson', '789 Oak Avenue', 'Bob Brown', '321 Pine Street', 3.5, 'Delivered', 'TN789012', '2024-04-10'),
(3, 3, 'Emily Davis', '456 Elm Street', 'David Wilson', '789 Oak Avenue', 7.2, 'Out for Delivery', 'TN345678', '2024-04-20'),
(4, 4, 'Sarah Taylor', '101 Pine Street', 'Michael Clark', '222 Oak Street', 6.8, 'In Transit', 'TN901234', '2024-04-25'),
(5, 5, 'James Johnson', '222 Oak Street', 'Laura Martinez', '789 Elm Street', 4.2, 'Out for Delivery', 'TN567890', '2024-04-28'),
(6, 6, 'Ethan Carter', '101 Pine Street', 'Sophia Rodriguez', '456 Park Avenue', 8.5, 'In Transit', 'TN678901', '2024-05-02'),
(7, 7, 'Olivia Anderson', '789 Elm Street', 'Alexander Harris', '101 Pine Street', 3.0, 'Delivered', 'TN234567', '2024-05-05'),
(8, 8, 'Daniel Moore', '456 Park Avenue', 'Ava Jackson', '123 Main Street', 5.7, 'Out for Delivery', 'TN789012', '2024-05-08'),
(9, 9, 'Mia Thompson', '222 Oak Street', 'Liam White', '789 Oak Avenue', 6.3, 'In Transit', 'TN345678', '2024-05-12'),
(10, 10, 'William Lee', '123 Main Street', 'Emily Brown', '456 Elm Street', 4.9, 'Out for Delivery', 'TN012345', '2024-05-15');

INSERT INTO customers (CustomerID, Name, Email, ContactNumber, Address)
VALUES 
(1, 'John Doe', 'johndoe@gmail.com', '1234567890', '123 Main Street'),
(2, 'Jane Smith', 'janesmith@gmail.com', '0987654321', '456 Elm Street'),
(3, 'Alice Johnson', 'alicejohnson@gmail.com', '1112223333', '789 Oak Avenue'),
(4, 'Michael Brown', 'michaelbrown@gmail.com', '4445556666', '321 Maple Road'),
(5, 'Emily Wilson', 'emilywilson@gmail.com', '7778889999', '567 Pine Lane'),
(6, 'David Lee', 'davidlee@gmail.com', '6667778888', '987 Cedar Drive'),
(7, 'Sarah Martinez', 'sarahmartinez@gmail.com', '3334445555', '654 Birch Street'),
(8, 'Christopher Taylor', 'christophertaylor@gmail.com', '2223334444', '890 Walnut Avenue'),
(9, 'Jessica Garcia', 'jessicagarcia@gmail.com', '9990001111', '246 Oakwood Drive'),
(10, 'Matthew Rodriguez', 'matthewrodriguez@gmail.com', '8889990000', '135 Elmwood Avenue');

INSERT INTO orders (OrderID, CustomerID, OrderDate)
VALUES 
(1, 1, '2024-04-05'),
(2, 2, '2024-04-08'),
(3, 3, '2024-04-10'),
(4, 4, '2024-04-12'),
(5, 5, '2024-04-15'),
(6, 6, '2024-04-18'),
(7, 7, '2024-04-20'),
(8, 8, '2024-04-23'),
(9, 9, '2024-04-25'),
(10, 10, '2024-04-28');

*/

# TASK - 2 (SELECT, WHERE)

# Question - 1. List all customers:  
SELECT * FROM courier_management_system.user;

# Question - 2.  List all orders for a specific customer:
SELECT * FROM courier_management_system.customers WHERE Name = 'John Doe';

# Question - 3.  List all couriers:  
SELECT * FROM courier_management_system.courier;

# Question - 4.  List all packages for a specific order:  
SELECT * FROM courier_management_system.parcels WHERE OrderID >= 2 AND OrderID <= 3;

# Question - 5. List all deliveries for a specific courier:  
SELECT * FROM courier_management_system.courier WHERE SenderName = 'John Doe';

# Question - 6. List all undelivered packages:  
SELECT * FROM courier_management_system.courier WHERE Status != 'Delivered';

# Question - 7. List all packages that are scheduled for delivery today:  
SELECT * FROM courier_management_system.courier WHERE DeliveryDate = CURDATE();

# Question - 8. List all packages with a specific status:  
SELECT * FROM courier_management_system.courier WHERE Status = 'In Transit';

# Question - 9. Calculate the total number of packages for each courier:
SELECT SenderName, COUNT(*) AS TotalPackages FROM courier_management_system.parcels GROUP BY SenderName;

# Question - 10.  Find the average delivery time for each courier:
SELECT p.CourierID, AVG(DATEDIFF(p.DeliveryDate, o.OrderDate)) AS AvgDeliveryTime
FROM Parcels p
JOIN Orders o ON p.OrderID = o.OrderID
GROUP BY p.CourierID;

# Question - 11. List all packages with a specific weight range:  
SELECT * FROM courier_management_system.courier WHERE Weight BETWEEN '2' AND '3';

# Question - 12. Retrieve employees whose names contain 'John'  
SELECT * FROM courier_management_system.employee WHERE Name LIKE '%John%';

# Question - 13. Retrieve all courier records with payments greater than $50.  
SELECT * FROM courier_management_system.payment WHERE Amount > 50;

------------------------------------------------------------------------------------------------------------------------------------------------

# Task 3: (GroupBy, Aggregate Functions, Having, Order By, where)

# 14. Find the total number of couriers handled by each employee.  
use courier_management_system;
SELECT EmployeeID, Name, COUNT(CourierID) AS TotalCouriersHandled
FROM courier_management_system.employee
LEFT JOIN Courier c ON EmployeeID = EmployeeID
GROUP BY EmployeeID, Name;

# 15. Calculate the total revenue generated by each location  
SELECT l.LocationID, l.LocationName, SUM(p.Amount) AS TotalRevenue
FROM Location l
LEFT JOIN Payment p ON l.LocationID = p.LocationID
GROUP BY l.LocationID, l.LocationName;

# 16. Find the total number of couriers delivered to each location.  
SELECT l.LocationID, l.LocationName, COUNT(c.CourierID) AS TotalCouriersDelivered
FROM Location l
LEFT JOIN Orders o ON l.LocationID = LocationID
LEFT JOIN Courier c ON o.OrderID = OrderID
WHERE c.Status = 'Delivered'
GROUP BY l.LocationID, l.LocationName;

# 17. Find the courier with the highest average delivery time:  
SELECT c.CourierID, AVG(DATEDIFF(p.DeliveryDate, o.OrderDate)) AS AvgDeliveryTime
FROM Courier c
JOIN Parcels p ON c.CourierID = p.CourierID
JOIN Orders o ON p.OrderID = o.OrderID
GROUP BY c.CourierID
ORDER BY AvgDeliveryTime DESC
LIMIT 1;

# 18. Find Locations with Total Payments Less Than a Certain Amount  
SELECT l.LocationID, l.LocationName, SUM(p.Amount) AS TotalPayments
FROM Location l
LEFT JOIN Payment p ON l.LocationID = p.LocationID
GROUP BY l.LocationID, l.LocationName
HAVING TotalPayments < 200;

# 19. Calculate Total Payments per Location 
SELECT LocationID, LocationName, SUM(Amount) AS TotalPayments
FROM Payment
GROUP BY LocationID, LocationName;

# 20. Retrieve couriers who have received payments totaling more than $50 in a specific location (LocationID = X):  
SELECT c.CourierID, c.SenderName, p.LocationName
FROM Courier c
JOIN Payment p ON c.CourierID = p.CourierID
WHERE p.LocationID = 2
GROUP BY c.CourierID, c.SenderName, p.LocationName
HAVING SUM(p.Amount) > 50;

# 21. Retrieve couriers who have received payments totaling more than $50 after a certain date (PaymentDate > 'YYYY-MM-DD'):  
SELECT c.CourierID, SenderName
FROM Courier c
JOIN Payment p ON c.CourierID = p.CourierID
WHERE p.PaymentDate > '2024-04-04'
GROUP BY c.CourierID, SenderName
HAVING SUM(p.Amount) > 50;

# 22. Retrieve locations where the total amount received is more than $50 before a certain date (PaymentDate > 'YYYY-MM-DD')    
SELECT l.LocationID, l.LocationName
FROM Location l
JOIN Payment p ON l.LocationID = p.LocationID
WHERE p.PaymentDate < '2024-04-15'
GROUP BY l.LocationID, l.LocationName
HAVING SUM(p.Amount) > 50;

------------------------------------------------------------------------------------------------------------------------------------------------

#Task 4: Inner Join,Full Outer Join, Cross Join, Left Outer Join,Right Outer Join 

-- 23. Retrieve Payments with Courier Information 
use courier_management_system;
SELECT payment.*, c.*
FROM courier_management_system.payment 
INNER JOIN Courier c ON payment.CourierID = c.CourierID;

-- 24. Retrieve Payments with Location Information 
SELECT payment.*, l.*
FROM payment 
INNER JOIN Location l ON payment.LocationID = l.LocationID;

-- 25. Retrieve Payments with Courier and Location Information 
SELECT payment.*, c.*, l.*
FROM payment
INNER JOIN Courier c ON payment.CourierID = c.CourierID
INNER JOIN Location l ON payment.LocationID = l.LocationID;

-- 26. List all payments with courier details 
SELECT payment.*, c.*
FROM payment
INNER JOIN Courier c ON payment.CourierID = c.CourierID;

-- 27. Total payments received for each courier 
SELECT CourierID, SUM(Amount) AS TotalPaymentsReceived
FROM payment
GROUP BY CourierID;

-- 28. List payments made on a specific date 
SELECT payment.PaymentID, payment.Amount, payment.PaymentDate, c.CourierID, c.SenderName
FROM payment
JOIN courier c ON payment.CourierID = c.CourierID
WHERE DATE(payment.PaymentDate) = '2024-04-13';

-- 29. Get Courier Information for Each Payment
SELECT payment.PaymentID, payment.Amount, payment.PaymentDate, c.CourierID, c.SenderName
FROM payment
LEFT JOIN courier c ON payment.CourierID = c.CourierID;

-- 30. Get Payment Details with Location 
SELECT payment.PaymentID, payment.Amount, payment.PaymentDate, l.LocationID, l.LocationName
FROM payment
LEFT JOIN courier c ON payment.CourierID = c.CourierID
LEFT JOIN Location l ON c.LocationID = l.LocationID;

-- 31. Calculating Total Payments for Each Courier 
SELECT courier.CourierID, SenderName AS CourierName, SUM(payment.Amount) AS TotalPayments
FROM courier
LEFT JOIN payment ON courier.CourierID = payment.CourierID
GROUP BY courier.CourierID, SenderName;

-- 32. List Payments Within a Date Range 
SELECT * FROM payment
WHERE PaymentDate BETWEEN '2024-04-01' AND '2024-04-20';

-- 33. Retrieve a list of all users and their corresponding courier records, including cases where there are no matches on either side 
SELECT * FROM `User` 
LEFT JOIN courier ON `User`.UserID = courier.UserID
UNION ALL
SELECT * FROM `User` 
RIGHT JOIN courier ON `User`.UserID = courier.UserID;

-- 34. Retrieve a list of all couriers and their corresponding services, including cases where there are no matches on either side 
SELECT * FROM courier
LEFT JOIN courierservices ON courier.CourierID = courierservices.CourierID
UNION ALL
SELECT * FROM courier
RIGHT JOIN courierservices ON courier.CourierID = courierservices.CourierID;

-- 35. Retrieve a list of all employees and their corresponding payments, including cases where there are no matches on either side 
SELECT * FROM employee
LEFT JOIN payment ON employee.EmployeeID = payment.EmployeeID
UNION ALL
SELECT * FROM employee
RIGHT JOIN payment ON employee.EmployeeID = payment.EmployeeID;

-- 36. List all users and all courier services, showing all possible combinations. 
SELECT * FROM user
CROSS JOIN courierservices;

-- 37. List all employees and all locations, showing all possible combinations: 
SELECT * FROM employee
CROSS JOIN location;

-- 38. Retrieve a list of couriers and their corresponding sender information (if available) 
SELECT * FROM courier c
LEFT JOIN parcels s ON c.SenderName = s.SenderName;		

-- 39. Retrieve a list of couriers and their corresponding receiver information (if available): 
SELECT * FROM courier c
LEFT JOIN parcels r ON c.ReceiverName = r.ReceiverName;


-- 40. Retrieve a list of couriers along with the courier service details (if available): 
SELECT * FROM courier c
LEFT JOIN courierservices cs ON c.CourierID = cs.CourierID;

-- 41. Retrieve a list of employees and the number of couriers assigned to each employee: 
SELECT e.EmployeeID, e.Name, COUNT(c.CourierID) AS NumCouriersAssigned
FROM employee e
LEFT JOIN courier c ON e.EmployeeID = c.EmployeeID
GROUP BY e.EmployeeID, e.Name;

-- 42. Retrieve a list of locations and the total payment amount received at each location: 
SELECT l.LocationID, l.LocationName, SUM(p.Amount) AS TotalPaymentAmount
FROM location l
LEFT JOIN payment p ON l.LocationID = p.LocationID
GROUP BY l.LocationID, l.LocationName;

-- 43. Retrieve all couriers sent by the same sender (based on SenderName). 
SELECT c1.* FROM courier c1
JOIN courier c2 ON c1.SenderName = c2.SenderName
WHERE c1.CourierID != c2.CourierID;

-- 44. List all employees who share the same role. 
SELECT e1.* FROM employee e1
JOIN employee e2 ON e1.Role = e2.Role
WHERE e1.EmployeeID != e2.EmployeeID order by e1.Role ASC;

-- 45. Retrieve all payments made for couriers sent from the same location. 
SELECT * FROM payment p
JOIN courier c ON p.CourierID = c.CourierID
JOIN location l ON c.LocationID = l.LocationID;

-- 46. Retrieve all couriers sent from the same location (based on SenderAddress). 
SELECT * FROM courier c1
JOIN courier c2 ON c1.SenderAddress = c2.SenderAddress
WHERE c1.CourierID != c2.CourierID;

-- 47. List employees and the number of couriers they have delivered: 
SELECT e.EmployeeID, e.Name, COUNT(c.CourierID) AS NumDeliveredCouriers
FROM employee e
LEFT JOIN courier c ON e.EmployeeID = c.EmployeeID
GROUP BY e.EmployeeID, e.Name;

-- 48. Find couriers that were paid an amount greater than the cost of their respective courier services 
SELECT * FROM payment p
JOIN courier c ON p.CourierID = c.CourierID
WHERE p.Amount > c.Cost;

-- Scope: Inner Queries, Non Equi Joins, Equi joins,Exist,Any,All 

-- 49. Find couriers that have a weight greater than the average weight of all couriers 
SELECT CourierID, Weight, (SELECT AVG(Weight) FROM courier) AS avg_weight
FROM courier WHERE Weight > (SELECT AVG(Weight) FROM courier);

-- 50. Find the names of all employees who have a salary greater than the average salary: 
SELECT Name, Salary, (SELECT AVG(SALARY) from employee) AS AVG_SALARY FROM Employee 
WHERE Salary > (SELECT AVG(Salary) FROM Employee);

-- 51. Find the total cost of all courier services where the cost is less than the maximum cost 
SELECT SUM(Cost) AS TotalCost FROM CourierServices
WHERE Cost < (SELECT MAX(Cost) FROM CourierServices);

-- 52. Find all couriers that have been paid for 
SELECT * FROM Courier WHERE CourierID 
IN (SELECT DISTINCT CourierID FROM Payment);

-- 53. Find the locations where the maximum payment amount was made 
SELECT LocationName, MAX(Amount) AS MaxPayment
FROM Payment GROUP BY LocationName;

-- 54. Find all couriers whose weight is greater than the weight of all couriers sent by a specific sender (e.g., 'SenderName'):
SELECT c.CourierID, c.Weight FROM Courier c
JOIN (SELECT MAX(Weight) AS MaxWeight FROM Courier WHERE SenderName = 'John Doe') AS max_weight
WHERE c.Weight > max_weight.MaxWeight;

---------------------------------------------------------------------------------------------------------------------------------------






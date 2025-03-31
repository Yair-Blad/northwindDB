import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("Nortwind.db")

#Obteniendo los 10 productos mas rentables y graficandolos
query_prod = '''
    SELECT ProductName, SUM(Price * Quantity) as Revenue
    FROM OrderDetails od
    JOIN Products p ON p.ProductID = od.ProductID
    GROUP BY od.ProductID
    ORDER BY Revenue DESC
    LIMIT 10
'''

top_products = pd.read_sql_query(query_prod, conn)

top_products.plot(x="ProductName", y="Revenue", kind="bar", figsize=(10, 6), legend=False)

plt.title("10 Productos mas rentables")
plt.xlabel("Productos")
plt.ylabel("Revenue")
plt.xticks(rotation=80)
plt.show()


#Obteniendo los 10 empleados mas productivos

query_employee = '''
    SELECT FirstName || " " || LastName as Employee, COUNT(*) as Total
    FROM Orders o
    JOIN Employees e
    ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY Total DESC
    LIMIT 10
'''

top_employees = pd.read_sql_query(query_employee, conn)
top_employees.plot(x="Employee", y="Total", kind="bar", figsize=(10, 6), legend=False)

plt.title("10 Empleados mas efectivos")
plt.xlabel("Empleados")
plt.ylabel("Total vendido")
plt.xticks(rotation = 80)
plt.show()

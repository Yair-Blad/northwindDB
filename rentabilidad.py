import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("Nortwind.db")

#Obteniendo los 10 productos mas rentables y graficandolos
query = '''
    SELECT ProductName, SUM(Price * Quantity) as Revenue
    FROM OrderDetails od
    JOIN Products p ON p.ProductID = od.ProductID
    GROUP BY od.ProductID
    ORDER BY Revenue DESC
    LIMIT 10
'''

top_products = pd.read_sql_query(query, conn)

top_products.plot(x="ProductName", y="Revenue", kind="bar", figsize=(10, 5), legend=False)

plt.title("10 Productos mas rentables")
plt.xlabel("Productos")
plt.ylabel("Revenue")
plt.xticks(rotation=80)
plt.show()

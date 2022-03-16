import psycopg2

conn = psycopg2.connect("postgresql://order_app:Pass1234@localhost/sneakerstore_database")
cur = conn.cursor()

print("Please enter an order ID...Orders Available are 90010-90015")
order_id = int(input())
cur.execute("""
    SELECT customers.first_name, customers.last_name, customers.street_address, customers.city, customers.state, customers.zip, customers.phone, 
    inventory.style_id, inventory.brand, inventory.name, inventory.retail, quantity, total
    
    FROM orders, customers, inventory
    
    WHERE orders.customer_id=customers.customer_id
        AND orders.style_id=inventory.style_id
        AND order_id=%s
""", (order_id,));

    print(f"Style ID:{row[6]} Brand:{row[7]} Name:{row[8]} Price Per Pair:{row[9]} Quantity:{row[10]} Total:{row[11]}")
print(f" ")

print(f"Ship to: {row[0]} {row[1]}")
print(f"Address: {row[2]} {row[1]}")
print(f"         {row[3]}, {row[4]} {row[5]}")
print(f" ")


cur.close()
conn.close()

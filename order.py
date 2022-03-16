import psycopg2

conn = psycopg2.connect("postgresql://order_app:Pass1234@localhost/sneakerstore_database")
cur = conn.cursor()

print("Please enter an order ID...Orders Available are 90010-90015")
order_id = int(input())
cur.execute("""
    SELECT customers.first_name, customers.last_name, customers.street_address, customers.city, customers.state, customers.zip, customers.phone, 
    inventory.style_id, quantity
    
    FROM orders, customers, inventory
    
    WHERE orders.customer_id=customers.customer_id
        AND orders.style_id=inventory.style_id
        AND order_id=%s
""", (order_id,));
for row in cur:
    item_name = row[2]
    quantity = row[3]
    print(f"{item_name} x {quantity}")
    
print(f"Ship to: {row[0]} {row[1]}")
print(f"Address: {row[2]} {row[1]}")
print(f"         {row[3]}, {row[4]} {row[5]}")

cur.close()
conn.close()
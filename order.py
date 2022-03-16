import psycopg2

conn = psycopg2.connect("postgresql://order_app:P@ss1234@localhost/sneakerstore_database")
cur = conn.cursor()

print("Please enter an order ID...Orders Available are 90010-90015")
order_id = int(input())
cur.execute("""
    SELECT customers.first_name, inventory.style_id, quantity
    FROM orders, customers, inventory
    WHERE orders.customer_id=customers.customer_id
        AND orders.style_id=inventory.style_id
        AND order_id=%s
""", (order_id,));
for row in cur:
    item_name = row[1]
    quantity = row[2]
    print(f"{item_name} x {quantity}")
print(f"Deliver to: {row[0]}")

cur.close()
conn.close()
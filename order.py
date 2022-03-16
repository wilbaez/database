import psycopg2

conn = psycopg2.connect("postgresql://order_app:Pass1234@localhost/sneakerstore_database")
cur = conn.cursor()

print("Please enter an order ID...Orders Available are 90010-90015")
order_id = int(input())
cur.execute("""
    SELECT customers.first_name, customers.last_name, customers.street_address, customers.city, customers.state, customers.zip, customers.phone, 
    inventory.style_id, inventory.brand, inventory.name, inventory.retail, quantity, total, employee_id, employees.first_name
    
    FROM orders, customers, inventory, employees
    
    WHERE orders.customer_id=customers.customer_id
        AND orders.style_id=inventory.style_id
        AND orders.employee_id=employees.employee_id
        AND order_id=%s
""", (order_id,));

for row in cur:
    sty = row[7]
    bra = row[8]
    nam = row[9]
    pri = row[10]
    qua = row[11]
    tot = row[12]
    print(f"Style ID: {sty} Brand: {bra} Name: {nam} Price Per Pair: {pri} Quantity: {qua} Total: {tot}")
print(f" ")
print(f" ******CUSTOMER INFORMATION******")
print(f" ")
print(f"Ship to: {row[0]} {row[1]}")
print(f"Address: {row[2]}
print(f"         {row[3]}, {row[4]} {row[5]}")
print(f"  Phone: {row[6]}
print(f" ")
print(f" ******EMPLOYEE INFORMATION******")
print(f" ")
print(f"Sold by: {row[14]}")
print(f" EMP ID: {row[13]}")

cur.close()
conn.close()
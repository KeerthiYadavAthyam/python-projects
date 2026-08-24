# list of customer orders
orders = [
    {
        "customer_id": 1, 
        "cust_name": "John Doe",      
        "order_id": 101,
        "items": [  
            (1, 2, 50000.0),  
            (1, 1, 50000.0),
            (5, 2, 1000.0),  
            (6, 1, 300.0) 
                   
        ]
    },
    {
        "customer_id": 2, 
        "cust_name": "Jane Smith",      
        "order_id": 102,
        "items": [  
            (1, 2, 50000.0),  
            (2, 7, 17000.0),
            (3, 9, 3000.0),  
            (7, 18, 50.0)        
        ]
    },
    {   
        "customer_id": 3,
        "cust_name": "Alice Johnson",
        "order_id": 103,
        "items": [
            (9, 4, 5000.0),
            (3, 15, 3000.0),
            (1, 2, 10.0),  
            (1, 3, 20.0)
        ]
    },
    {
        "customer_id": 4,
        "cust_name": "Bob Brown",
        "order_id": 105,
        "items": [
            (4, 2, 30.0),
            (3, 1, 3000.0),
            (5, 5, 1000.0),  
            (8, 12, 2000.0)
        ]
    },
    {
        "customer_id": 3,
        "cust_name": "Alice Johnson",
        "order_id": 106,
        "items": [
            (4, 20, 30.0),
            (3, 14, 3000.0),
            (5, 15, 1000.0),  
            (8, 12, 2000.0)
        ]
    },
    {
        "customer_id": 4,
        "cust_name": "Bob Brown",
        "order_id": 104,
        "items": [
            (2, 3, 17000.0),
            (6, 4, 300.0),  
            (7, 10, 50.0),        
            (10, 1, 1500.0)
        ]
    },
    {
        "customer_id": 5,
        "cust_name": "Charlie Davis",   
        "order_id": 107,
        "items": [  
            (2, 3, 17000.0),
            (6, 4, 300.0),  
            (7, 10, 50.0),        
            (10, 1, 1500.0)
        ]       
    },    
    {   
        "customer_id": 6,
        "cust_name": "Diana Evans",
        "order_id": 108,
        "items": [
            (9, 2, 5000.0),
            (3, 5, 3000.0),
            (1, 1, 10.0),  
            (1, 1, 20.0)
        ]
    },  
    {
        "customer_id": 7,
        "cust_name": "Ethan Foster",
        "order_id": 109,
        "items": [
            (4, 5, 30.0),
            (3, 2, 3000.0),
            (5, 1, 1000.0),  
            (8, 3, 2000.0)
        ]
    },
    {
        "customer_id": 8,
        "cust_name": "Fiona Green",
        "order_id": 110,
        "items": [
            (4, 10, 30.0),
            (3, 8, 3000.0),
            (5, 4, 1000.0),  
            (8, 6, 2000.0)
        ]
    },  
    {
        "customer_id": 9,
        "cust_name": "George Harris",
        "order_id": 111,
        "items": [
            (2, 1, 17000.0),
            (6, 2, 300.0),  
            (7, 5, 50.0),        
            (10, 2, 1500.0)
        ]       
    },
    {   
        "customer_id": 10,
        "cust_name": "Hannah Irving",
        "order_id": 112,
        "items": [
            (2, 3, 17000.0),
            (6, 4, 300.0),  
            (7, 10, 50.0),        
            (10, 1, 1500.0)
        ]
    },
    {
        "customer_id": 10,
        "cust_name": "Hannah Irving",
        "order_id": 113,
        "items": [
            (4, 8, 30.0),
            (3, 4, 3000.0),
            (5, 2, 1000.0),  
            (8, 5, 2000.0)
        ]
    }
]

# A dictionary mapping product_id to product details 
products = {
    1: {"name": "Laptop", "category": "Electronics"},   
    2: {"name": "Smartphone", "category": "Electronics"},
    3: {"name": "Desk Chair", "category": "Furniture"},     
    4: {"name": "Book", "category": "Stationery"},
    5: {"name": "Headphones", "category": "Electronics"},
    6: {"name": "Coffee Mug", "category": "Kitchenware"},
    7: {"name": "Notebook", "category": "Stationery"},
    8: {"name": "Backpack", "category": "Accessories"}, 
    9: {"name": "Monitor", "category": "Electronics"},
    10: {"name": "Keyboard", "category": "Electronics"}
}

# Dictionary to store total quantity sold per product
total_quantity_sold = {}    
for order in orders:
    for item in order["items"]:
        product_id, quantity, price = item
        if product_id in total_quantity_sold:
            total_quantity_sold[product_id] += quantity
        else:
            total_quantity_sold[product_id] = quantity

# find popular products, sort product_sales by value in ascending order
popular_products = sorted(total_quantity_sold.items(), key=lambda x: x[1], reverse=True)

#Identifying high-value customers with unique customer_id and accumulating their total order value
high_value_customers = {}
for order in orders:
    customer_id = order["customer_id"]
    if customer_id in high_value_customers:
        order_value = sum(quantity * price for _, quantity, price in order["items"])
        previous_total_order_value = high_value_customers[customer_id][2]
        total_order_value = order_value + previous_total_order_value
        high_value_customers[customer_id] = (customer_id, order["cust_name"], total_order_value)
    else:
        total_order_value = sum(quantity * price for _, quantity, price in order["items"])
        high_value_customers[customer_id] = (customer_id, order["cust_name"], total_order_value)
# Sort high_value_customers by total_order_value in descending order
high_value_customers = dict(sorted(high_value_customers.items(), key=lambda x: x[1][2], reverse=True))

# Analyzing purchase behaviour by category
category_sales = {} 
for order in orders:
    for item in order["items"]:
        product_id, quantity, price = item
        category = products[product_id]["category"]
        if category in category_sales:
            category_sales[category] += quantity * price
        else:
            category_sales[category] = quantity * price
# Sort category_sales by value in ascending order
category_sales = dict(sorted(category_sales.items(), key=lambda x: x[1], reverse=True))

# Unique customers count and there names with set comprehension
unique_customers = {(order["cust_name"], order["customer_id"]) for order in orders}

# User interaction loop  
print("Welcome to the Customer Order Analysis Program!") 
while True:
    print("Please enter a number to choose an option:")
    print("1.Top five popular products that are frequently purchased.")
    print("2.Identify high-value customers who consistently make large purchases.")
    print("3.Analyze most profitable product categories.")
    print("4.Count total customers and list their names.")
    choice=input("Enter your choice (1-4): ")
    if choice=='1': 
        print("Top five popular products that are frequently purchased:")
        for product_id, quantity in popular_products[:5]:
            print(f"Product: {products[product_id]['name']}, Quantity Sold: {quantity}")   
    elif choice=='2':
        print("High-value customers who consistently make large purchases:")
         # Slice high-value customers dictionary to get only customer_id, cust_name and total_order_value
        sliced_dict_value = {}
        count=0
        for customer_id,cust_name, total_value in high_value_customers.values():
            count+=1
            if count>5:
                break
            print(f"Customer ID: {customer_id}, Name: {cust_name}, Total Order Value: {total_value}")
    elif choice=='3':
        print("Most profitable product categories:")
        for category, sales in category_sales.items():
            print(f"Category: {category}, Total Sales: {sales}")
    elif choice=='4':
        print(f"Total customers: {len(unique_customers)}")
        sorted_customers = sorted(unique_customers, key=lambda x: x[1])  # Sort by customer_id
        for cust_name,customer_id in sorted_customers:
            print(f"Customer ID: {customer_id}, Name: {cust_name}")
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
        continue
    continue_input = input("Do you want to continue? (yes/no): ").lower()
    if continue_input == 'yes':
        continue # Continue the while loop
    elif continue_input == 'no':
        print("Thank you for using the Customer Order Analysis Program!")
        print("Exiting program.")
        break # Exit the while loop 
    else:
        print("Invalid input. Exiting program.")
        break # Exit the while loop
        



                                                          



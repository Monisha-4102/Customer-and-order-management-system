"""
Customer & Order Management System
Author: Demo User
Purpose: Sample project for testing source code integration in a small company setting
"""

# -----------------------------
# Global Variables
# -----------------------------
company_name = "Reliance AI Solutions"
customers = []   # list of Customer objects
orders = []      # list of Order objects


# -----------------------------
# Classes
# -----------------------------
class Customer:
    def __init__(self, customer_id: int, name: str, email: str, phone: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Customer {self.customer_id}: {self.name}, {self.email}, {self.phone}"


class Order:
    def __init__(self, order_id: int, customer: Customer, items: list, total_amount: float):
        self.order_id = order_id
        self.customer = customer
        self.items = items  # list of strings (product names)
        self.total_amount = total_amount

    def __str__(self):
        return (f"Order {self.order_id} for {self.customer.name} | "
                f"Items: {', '.join(self.items)} | Total: ₹{self.total_amount:.2f}")


# -----------------------------
# Functions
# -----------------------------
def add_customer(customer_id: int, name: str, email: str, phone: str):
    customer = Customer(customer_id, name, email, phone)
    customers.append(customer)
    print(f"✅ Customer {name} added successfully!")


def create_order(order_id: int, customer_id: int, items: list, total_amount: float):
    # Find customer
    customer = None
    for c in customers:
        if c.customer_id == customer_id:
            customer = c
            break

    if not customer:
        print(f"⚠️ Customer with ID {customer_id} not found!")
        return

    order = Order(order_id, customer, items, total_amount)
    orders.append(order)
    print(f"🛒 Order {order_id} created for {customer.name}.")


def display_all_customers():
    print(f"\n--- {company_name} Customers ---")
    for c in customers:
        print(c)
    print("---------------------------------")


def display_all_orders():
    print(f"\n--- {company_name} Orders ---")
    for o in orders:
        print(o)
    print("---------------------------------")


# -----------------------------
# Main Execution
# -----------------------------
if __name__ == "__main__":
    # Add some customers
    add_customer(1, "Alice Johnson", "alice@example.com", "9876543210")
    add_customer(2, "Bob Smith", "bob@example.com", "8765432109")

    # Create orders
    create_order(101, 1, ["Laptop", "Mouse"], 55000.75)
    create_order(102, 2, ["Keyboard"], 1200.50)

    # Display data
    display_all_customers()
    display_all_orders()

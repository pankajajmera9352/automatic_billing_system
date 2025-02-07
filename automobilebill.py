import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import random

# Create the main window
root = tk.Tk()
root.title("Automobiles Billing Software")
root.geometry("500x600")

# Define functions
def generate_bill():
    current_date = datetime.now().strftime("%Y-%m-%d")
    bill_no = random.randint(1, 100)
    customer_name = customer_name_entry.get()
    vehicle_name = vehicle_name_entry.get()

    items_list = []
    total_amount = 0

    try:
        for i in range(int(items_entry.get())):
            item_name = items_entries[i].get()
            item_price = float(price_entries[i].get())
            items_list.append(f"{item_name} - ₹{item_price}")
            total_amount += item_price
        bill_text.set(f"**** BILL ****\n"
                      f"Date: {current_date}\n"
                      f"Bill No: {bill_no}\n"
                      f"Customer: {customer_name}\n"
                      f"Vehicle: {vehicle_name}\n"
                      f"Items:\n" + "\n".join(items_list) +
                      f"\nTotal: ₹{total_amount}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid inputs.")

# Function to add item fields dynamically
def create_items_entries():
    global items_entries, price_entries
    items_frame = tk.Frame(root)
    items_frame.pack(pady=10)
    items_entries = []
    price_entries = []

    for i in range(int(items_entry.get())):
        tk.Label(items_frame, text=f"Item {i + 1}").grid(row=i, column=0, padx=5, pady=5)
        item_entry = tk.Entry(items_frame)
        item_entry.grid(row=i, column=1, padx=5, pady=5)
        items_entries.append(item_entry)

        tk.Label(items_frame, text="Price").grid(row=i, column=2, padx=5, pady=5)
        price_entry = tk.Entry(items_frame)
        price_entry.grid(row=i, column=3, padx=5, pady=5)
        price_entries.append(price_entry)


header_label = tk.Label(root, text="**** AUTOMOBILES BILLING SOFTWARE SYSTEM ****\n"
                                   "---- MADE BY PANKAJ AJMERA ----", 
                        font=('Arial', 16, 'bold'),  # Larger font for emphasis
                        fg='black',  # Text color
                        bg='lightblue',  # Background color
                        justify='center')
header_label.pack(pady=10)

# Service Center Label with improved formatting
service_center_label = tk.Label(root, text="--- ANIT AUTO SERVICE CENTER ---\n"
                                           "MR: KULDEEP AJMERA\n"
                                           "MOBILE: 9928842159, 9024451240", 
                                 font=('Arial', 12, 'italic'),  # Italic for style
                                 fg='black',  # Text color
                                 bg='lightgray',  # Background color
                                 justify='center')
service_center_label.pack(pady=10)
print("MADE BY PANKAJ AJMERA")
print("Service Center: ANIT AUTO SERVICE CENTER\nMR: KULDEEP AJMERA\nMOBILE: 9928842159, 9024451240")


tk.Label(root, text="Customer Name", bg="lightblue").pack(pady=5)
customer_name_entry = tk.Entry(root, bg="lightyellow")
customer_name_entry.pack(pady=5)


tk.Label(root, text="Vehicle Name", bg="lightpink").pack(pady=5)
vehicle_name_entry = tk.Entry(root, bg="lightblue")
vehicle_name_entry.pack(pady=5)

tk.Label(root, text="Number of Items").pack(pady=5)
items_entry = tk.Entry(root)
items_entry.pack(pady=5)

add_items_button = tk.Button(root, text="Add Items", command=create_items_entries)
add_items_button.pack(pady=10)

generate_bill_button = tk.Button(root, text="Generate Bill", command=generate_bill)
generate_bill_button.pack(pady=10)

bill_text = tk.StringVar()
bill_label = tk.Label(root, textvariable=bill_text, font=('Arial', 12), justify='left')
bill_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()

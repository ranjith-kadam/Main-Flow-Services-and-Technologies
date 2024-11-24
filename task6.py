#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
from tkinter import messagebox

 
root = tk.Tk()
root.title("Billing and Invoice System")
root.geometry("600x600")

 
def generate_invoice():
    customer_name = entry_customer_name.get()
    customer_email = entry_customer_email.get()
    product_name = entry_product_name.get()
    product_price = entry_product_price.get()
    product_quantity = entry_product_quantity.get()

    
    if not customer_name or not customer_email or not product_name or not product_price or not product_quantity:
        messagebox.showerror("Input Error", "Please fill all fields.")
        return

    try:
        product_price = float(product_price)
        product_quantity = int(product_quantity)
    except ValueError:
        messagebox.showerror("Input Error", "Price and Quantity must be valid numbers.")
        return

    
    total_price = product_price * product_quantity

     
    invoice_details = f"Customer: {customer_name}\n"
    invoice_details += f"Email: {customer_email}\n"
    invoice_details += f"Product: {product_name}\n"
    invoice_details += f"Price: {product_price}\n"
    invoice_details += f"Quantity: {product_quantity}\n"
    invoice_details += f"Total: {total_price}\n"

    messagebox.showinfo("Invoice Generated", invoice_details)

# Frame for customer details
frame_customer_details = tk.Frame(root, padx=20, pady=10)
frame_customer_details.pack(fill="x")

label_customer_name = tk.Label(frame_customer_details, text="Customer Name:")
label_customer_name.grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_customer_name = tk.Entry(frame_customer_details)
entry_customer_name.grid(row=0, column=1, padx=5, pady=5)

label_customer_email = tk.Label(frame_customer_details, text="Customer Email:")
label_customer_email.grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_customer_email = tk.Entry(frame_customer_details)
entry_customer_email.grid(row=1, column=1, padx=5, pady=5)

# Frame for product entry
frame_product_entry = tk.Frame(root, padx=20, pady=10)
frame_product_entry.pack(fill="x")

label_product_name = tk.Label(frame_product_entry, text="Product Name:")
label_product_name.grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_product_name = tk.Entry(frame_product_entry)
entry_product_name.grid(row=0, column=1, padx=5, pady=5)

label_product_price = tk.Label(frame_product_entry, text="Product Price:")
label_product_price.grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_product_price = tk.Entry(frame_product_entry)
entry_product_price.grid(row=1, column=1, padx=5, pady=5)

label_product_quantity = tk.Label(frame_product_entry, text="Product Quantity:")
label_product_quantity.grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_product_quantity = tk.Entry(frame_product_entry)
entry_product_quantity.grid(row=2, column=1, padx=5, pady=5)

# Frame for billing and invoice generation
frame_billing = tk.Frame(root, padx=20, pady=20)
frame_billing.pack(fill="x")

generate_invoice_button = tk.Button(frame_billing, text="Generate Invoice", command=generate_invoice)
generate_invoice_button.pack()

# Start the Tkinter main loop
root.mainloop()


# In[ ]:





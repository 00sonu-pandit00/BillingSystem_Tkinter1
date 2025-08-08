import tkinter as tk
from tkinter import messagebox

items = []

def add_item():
    name = entry_name.get()
    try:
        price = float(entry_price.get())
        qty = int(entry_qty.get())
        total = price * qty
        items.append((name, price, qty, total))
        update_bill()
        entry_name.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        entry_qty.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Invalid price or quantity")

def update_bill():
    text_bill.delete("1.0", tk.END)
    text_bill.insert(tk.END, f"{'Item':<10}{'Price':<10}{'Qty':<10}{'Total':<10}\n")
    text_bill.insert(tk.END, "-" * 40 + "\n")
    subtotal = 0
    for name, price, qty, total in items:
        text_bill.insert(tk.END, f"{name:<10}{price:<10}{qty:<10}{total:<10}\n")
        subtotal += total

    # Read discount and tax input
    try:
        discount_pct = float(entry_discount.get())
    except:
        discount_pct = 0
    try:
        tax_input = float(entry_tax.get())
    except:
        tax_input = 0

    discount_amt = subtotal * (discount_pct / 100)
    gst = (subtotal - discount_amt) * 0.18
    grand_total = subtotal - discount_amt + gst + tax_input

    text_bill.insert(tk.END, "-" * 40 + "\n")
    text_bill.insert(tk.END, f"{'Subtotal':<30}{subtotal:.2f}\n")
    text_bill.insert(tk.END, f"{'Discount (' + str(discount_pct) + '%)':<30}{discount_amt:.2f}\n")
    text_bill.insert(tk.END, f"{'GST (18%)':<30}{gst:.2f}\n")
    text_bill.insert(tk.END, f"{'Other Tax':<30}{tax_input:.2f}\n")
    text_bill.insert(tk.END, f"{'Grand Total':<30}{grand_total:.2f}\n")

def clear_all():
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_qty.delete(0, tk.END)
    entry_discount.delete(0, tk.END)
    entry_tax.delete(0, tk.END)
    text_bill.delete("1.0", tk.END)
    items.clear()

# UI setup
root = tk.Tk()
root.title("Billing System with GST, Discount & Tax")
root.geometry("550x600")

tk.Label(root, text="Item Name").grid(row=0, column=0, padx=10, pady=5, sticky='w')
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Price").grid(row=1, column=0, padx=10, pady=5, sticky='w')
entry_price = tk.Entry(root)
entry_price.grid(row=1, column=1)

tk.Label(root, text="Quantity").grid(row=2, column=0, padx=10, pady=5, sticky='w')
entry_qty = tk.Entry(root)
entry_qty.grid(row=2, column=1)

tk.Label(root, text="Discount (%)").grid(row=3, column=0, padx=10, pady=5, sticky='w')
entry_discount = tk.Entry(root)
entry_discount.grid(row=3, column=1)

tk.Label(root, text="Other Tax (₹)").grid(row=4, column=0, padx=10, pady=5, sticky='w')
entry_tax = tk.Entry(root)
entry_tax.grid(row=4, column=1)

tk.Button(root, text="Add Item", command=add_item).grid(row=5, column=0, columnspan=2, pady=10)
tk.Button(root, text="Clear All", command=clear_all).grid(row=6, column=0, columnspan=2)

text_bill = tk.Text(root, width=64, height=20)
text_bill.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

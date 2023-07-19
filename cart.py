import tkinter as tk

class Node:
    def __init__(self, item_id, quantity, price):
        self.item_id = item_id
        self.quantity = quantity
        self.price = price
        self.next = None


class ShoppingCartGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Shopping Cart")
        self.window.configure(bg="lightgrey")
        
        self.item_label = tk.Label(self.window, text="Item Name:")
        self.item_label.pack()
        self.item_entry = tk.Entry(self.window)
        self.item_entry.pack()

        self.quantity_label = tk.Label(self.window, text="Quantity:")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(self.window)
        self.quantity_entry.pack()

        self.price_label = tk.Label(self.window, text="Price:")
        self.price_label.pack()
        self.price_entry = tk.Entry(self.window)
        self.price_entry.pack()

        self.add_button = tk.Button(self.window, text="Add Item", command=self.add_item,bg="green")
        self.add_button.pack()
        
        self.remove_label = tk.Label(self.window, text="Item Name to remove:")
        self.remove_label.pack()
        self.remove_entry = tk.Entry(self.window)
        self.remove_entry.pack()

        self.remove_button = tk.Button(self.window, text="Remove Item", command=self.remove_item, bg='red')
        self.remove_button.pack()

        self.update_label = tk.Label(self.window, text="Item Name to update:")
        self.update_label.pack()
        self.update_entry = tk.Entry(self.window)
        self.update_entry.pack()

        self.update_quantity_label = tk.Label(self.window, text="New Quantity:")
        self.update_quantity_label.pack()
        self.update_quantity_entry = tk.Entry(self.window)
        self.update_quantity_entry.pack()

        self.update_button = tk.Button(self.window, text="Update Quantity", command=self.update_quantity)
        self.update_button.pack()

        self.view_button = tk.Button(self.window, text="View Cart", command=self.view_cart)
        self.view_button.pack()

        self.total_items_label = tk.Label(self.window, text="Total Items:")
        self.total_items_label.pack()
        self.total_items_value = tk.Label(self.window, text="0")
        self.total_items_value.pack()

        self.total_price_label = tk.Label(self.window, text="Total Price:")
        self.total_price_label.pack()
        self.total_price_value = tk.Label(self.window, text="0")
        self.total_price_value.pack()

        self.head = None

    def add_item(self):
        item_id = self.item_entry.get()
        quantity = int(self.quantity_entry.get())
        price = float(self.price_entry.get())
        if not self.head:
            self.head = Node(item_id, quantity, price)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(item_id, quantity, price)

        self.item_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)


    def remove_item(self):
        item_id = self.remove_entry.get()
        if not self.head:
            return

        if self.head.item_id == item_id:
            self.head = self.head.next

        else:
            prev = self.head
            current = self.head.next
            while current:
                if current.item_id == item_id:
                    prev.next = current.next
                    break
                prev = current
                current = prev.next
        self.remove_entry.delete(0, tk.END)


    def update_quantity(self):
        item_id = self.update_entry.get()
        quantity = int(self.update_quantity_entry.get())
        current = self.head
        while current:
            if current.item_id == item_id:
                current.quantity = quantity
                break
            current = current.next

        self.update_entry.delete(0, tk.END)
        self.update_quantity_entry.delete(0, tk.END)


    def calculate_total_items(self):
        total_items = 0
        current = self.head
        while current:
            total_items += current.quantity
            current = current.next
        return total_items

    def update_total_items(self):
        total_items = self.calculate_total_items()
        self.total_items_value.config(text=str(total_items))

    def calculate_total_price(self):
        total_price = 0
        current = self.head
        while current:
            total_price += current.quantity * current.price
            current = current.next
        return total_price

    def update_total_price(self):
        total_price = self.calculate_total_price()
        self.total_price_value.config(text=str(total_price))

    def view_cart(self):
        cart_window = tk.Toplevel(self.window)
        cart_window.title("Shopping Cart")

        cart_label = tk.Label(cart_window, text="Cart Items:")
        cart_label.pack()

        cart_text = tk.Text(cart_window, height=10, width=50)
        cart_text.pack()

        current = self.head
        while current:
            cart_text.insert(tk.END, f"Item Name: {current.item_id}, Quantity: {current.quantity}, Price: {current.price*current.quantity}\n")
            current = current.next

        total_items = self.calculate_total_items()
        total_price = self.calculate_total_price()

        self.total_items_value.config(text=str(total_items))
        self.total_price_value.config(text=str(total_price))


    def run(self):
        self.window.mainloop()


# Example usage:
cart = ShoppingCartGUI()
cart.run()

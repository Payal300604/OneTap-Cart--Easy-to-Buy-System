import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk
import webbrowser
import urllib.parse
import datetime

# Sample product data
products = {
    "Women": {
        "Tops": [("Floral Top", 499), ("Silk Blouse", 699), ("Crop Top", 399), ("Tank Top", 299), ("Denim Shirt", 599)],
        "Bottoms": [("Jeans", 999), ("Skirt", 599), ("Leggings", 399), ("Palazzo", 499), ("Shorts", 299)]
    },
    "Men": {
        "Shirts": [("Formal Shirt", 799), ("Casual Shirt", 599), ("T-Shirt", 399), ("Hoodie", 999), ("Jacket", 1499)],
        "Bottoms": [("Jeans", 899), ("Trousers", 799), ("Shorts", 499), ("Trackpants", 599), ("Chinos", 699)]
    },
    "Kids": {
        "Tops": [("Kid T-Shirt", 299), ("Kid Shirt", 399), ("Kid Hoodie", 499)],
        "Bottoms": [("Kid Shorts", 199), ("Kid Pants", 299), ("Kid Leggings", 249)]
    }
}

def open_whatsapp_chat(phone_number: str, bill_text: str):
    number = ''.join(ch for ch in phone_number if ch.isdigit())
    url = f"https://wa.me/{number}?text={urllib.parse.quote(bill_text)}"
    webbrowser.open(url)

class ShoppingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("XYZ Online Shopping App")
        self.root.geometry("600x550")

        self.cart = {}
        self.customer_info = {}
        self.frames = {name: tk.Frame(root) for name in ["welcome","category","subcategory","product","cart","customer","qr","thanks"]}
        self.current_cat = ""
        self.show_welcome()

    def clear_frames(self):
        for f in self.frames.values():
            f.pack_forget()

    def clear_widgets(self, frame):
        for w in frame.winfo_children():
            w.destroy()

    def show_welcome(self):
        self.clear_frames()
        f = self.frames["welcome"]; self.clear_widgets(f); f.pack(fill="both", expand=True)
        tk.Label(f, text="🛍️ Welcome to XYZ Online Shopping App", font=("Arial", 18, "bold")).pack(pady=120)
        tk.Button(f, text="Continue ➡️", font=("Arial", 14), command=self.show_category).pack()

    def show_category(self):
        self.clear_frames()
        f = self.frames["category"]; self.clear_widgets(f); f.pack(fill="both", expand=True)
        tk.Label(f, text="Select Category", font=("Arial", 16, "bold")).pack(pady=20)
        for label, key in [("👩 Women","Women"),("👨 Men","Men"),("🧒 Kids","Kids"),("🛍️ View All","All")]:
            tk.Button(f, text=label, font=("Arial",14), width=20, command=lambda k=key: self.show_subcategory(k)).pack(pady=7)
        tk.Button(f, text="🛒 View Cart", font=("Arial",12), command=self.show_cart).pack(pady=15)

    def show_subcategory(self, category):
        self.clear_frames()
        self.current_cat = category
        f = self.frames["subcategory"]; self.clear_widgets(f); f.pack(fill="both", expand=True)
        tk.Label(f, text=f"{category} Categories", font=("Arial", 16, "bold")).pack(pady=15)
        subs = set()
        if category == "All":
            for cat in products.values(): subs.update(cat.keys())
        else:
            subs = products[category].keys()
        for sub in sorted(subs):
            tk.Button(f, text=sub, font=("Arial", 13), width=20, command=lambda s=sub: self.show_products(category, s)).pack(pady=5)
        tk.Button(f, text="⬅️ Back", command=self.show_category).pack(pady=15)

    def show_products(self, category, subcat):
        self.clear_frames()
        f = self.frames["product"]; self.clear_widgets(f); f.pack(fill="both", expand=True)
        tk.Label(f, text=f"{subcat} Collection", font=("Arial", 16, "bold")).pack(pady=10)
        items = []
        if category == "All":
            for cat in products.values(): items += cat.get(subcat, [])
        else:
            items = products[category][subcat]
        for name, price in items:
            fr = tk.Frame(f); fr.pack(pady=3)
            tk.Label(fr, text=f"{name} - ₹{price}", font=("Arial",12)).pack(side=tk.LEFT, padx=10)
            qty = tk.Spinbox(fr, from_=1, to=10, width=5); qty.pack(side=tk.LEFT)
            tk.Button(fr, text="Add to Cart", command=lambda n=name,p=price,q=qty: self.add_to_cart(n,p,q)).pack(side=tk.LEFT,padx=10)
        tk.Button(f, text="⬅️ Back", command=lambda: self.show_subcategory(category)).pack(pady=10)
        tk.Button(f, text="🛒 View Cart", command=self.show_cart).pack()

    def add_to_cart(self, name, price, qty_widget):
        qty = int(qty_widget.get())
        self.cart[(name, price)] = self.cart.get((name, price), 0) + qty
        messagebox.showinfo("Added", f"{qty} x {name} added to cart!")

    def show_cart(self):
        self.clear_frames()
        f = self.frames["cart"]; self.clear_widgets(f); f.pack(fill="both", expand=True)
        tk.Label(f, text="🛒 Cart Summary", font=("Arial",16,"bold")).pack(pady=10)

        self.total = 0
        frame_center = tk.Frame(f); frame_center.pack(pady=5)
        tk.Label(frame_center, text=f"{'Item':<20}{'Qty':<5}{'Rate':<7}{'Subtotal':<8}", font=("Courier",12,"underline")).pack()
        for (name,price),qty in self.cart.items():
            sub = price*qty; self.total+=sub
            tk.Label(frame_center, text=f"{name[:18]:<20}{qty:<5}{price:<7}{sub:<8}", font=("Courier",12)).pack()
        tk.Label(f, text=f"\nTotal Amount: ₹{self.total}", font=("Arial",14,"bold")).pack(pady=10)
        tk.Button(f, text="Proceed to Checkout", command=self.show_customer_details).pack(pady=7)
        tk.Button(f, text="⬅️ Back to Categories", command=self.show_category).pack(pady=5)

    def show_customer_details(self):
        self.clear_frames()
        f = self.frames["customer"]; self.clear_widgets(f); f.pack(fill="both", expand=True)
        tk.Label(f, text="Customer Details", font=("Arial",16,"bold")).pack(pady=20)
        tk.Label(f, text="Name:", font=("Arial",12)).pack(); name_e=tk.Entry(f,width=30); name_e.pack()
        tk.Label(f, text="WhatsApp No (+ country):", font=("Arial",12)).pack(pady=10)
        num_e=tk.Entry(f,width=30); num_e.pack()
        def save_and_qr():
            name, num = name_e.get().strip(), num_e.get().strip()
            if not name or not num or not num.isdigit(): messagebox.showerror("Error","Enter valid details."); return
            self.customer_info={"name":name,"mob":num}; self.generate_qr()
        tk.Button(f, text="Generate QR", command=save_and_qr).pack(pady=20)
        tk.Button(f, text="⬅️ Back to Cart", command=self.show_cart).pack()

    def generate_qr(self):
        self.clear_frames()
        f = self.frames["qr"]; self.clear_widgets(f); f.pack(fill="both", expand=True)
        data = f"XYZ Shop\nCustomer: {self.customer_info['name']}\nAmount: ₹{self.total}"
        img = qrcode.make(data); img.save("payment_qr.png")
        tk.Label(f, text="Scan QR to Pay", font=("Arial",16)).pack(pady=10)
        qr_img = ImageTk.PhotoImage(Image.open("payment_qr.png").resize((220,220)))
        tk.Label(f, image=qr_img).pack(); f.qr_img = qr_img
        tk.Button(f, text="✅ Payment Done", command=self.prepare_whatsapp).pack(pady=10)
        tk.Button(f, text="⬅️ Back to Customer", command=self.show_customer_details).pack()

    def prepare_whatsapp(self):
        bill = ["🧾 XYZ Shopping Bill", "-"*30]
        for (name,price),qty in self.cart.items():
            bill.append(f"{name} x{qty} @₹{price} = ₹{price*qty}")
        bill.append("-"*30); bill.append(f"Total: ₹{self.total}")
        bill.append("Thank You!")
        open_whatsapp_chat(self.customer_info["mob"], "\n".join(bill))
        self.show_thanks()

    def show_thanks(self):
        self.clear_frames()
        f = self.frames["thanks"]; self.clear_widgets(f); f.pack(fill="both", expand=True)
        tk.Label(f, text="🙏 Thank You!", font=("Arial",18,"bold")).pack(pady=40)
        tk.Label(f, text="We hope to see you again.", font=("Arial",14)).pack(pady=10)
        tk.Label(f, text="Please leave your feedback:", font=("Arial",12)).pack(pady=10)
        fb = tk.Text(f, width=40, height=5); fb.pack()
        tk.Button(f, text="Submit Feedback", command=lambda: messagebox.showinfo("Received","Thanks!")).pack(pady=10)
        tk.Button(f, text="🛑 Exit", fg="red", command=self.root.quit).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingApp(root)
    root.mainloop()

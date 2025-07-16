# 🛍️ OneTap-Cart--Easy-to-Buy-System

A user-friendly, Tkinter-based Python application that simulates a real-time online shopping experience. The app allows users to browse products, add them to a cart, make payments through QR codes, and receive bills directly via WhatsApp.

---

## 📝 Description
This Python GUI application allows users to browse products, add them to a cart, and complete a purchase through QR code payments. The final bill is shared via WhatsApp.

## 📌 Project Highlights

- 🗂️ Browse categories: Women, Men, Kids, or View All
- 👗 View subcategories with a curated list of products
- 🛒 Add multiple items with quantity control
- 💰 Auto-calculated cart summary and checkout flow
- 📇 Customer detail form (Name & WhatsApp)
- 🔐 Secure QR code generation for payment
- 💬 WhatsApp integration to send a digital bill
- 🙏 Thank-you screen with feedback collection

---

## 📁 Project Structure

OneTap-Cart--Easy-to-Buy-System/
├── main.py # Main application code
├── payment_qr.png # QR code (generated at runtime)
├── README.md # Documentation file


---

## 🖥️ Tech Stack

- **Python 3.x**
- **Tkinter** – GUI creation
- **qrcode** – Dynamic QR code generation
- **Pillow** – Image processing for QR display
- **webbrowser & urllib** – WhatsApp integration

---

## 📲 WhatsApp Bill Sharing
After a successful purchase, the app:

Generates a digital bill

Opens a WhatsApp chat with the customer’s number

Pre-fills the chat box with the bill using wa.me link

Make sure the system has internet access and WhatsApp is installed or accessible via browser.

----

##🧾 Features in Detail

| Feature              | Description                                             |
| -------------------- | ------------------------------------------------------- |
| Category Selection   | Women, Men, Kids, or all at once                        |
| Subcategory Browsing | Tops, Bottoms, Shirts, etc.                             |
| Add to Cart          | Quantity input + dynamic item addition                  |
| Cart Summary         | Shows all items with subtotal and grand total           |
| Checkout             | Collects name and WhatsApp number                       |
| QR Payment           | Displays a scannable QR image for the total bill        |
| WhatsApp Bill        | Opens WhatsApp with a message containing a full invoice |
| Feedback Form        | Users can submit feedback after checkout                |

-----

🚀 How to Run

1. Clone the repository:
git clone https://github.com/your-username/xyz-online-shopping-app.git
cd xyz-online-shopping-app

2. Run the Python script:
python main.py

3. Start shopping!

-----

## 📦 Requirements

Before running the project, install the required dependencies:

```bash
pip install pillow qrcode
   


🌾 FarmHub — Online Farm Product Management System

FarmHub link : https://github.com/kvishnukumarreddy/FarmHub

An Online Farm Product Management System developed using Django that:

1. Allows farmers and customers to register/login securely
2. Enables farmers to add and manage farm products
3. Displays available agricultural products for customers
4. Provides search and product viewing functionality
5. Includes admin panel for complete product/user management

---

🚀 Quick Start

1. Clone the repository

git clone https://github.com/kvishnukumarreddy/FarmHub.git
cd FarmHub

2. Install dependencies

pip install django

3. Run migrations & start server

python manage.py migrate

python manage.py runserver

4. Open browser

Go to http://127.0.0.1:8000

---

## 📂 Project Structure

```text
FarmHub
- manage.py
- db.sqlite3
- farmhub
   - settings.py
   - urls.py
   - wsgi.py
- core
   - models.py
   - views.py
   - urls.py
   - templates
      - home.html
      - register.html
      - login.html
      - dashboard.html
      - products.html


---

🌟 Main Features

- Farmer Registration and Login
- Customer Registration and Login
- Add Farm Products
- View Available Products
- Product Search Functionality
- Admin Dashboard
- User Authentication
- Product Management

---

🛠 Tech Stack

- Backend : Django, Python 3.10+
- Frontend : HTML, CSS, Bootstrap
- Database : SQLite3
- Authentication : Django Authentication System

---

🎯 Project Objective

The main objective of FarmHub is to provide a digital platform where farmers can directly upload and manage their agricultural products, and customers can easily browse farm goods online.

---

📌 Future Enhancements

- Online Payment Integration
- Product Ordering System
- Delivery Tracking
- Farmer Customer Chat
- Email Notifications

---



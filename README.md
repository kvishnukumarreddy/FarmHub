# 🌾 FarmHub — Online Farm Product Management System

FarmHub link : https://github.com/kvishnukumarreddy/FarmHub

An Online Farm Product Management System developed using Django that:

1. Allows farmers and customers to register/login securely
2. Enables farmers to add and manage farm products
3. Displays available agricultural products for customers
4. Provides search and product viewing functionality
5. Includes admin panel for complete product/user management

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/kvishnukumarreddy/FarmHub.git
cd FarmHub
2. Install dependencies
Bash
pip install django
3. Run migrations & start server
Bash
python manage.py migrate
python manage.py runserver
4. Open browser
Go to http://127.0.0.1:8000

📂 Project Structure
Bash
FarmHub/
├── manage.py
├── db.sqlite3
├── farmhub/                ← Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── core/                   ← Main application
    ├── models.py           ← Database models
    ├── views.py            ← Business logic
    ├── urls.py             ← URL routes
    └── templates/
        ├── home.html
        ├── register.html
        ├── login.html
        ├── dashboard.html
        └── products.html
🌟 Main Features
Farmer Registration and Login
Customer Registration and Login
Add Farm Products
View Available Products
Product Search Functionality
Admin Dashboard
User Authentication
Product Management
🛠 Tech Stack
Backend: Django, Python 3.10+
Frontend: HTML, CSS, Bootstrap
Database: SQLite3
Authentication: Django User Authentication
🔑 Modules Included
User Registration Module
User Login Module
Product Add/View Module
Search Module
Admin Management Module

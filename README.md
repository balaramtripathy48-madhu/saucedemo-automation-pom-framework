SauceDemo Automation POM Framework

A web automation testing framework built using Python, Selenium, Pytest, and Page Object Model (POM) design pattern.

This project automates real-time user scenarios on the SauceDemo application such as login, inventory, cart, checkout, logout, and end-to-end purchase flow.

---

🚀 Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- VS Code / PyCharm
- Git & GitHub

---

📁 Project Structure

saucedemo-automation-pom-framework/
│── pages/
│   ├── saucedemo_login.py
│   ├── saucedemo_inventory.py
│   ├── saucedemo_cart.py
│   ├── saucedemo_checkout.py
│   └── saucedemo_logout.py
│
│── tests/
│   ├── conftest.py
│   ├── test_end_to_end_flow.py
│   └── test_logout.py
│
│── requirements.txt
│── README.md

---

✅ Features Covered

- Login functionality
- Add products to cart
- Remove products from cart
- Continue shopping
- Checkout process
- Logout functionality
- End-to-end purchase flow
- Assertions & validations
- Reusable fixtures with Pytest

---

▶️ Installation

Clone Repository

git clone https://github.com/your-username/saucedemo-automation-pom-framework.git
cd saucedemo-automation-pom-framework

Install Dependencies

pip install -r requirements.txt

---

▶️ Run Tests

Run All Tests

pytest -v -s

Run Specific Test

pytest tests/test_end_to_end_flow.py -v -s

---

🧪 Test Scenarios

Login

- Enter username
- Enter password
- Verify successful login

Inventory

- Add products to cart
- Open cart page

Cart

- Remove product
- Continue shopping
- Add another product

Checkout

- Enter first name
- Enter last name
- Enter postal code
- Finish order

Logout

- Open menu
- Click logout

---

📌 Framework Design

Page Object Model (POM)

Each page contains:

- Locators
- Page actions
- Reusable methods

Benefits:

- Better code readability
- Easy maintenance
- Reusability
- Scalable framework design

---

📈 Future Enhancements

- HTML Reports
- Screenshot on failure
- Data-driven testing
- Cross-browser testing
- CI/CD Integration (GitHub Actions / Jenkins)

---

👨‍💻 Author

Balaram Tripathy
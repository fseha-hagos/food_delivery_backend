# 🍔 Food Delivery Backend Application 🚚

## Description
This project is a food delivery application built using Django. It includes features for managing food items, orders, payments, and user reviews.

🛠️ Tech Stack
**Backend Framework:**
   - Django (Python)
   - Django REST Framework (for building APIs)
**Database:**
   - SQLite (default for development)
   - PostgreSQL (recommended for production)
**Authentication:**
   - Django's built-in authentication system
   - Token-based authentication (optional)
**Other Tools:**
   - Django Admin (for backend management)
   - Django REST Framework (for API development)
**Python (v3.8 or higher)**

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd food_delivery_backend
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:
   - Configure your database settings in `food_delivery_backend/settings.py`.

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## 🚀 Usage
Access the API endpoints at `http://localhost:8000/`.

## API Endpoints
- **Food**
  - `GET /food`: Retrieve all food items.
  - `POST /food`: Add a new food item.
  - `PUT /food/<id>`: Update a food item.
  - `DELETE /food/<id>`: Delete a food item.

- **Menu**
  - `GET /menu`: Retrieve all menu items.
  - `POST /menu`: Add a new menu item.
  - `PUT /menu/<id>`: Update a menu item.
  - `DELETE /menu/<id>`: Delete a menu item.

- **Categories**
  - `GET /catagory`: Retrieve all categories.
  - `GET /catagory/<id>`: Retrieve a specific category.

- **Delivery Staff**
  - `GET /delivery-staff`: Retrieve all delivery staff.
  - `POST /delivery-staff`: Add a new delivery staff member.
  - `PUT /delivery-staff/<id>`: Update a delivery staff member.
  - `DELETE /delivery-staff/<id>`: Delete a delivery staff member.

- **Orders**
  - `GET /order`: Retrieve all orders.
  - `POST /order`: Create a new order.
  - `PUT /order/<id>`: Update an order.
  - `DELETE /order/<id>`: Delete an order.

- **Order Items**
  - `GET /order-items`: Retrieve all order items.
  - `POST /order-items`: Add a new order item.
  - `PUT /order-items/<id>`: Update an order item.
  - `DELETE /order-items/<id>`: Delete an order item.

- **Deliveries**
  - `GET /delivery`: Retrieve all deliveries.
  - `POST /delivery`: Add a new delivery.
  - `PUT /delivery/<id>`: Update a delivery.
  - `DELETE /delivery/<id>`: Delete a delivery.

- **Payments**
  - `GET /payment`: Retrieve all payments.
  - `POST /payment`: Add a new payment.
  - `PUT /payment/<id>`: Update a payment.
  - `DELETE /payment/<id>`: Delete a payment.

- **Reviews**
  - `GET /review`: Retrieve all reviews.
  - `POST /review`: Add a new review.
  - `PUT /review/<id>`: Update a review.
  - `DELETE /review/<id>`: Delete a review.

## 🌟Models
- **Food**: Represents food items with attributes like name, address, and fee.
- **Delivery Staff**: Represents delivery staff with unique IDs and contact information.
- **Order**: Represents customer orders, including delivery status and total amount.
- **Menu**: Represents menu items with categories, images, and pricing.
- **Payment**: Represents payment transactions associated with orders.
- **Review**: Represents customer reviews for the food delivery service.

## 🤝 Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

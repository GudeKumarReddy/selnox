# Vendor Management System

This project is a Vendor Management System built with Django and Django REST Framework. It allows you to manage vendor profiles, track purchase orders, and calculate vendor performance metrics.

## Features

1. **Vendor Profile Management**
    - Create, list, retrieve, update, and delete vendor profiles.
2. **Purchase Order Tracking**
    - Create, list, retrieve, update, and delete purchase orders.
3. **Vendor Performance Evaluation**
    - Calculate metrics such as on-time delivery rate, quality rating, response time, and fulfillment rate.

## Setup Instructions

### Prerequisites

- Python 3.8+
- Pip (Python package installer)
- Virtualenv (Recommended)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/NameisGoaT/selnox.git
    cd vendor-management-system
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the database migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser to access the admin interface:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

### API Endpoints

#### Vendor Endpoints

- **Create a new vendor:** `POST /api/vendors/`
- **List all vendors:** `GET /api/vendors/`
- **Retrieve a specific vendor's details:** `GET /api/vendors/{vendor_id}/`
- **Update a vendor's details:** `PUT /api/vendors/{vendor_id}/`
- **Delete a vendor:** `DELETE /api/vendors/{vendor_id}/`
- **Retrieve a vendor's performance metrics:** `GET /api/vendors/{vendor_id}/performance`

#### Purchase Order Endpoints

- **Create a purchase order:** `POST /api/purchase_orders/`
- **List all purchase orders:** `GET /api/purchase_orders/`
- **Retrieve details of a specific purchase order:** `GET /api/purchase_orders/{po_id}/`
- **Update a purchase order:** `PUT /api/purchase_orders/{po_id}/`
- **Delete a purchase order:** `DELETE /api/purchase_orders/{po_id}/`

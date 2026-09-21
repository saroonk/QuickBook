# QuickBook — Event Booking Platform

QuickBook is a Django-based event booking platform developed as part of a Django Backend Developer machine test.

The application provides REST APIs for authentication, event browsing and booking, a binary referral network, vendor/event management, and a custom staff dashboard.

## Tech Stack

* Python
* Django
* Django REST Framework
* SQLite
* JWT Authentication
* HTML / CSS / Bootstrap
* JavaScript
* Swagger / OpenAPI

---

## Features

### Authentication

* User registration
* User login
* User logout
* JWT token-based authentication
* Protected APIs
* User management
* Referral code support during registration

### Event Booking

* Browse events
* View event details
* Search and filter events
* Book event tickets
* Cancel bookings
* View booking history
* Ticket/seat availability validation
* Prevention of invalid bookings
* Protection against concurrent booking conflicts

### Binary Referral Network

* Unique referral code for registered users
* Registration using a referral code
* Automatic placement in the binary referral network
* Referral tree retrieval
* Root user retrieval
* Left and right referral team counts
* Referral validation and error handling

### Custom Staff Dashboard

A custom staff dashboard is provided instead of using Django's built-in Admin interface.

Staff users can:

* View dashboard statistics
* Manage vendors
* Add and update events
* Search and filter events
* View users
* View detailed user information
* View user referral trees
* Search referral trees
* Use pagination

The dashboard is responsive and protected so that only staff users can access it.

---

# Setup Instructions

## 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <PROJECT_FOLDER>
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Apply Database Migrations

The project uses SQLite.

```bash
python manage.py migrate
```

## 5. Create a Staff/Superuser

The custom staff dashboard requires a staff user.

Run:

```bash
python manage.py createsuperuser
```

Follow the prompts to create the account.

The created superuser can be used to log in to the custom staff dashboard.

## 6. Start the Development Server

```bash
python manage.py runserver
```

The application will normally be available at:

```text
http://127.0.0.1:8000/
```

---

# Staff Dashboard

## **Dashboard URL**

### **http://127.0.0.1:8000/dashboard/**

**This is the main management dashboard for staff users.**

After creating the superuser, open:

```text
http://127.0.0.1:8000/dashboard/
```

and log in using the staff/superuser credentials.

The dashboard provides access to:

* Dashboard statistics
* Vendor management
* Event management
* User management
* User details
* Referral tree

Only authenticated staff users can access the dashboard.

> **Note:** Django's built-in Admin panel is not used as the management interface. The application uses a custom dashboard at `/dashboard/`.

---

# API Documentation

The project includes **Swagger / OpenAPI documentation** for the REST APIs.

After starting the development server, access the Swagger documentation at:

### **http://127.0.0.1:8000/api/docs/**

The Swagger interface allows you to explore and test the available APIs directly from the browser.

The documented APIs include functionality for:

* User registration
* Login and logout
* User/account management
* Authentication
* Event management
* Event booking
* Booking cancellation
* Booking history
* Referral registration
* Referral tree
* Referral statistics
* Other available REST API operations

Protected APIs can be tested through Swagger by providing the required authentication token.

---

## OpenAPI Schema

The generated OpenAPI schema is available at:

### **http://127.0.0.1:8000/api/schema/**

This can be used to inspect the API specification directly.

---

# Authentication

The API uses token-based authentication.

After obtaining an authentication token through the API, protected endpoints can be accessed using the authentication mechanism provided in the Swagger interface.

Swagger can be used to:

1. Register a user.
2. Log in and obtain the required token.
3. Authorize the Swagger session.
4. Test protected APIs.
5. Test event booking and referral functionality.

The exact API endpoints and request/response formats are available in the Swagger documentation.

---

# Booking

The booking system supports:

* Event ticket booking
* Ticket availability validation
* Invalid booking prevention
* Booking cancellation
* Customer booking history
* Concurrent booking protection

The booking logic validates availability before confirming a booking to maintain consistent seat/ticket counts.

---

# Referral Network

Each registered user receives a unique referral code.

Users can register using another user's referral code, after which they are automatically placed within the binary referral network.

The referral functionality supports:

* Binary referral tree
* Root user identification
* Left team count
* Right team count
* Referral tree retrieval
* Referral validation

All available referral APIs can be tested through the Swagger documentation.

---

# Staff Management

The custom dashboard provides management functionality for:

### Vendors

* Add vendors
* View vendors
* Update vendor information

### Events

* Add events
* View events
* Update events
* Search events
* Filter events

### Users

* View users
* View detailed user information
* View referral tree
* Search referral tree
* Pagination

### Dashboard Statistics

The dashboard displays:

* Total Customers
* Total Vendors
* Total Events
* Total Bookings

---

# Database

The project uses **SQLite** as required by the machine-test specification.

After cloning the project, run:

```bash
python manage.py migrate
```

to create the required database tables.

---

# Requirements

All required Python dependencies are included in:

```text
requirements.txt
```

Install them using:

```bash
pip install -r requirements.txt
```

---

# Quick Start

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <PROJECT_FOLDER>

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then access:

### **Staff Dashboard**

**http://127.0.0.1:8000/dashboard/**

### **Swagger API Documentation**

**http://127.0.0.1:8000/api/docs/**

### **OpenAPI Schema**

**http://127.0.0.1:8000/api/schema/**

Use the superuser credentials for the staff dashboard, and use Swagger to explore and test the REST APIs.

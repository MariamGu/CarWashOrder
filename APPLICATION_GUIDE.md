# Car Wash Order Console Application Guide

## Overview

The Car Wash Order Console Application is a Python-based console application designed to manage car wash orders. It allows users to create orders, view available washers, and manage car wash types. The application supports two roles: admin and user.

## Features

- **Admin Panel:**
  - Add new washers with details such as name, experience, and mobile number.
  - Add or update car wash types with details such as type, duration, and price.

- **User Panel:**
  - View available washers.
  - View available car wash types.
  - Create a new order.
  - Visualize the transaction process.
  - Get immediate feedback about the order and transaction details.

## Setup and Installation

1. **Clone the Repository:**
   ```sh
   git clone <repository_url>
   cd CarWashOrder

## Usage
### Running the Application
To run the application, execute the main.py file:

```sh
python main.py
```
## Admin Panel

### Login as Admin:

When prompted, enter your username, role as `admin` and mobile number.

### Admin Menu Options:

- **Add Washer:** Follow the prompts to add a new washer with name, experience, and mobile number.
- **Add Car Wash Type:** Follow the prompts to add or update a car wash type with type, duration, and price.
- **Exit:** Exit the admin panel.

## User Panel

### Login as User:

When prompted, enter your username, role as `user`, mobile number, and initial balance.

### User Menu Options:

- **Create Order:** Follow the prompts to create a new order.
  - **View Available Washers:** Display a list of available washers.
  - **View Car Wash Types:** Display a list of available car wash types.
  - **Proceed with Order:** Enter the Car Wash ID and Washer ID to create an order. The application will visualize the transaction process and provide feedback.
  - **Cancel:** Cancel the order creation process.
- **Exit:** Exit the user panel.

## Example Scenarios

### Scenario 1: Adding a New Washer (Admin)

#### Login as Admin:

- Username: `admin`
- Role: `admin`
- Mobile: `1234567890`


#### Add Washer:

- Choose option `1` from the admin menu.
- Enter washer details:
  - Name: `John Doe`
  - Experience: `5`
  - Mobile: `0987654321`
- Washer added successfully.

### Scenario 2: Creating a New Order (User)

#### Login as User:

- Username: `user`
- Role: `user`
- Mobile: `1122334455`
- Initial Balance: `100`

#### Create Order:

- Choose option `1` from the user menu.
- View available washers (option `1` in the create order menu).
- View available car wash types (option `2` in the create order menu).
- Proceed with order (option `3` in the create order menu).
  - Enter Car Wash ID: `1`
  - Enter Washer ID: `1`
- The transaction process is visualized, and the user receives feedback with order details.

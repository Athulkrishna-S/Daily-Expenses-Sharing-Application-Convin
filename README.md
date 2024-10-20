# Daily Expenses Sharing Application

A web application built with Flask and MongoDB to manage shared expenses among users. The application allows users to create accounts, log in, add expenses, and view their expenses and balance sheets.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Creating the `.env` File](#creating-the-env-file)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)


## Features

- User authentication (login/logout)
- User account creation
- Add and manage expenses
- Split expenses equally, by percentage, or by exact amounts
- Download balance sheet as a PDF
- View individual user expenses

## Technologies Used

- Flask: Web framework for Python
- Flask-JWT-Extended: For JWT authentication
- PyMongo: MongoDB integration for Flask
- dotenv: To manage environment variables
- MongoDB: NoSQL database for storing user data and expenses

## Setup Instructions

**1. Clone the repository:**

```sh
git clone https://github.com/Athulkrishna-S/Daily-Expenses-Sharing-Application-Covin.git

cd Daily-Expenses-Sharing-Application-Covin
```

**2. Install the required packages:**

```sh
pip install -r requirements.txt
```

**3. Create the .env file:**

Create a .env file in the root of the project directory and add the following environment variables

```sh
JWT_SECRET_KEY=<your_secret_key>   # Secret key for JWT
MONGO_URI=<your_mongo_connection_uri>  # MongoDB connection URI
DB_NAME=<your_database_name>  # Name of your MongoDB database

```
**4. Run the application:**
```sh
python app.py

```
## Api-Endpoints

https://www.apidog.com/apidoc/shared-a310629b-fb24-4fd5-950e-1212e6f25e21
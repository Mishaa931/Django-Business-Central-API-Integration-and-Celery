# Django Business Central Integration

## Overview

A Django application designed to integrate with the Business Central API. This project includes RESTful APIs for managing customer data, Celery for asynchronous task processing, and custom functionalities for data synchronization.

## Features

- **RESTful APIs**: CRUD operations for customer data.
- **Celery Integration**: Background task processing for data synchronization.
- **Environment Configuration**: Secure management of sensitive settings using `.env`.

## Installation

1. **Clone the Repository**

       git clone https://github.com/yourusername/django-business-central-integration.git
       cd django-business-central-integration
   
2. **Create and Activate a Virtual Environment**

       python -m venv venv
       source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Create and Activate a Virtual Environment**

        pip install -r requirements.txt

4. **Set Up Environment Variables**
   
   Create a .env file in the root directory and add your configuration settings:

        SECRET_KEY=your_secret_key
        DEBUG=True
        ALLOWED_HOSTS=127.0.0.1,localhost
        
        DB_NAME=your_db_name
        DB_USER=your_db_user
        DB_PASSWORD=your_db_password
        DB_HOST=localhost
        DB_PORT=5432
   
6. **Run Migrations**

        python manage.py migrate

7. **Start the Development Server**

       python manage.py runserver


## Usage
* API Endpoints: Access the RESTful APIs at http://127.0.0.1:8000/api/.
* Celery Tasks: Use Celery for background tasks and data synchronization.

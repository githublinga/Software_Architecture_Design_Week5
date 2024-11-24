# Software_Architecture_Design_Week5

# Lingareddy Project - Hello World Django App

## Requirements
Ensure the following are installed on your system before proceeding:
- **Python 3.x**
- **Django Framework**

If Django is not installed, follow the instructions below to install it.

## Overview
This is a simple Django application that responds with a "Hello World" message in JSON format when accessed via a web browser.

## Steps to Set Up and Run the Application

### 1. Clone the Project Repository
First, clone the project repository and navigate to the project directory:


git clone https://github.com/githublinga/Software_Architecture_Design_Week5.git
cd Lingareddy_project

### 2. Set Up a Virtual Environment
Create a virtual environment to keep project dependencies isolated:


python3 -m venv venv
source venv/bin/activate


### 3. Install Required Packages
Install Django, which is required to run this application:


pip install Django


### 4. Run the Application

#### Step 1: Navigate to the Project Directory

Ensure you are in the main project directory where `manage.py` is located:


cd Lingareddy_project


#### Step 2: Apply Database Migrations
Initialize the database by applying the migrations:


python manage.py migrate


#### Step 3: Start the Development Server
Run the Django development server:


python manage.py runserver


#### Step 4: Access the Application
Open your web browser and navigate to the following URL:


http://127.0.0.1:8000/hello/


## Expected Output
When you access the `/hello/` route, you should see a JSON response like this:

{
  "message": "Hello World"
}

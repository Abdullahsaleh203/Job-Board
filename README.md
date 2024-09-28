# Django-Job-Board

## Project Overview
Django-Job-Board is a web application built using Django that allows users to post and search for job listings. The project aims to provide a platform for job seekers and employers to connect and find suitable job opportunities.

## Features
- User authentication and authorization
- Job posting and searching
- Responsive design using Bootstrap
- Image upload for job listings
- Easy-to-use admin interface

## Installation

### Prerequisites
- Python 3.x
- Django 5.0.7
- Other dependencies listed in `requirements.txt`

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Abdullahsaleh203/Django-Job-Board.git
   cd Django-Job-Board
Create a virtual environment and activate it:

```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    Install the dependencies:
```
---
```bash
    pip install -r requirements.txt
    Run the migrations:
```

```bash
    python manage.py migrate
```
- Start the development server:
```
    python manage.py runserver
```
Open your browser and navigate to http://127.0.0.1:8000.

Usage
Register as a new user or log in with existing credentials.
Create job listings and manage them through the admin interface.
Search for job listings using various filters.
Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to follow the code style guidelines and write tests for your code.

License
This project is licensed under the MIT License.

#Dependencies
The project uses the following dependencies:


``` 
    asgiref 3.8.1
    beautifulsoup4 4.12.3
    Django 5.0.7
    django-bootstrap4 24.3
    pillow 10.4.0
    soupsieve 2.5
    sqlparse 0.5.1
    typing_extensions 4.12.2
    tzdata 2024.1
```

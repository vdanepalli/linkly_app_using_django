# [Linkly App Using Django](https://linkly-app-using-django.onrender.com/)

A practice project for building a simple link management application using Django. This project demonstrates the use of Django for backend development and HTML for frontend rendering.

## Features

- Add, edit, and delete links
- View a list of all saved links
- Responsive design using Django templates

## Technologies Used

- **Backend**: Python (Django framework)
- **Frontend**: HTML

## Getting Started

Follow these steps to set up the project locally.

### Prerequisites

Make sure you have the following installed:

- Python 3.7 or higher
- pip (Python package manager)
- Virtualenv (optional but recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/vdanepalli/linkly_app_using_django.git
   cd linkly_app_using_django
   ```
2. Create and activate a virtual environment:
   ```bash
    # On Linux/MacOS
    python3 -m venv venv
    source venv/bin/activate
    
    # On Windows
    python -m venv venv
    venv\Scripts\activate
   ```
3. Install the project dependencies:
   ```bash
    pip install -r requirements.txt
   ```
5. Run migrations to set up the database:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```
7. Open the application in your browser:
   ```Code
   http://127.0.0.1:8000/
   ```

----- 

Happy Coding! 🚀

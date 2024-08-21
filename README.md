# Starchat Django Project

Starchat is a web application built using the Django framework. It features user authentication, group management, and post creation capabilities.

## Setup Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Parsa-SadeghiAsl/StarChat.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd starchat
   ```

3. **Create a Virtual Environment** (Optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run Migrations** to create the necessary database tables:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser Account** for administrative purposes:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the Application** in your web browser:
   Open `http://127.0.0.1:8000/` in a web browser to access the Starchat application.

## Features

- **User Accounts**: Users can create accounts, log in, and log out.
- **Group Management**: Users can join or leave groups, and view posts within those groups.
- **Post Creation**: Users can create new posts within their joined groups.


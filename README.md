# csci262-group-project

## Project Overview

This project is a Flask web application designed to demonstrate various security features for a login system. The application includes multifactor authentication (MFA), password policies, hash salting, and potentially behavioral analytics and passkeys. The goal is to develop an overall defense solution against password cracking.

## Project Structure

```text
project_root/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── forms.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── dashboard.html
│   └── utils/
│       └── security.py
│
├── tests/
│   └── test_routes.py
├── requirements.txt
├── config.py
└── run.py
```

### app/

- `__init__.py`: Initialises the Flask application and sets up configurations.
- `routes.py`: Contains the route definitions for the application, including login, registration, and MFA.
- `forms.py`: Defines the forms used in the application, such as `LoginForm` and `RegisterForm`.
- `templates/`: Contains the HTML templates for rendering the web pages.
  - `base.html`: Base template that other templates extend.
  - `login.html`: Template for the login page.
  - `register.html`: Template for the registration page.
  - `dashboard.html`: Template for the dashboard page after successful MFA.
- `utils/`: Contains utility modules.
  - `security.py`: Contains security-related functions such as password hashing and verification.

### tests/

- `test_routes.py`: Contains unit tests for the routes in the application.

### requirements.txt

Lists the Python dependencies required for the project.

### config.py

Contains configuration settings for the Flask application.

### run.py

Entry point for running the Flask application.

## Setup Instructions

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/csci262-group-project.git
   cd csci262-group-project
   ```

2. **Create a virtual environment**:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```sh
   python run.py
   ```

5. **Access the application**:
   Open your web browser and navigate to `http://127.0.0.1:5000`.

## Features

- **Login**: Users can log in with their credentials.
- **Registration**: New users can register with a unique user ID and password.
- **Multifactor Authentication (MFA)**: After successful login, users are prompted to complete an MFA challenge.
- **Password Policies**: Enforces strong password policies.
- **Hash Salting**: Uses salt and pepper for hashing passwords to enhance security.
- **Behavioral Analytics** (Planned): Tracks user behavior to detect anomalies.
- **Passkeys** (Planned): Implements WebAuthn for passkey support.
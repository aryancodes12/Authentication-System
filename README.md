# User Registration System

A Python-based command-line user registration system with data persistence using JSON storage.

## 📋 Overview

A learning project building towards a complete authentication system. This is the registration module with JSON persistence, input validation, and a clean CLI interface. Part of my journey to master Python fundamentals through real-world projects.

## ✨ Features

- User registration with validation (email format, unique usernames, password strength)
- JSON-based data persistence with auto-incrementing user IDs
- Color-coded Rich console output for better UX
- Password confirmation and security checks

## 🛠️ Requirements

- Python 3.6+ (tested on latest version)
- Rich library

## 📦 Installation

1. Clone or download this repository

2. Install the required dependency:
```bash
pip install rich
```

## 🚀 Usage

```bash
python user_registration.py
```

Follow the prompts to register users. Data automatically saves to `user_data.json`.

## 💾 Data Storage

User data is stored in JSON format with the following structure:

```json
{
    "u001": {
        "Name": "John Doe",
        "Email": "john@example.com",
        "Username": "johndoe",
        "Password": "password123"
    }
}
```

## ⚠️ Important Notes

- **Security**: Passwords stored in plain text (educational purposes only)
- Previous data auto-loads on startup
- User IDs increment automatically (u001, u002, etc.)



## 🔮 Roadmap

```
🎯 Phase 2: User login system with authentication
🎯 Phase 3: Admin dashboard to view/manage all users
🔐 Security: Password hashing (bcrypt)
⚡ Session management
```

---

## 👤 Author

**Aryan Gupta**  
B.Sc. Data Science & AI Student <br>
📧 EMAIL: aryansynthh@gmail.com  
💼 [LinkedIn](https://www.linkedin.com/in/aryan-rajesh-gupta-386449360)

*Learning by building. One project at a time.* 🚀
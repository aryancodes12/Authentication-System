# 🔐 User Authentication System

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![Maintenance](https://img.shields.io/badge/maintained-yes-brightgreen.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

A robust Python-based command-line authentication system with JSON persistence, built as a learning project to master software development fundamentals.

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Roadmap](#️-development-roadmap) • [Contributing](#-contributing)

</div>

---

## 📋 Overview

A comprehensive learning project building towards a complete authentication system with user management and admin capabilities. Currently features a fully functional registration module with modular architecture, input validation, and an elegant CLI interface.

**Project Goal**: Transform fundamental Python concepts into a production-ready authentication system through iterative development and best practices.

## ✨ Features

### Current Features ✅
- ✔️ **User Registration** - Complete registration workflow with validation
- ✔️ **Email Validation** - RFC-compliant email format checking
- ✔️ **Username Uniqueness** - Prevents duplicate usernames
- ✔️ **Password Strength** - Enforces secure password requirements
- ✔️ **Password Confirmation** - Double-entry verification
- ✔️ **JSON Persistence** - Automatic data storage and retrieval
- ✔️ **Auto-incrementing IDs** - Sequential user ID generation (u001, u002, ...)
- ✔️ **Rich Console UI** - Color-coded, user-friendly terminal interface
- ✔️ **Modular Architecture** - Clean separation of concerns

### Coming Soon 🚀
- 🔜 User login and authentication
- 🔜 Session management
- 🔜 Admin dashboard
- 🔜 Password hashing (bcrypt)
- 🔜 MySQL database integration

## 📁 Project Structure
```
Authentication-System/
│
├── auth/                      # Core authentication module
│   ├── register.py           # User registration logic
│   ├── storage.py            # Data persistence layer
│   ├── ui.py                 # Console UI components
│   └── validators.py         # Input validation functions
│
├── data/                      # Data storage directory
│   └── user_data.json        # User database (auto-generated)
│
├── main.py                    # Application entry point
├── requirements.txt           # Python dependencies
├── .gitignore                # Git ignore rules
└── README.md                  # Project documentation
```

## 🛠️ Tech Stack

- **Language**: Python 3.6+
- **UI Library**: Rich (terminal formatting)
- **Data Storage**: JSON (migrating to MySQL in Phase 6)
- **Security**: bcrypt (planned for Phase 5)

## 📦 Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**
```bash
   git clone https://github.com/aryancodes12/Authentication-System.git
   cd Authentication-System
```

2. **Create virtual environment** (recommended)
```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

## 🚀 Usage

### Starting the Application
```bash
python main.py
```

### Registration Flow

1. Launch the application
2. Select "Register" from the main menu
3. Enter your details:
   - First Name
   - Last Name
   - Email Address
   - Username (must be unique)
   - Password (with strength requirements)
   - Confirm Password
4. Registration confirmation displayed
5. Data automatically saved to `data/user_data.json`

## ⚠️ Important Security Notes

> **⚠️ WARNING**: This is an educational project currently in development.

- 🔓 **Passwords are stored in plain text** - FOR LEARNING PURPOSES ONLY
- 🚫 **DO NOT use in production** without implementing proper security
- ✅ **Phase 5** will implement bcrypt password hashing
- 🔐 **Phase 6** will migrate to MySQL with proper security practices

## 🗺️ Development Roadmap

### ✅ Phase 1: Registration Logic
**Status**: Complete ✓
- [x] User registration functionality
- [x] Input validation (email, username, password)
- [x] JSON data persistence
- [x] Auto-incrementing user IDs

### ✅ Phase 1.5: UI Polishing
**Status**: Complete ✓
- [x] Rich library integration
- [x] Color-coded console output
- [x] Enhanced user experience
- [x] Professional formatting

### ✅ Phase 2: Refactoring
**Status**: Complete ✓
- [x] Modular architecture implementation
- [x] Separation of concerns (UI, logic, storage, validation)
- [x] Code organization and cleanup
- [x] Documentation improvements

### 🔄 Phase 3: User Login & Authentication
**Status**: In Progress 🚧
- [ ] User login system
- [ ] Session management
- [ ] User dashboard with profile view
- [ ] Account settings
- [ ] Logout functionality

### 📋 Phase 4: Admin Dashboard
**Status**: Planned 📅
- [ ] Admin authentication and authorization
- [ ] View all registered users
- [ ] User management (edit/delete users)
- [ ] System statistics and analytics
- [ ] Role-based access control

### 🔐 Phase 5: Password Security
**Status**: Planned 📅
- [ ] Implement bcrypt password hashing
- [ ] Secure password storage
- [ ] Password strength meter
- [ ] Password reset functionality
- [ ] Security best practices

### 🗄️ Phase 6: Database Migration
**Status**: Planned 📅
- [ ] Design MySQL database schema
- [ ] Implement MySQL connection
- [ ] CRUD operations with MySQL
- [ ] Data migration script from JSON
- [ ] Database optimization

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/aryancodes12/Authentication-System/issues).

### How to Contribute

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 🎓 Learning Outcomes

Through this project, I've gained hands-on experience with:

- ✅ Modular code architecture and design patterns
- ✅ Input validation and data sanitization
- ✅ File I/O and JSON data handling
- ✅ Terminal UI/UX design with Rich library
- ✅ Git version control and project management
- 🔜 Authentication and authorization systems
- 🔜 Password hashing and security best practices
- 🔜 Database design and SQL operations

## 👤 Author

**Aryan Gupta**

- 🎓 B.Sc. Data Science & AI Student
- 📧 Email: [aryansynthh@gmail.com](mailto:aryansynthh@gmail.com)
- 💼 LinkedIn: [Aryan Rajesh Gupta](https://www.linkedin.com/in/aryan-rajesh-gupta-386449360)
- 🐙 GitHub: [@aryancodes12](https://github.com/aryancodes12)

## 💖 Acknowledgments

- Thanks to the [Rich library](https://github.com/Textualize/rich) for beautiful terminal formatting
- Inspired by real-world authentication systems
- Built as part of my journey to master Python and software development

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

*Learning by building. One project at a time.* 🚀

Made with ❤️ by [Aryan Gupta](https://github.com/aryancodes12)

</div>

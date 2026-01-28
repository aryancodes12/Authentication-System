# 🔐 Python CLI User Registration System

A simple standalone **Command Line User Registration System** built using Python.

This project allows users to register accounts with input validation and stores data locally using a JSON file.

It is designed as a beginner-friendly backend project to practice:
- File handling
- JSON storage
- Input validation
- Modular Python structure
- CLI application development

---

## ✨ Features

- 🧑 Register multiple users
- 📧 Email validation
- 🔁 Unique username checking
- 🔒 Password rules (minimum 8 characters)
- 🆔 Auto-generated user IDs (u001, u002, ...)
- 💾 Persistent storage using JSON
- 🎨 Colored terminal output support (ANSI / Rich)

---

## Program flow

```bash

Start
 ↓
Load existing users (if any)
 ↓
Register new user
 ↓
Validate inputs
 ↓
Generate user ID
 ↓
Save to dictionary
 ↓
Write to JSON file
 ↓
Display all users
```

---

## 🚀 Future Improvements

Ideas to enhance the system:
- 🔐 Hash passwords (bcrypt / hashlib)
- 🔑 Login & authentication system
- 📧 Regex-based email validation
- 🗄 SQLite database support
- 🎨 Full Rich-based UI
- 🧪 Unit testing
- 📦 Convert into installable package
- 🌐 API version using FastAPI/Flask

---

## 👨‍💻 Author

Aryan
BSc Data Science & AI Student
Learning by building real-world Python projects 🚀

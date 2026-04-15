# 🔐 Authentication System

A terminal-based authentication system built from scratch in Python with a cyberpunk-themed UI. This project demonstrates core authentication concepts, clean code architecture, and modern terminal interface design.

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Status](https://img.shields.io/badge/status-active-success)
![Phase](https://img.shields.io/badge/phase-3%20complete-orange)

## ✨ Features

### 🔐 **Core Authentication**
- ✅ User registration with comprehensive validation
- ✅ Secure login with username OR email
- ✅ Session management (login/logout)
- ✅ Password strength requirements (8+ chars, numbers, special characters)
- ✅ Login attempt limiting (3 attempts maximum)
- ✅ Input sanitization and validation

### 👤 **User Management**
- ✅ View profile information
- ✅ Update display name
- ✅ Change password with validation
- ✅ Secure logout with session cleanup

### 🎨 **Terminal UI**
- ✅ Cyberpunk-themed interface with neon colors
- ✅ 25+ reusable UI components
- ✅ Color-coded feedback (success/error/warning)
- ✅ Smooth transitions and loading animations
- ✅ Professional panel layouts
- ✅ 15 customizable themes (Cyberpunk default)

## 🏗️ Project Structure
```
Authentication-System/
│
├── auth/                      # Core authentication module
│   ├── __init__.py           # Package initialization
│   ├── dashboard.py          # User dashboard & profile management
│   ├── login.py              # Login logic & authentication
│   ├── register.py           # User registration flow
│   ├── sessions.py           # Session state management
│   ├── storage.py            # JSON data persistence
│   ├── theme.py              # Color themes (15 options)
│   ├── ui.py                 # 25+ reusable UI components
│   └── validators.py         # Input validation functions
│
├── user_data.json            # User database (auto-generated)
├── main.py                   # Application entry point
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

### 🎯 **Architecture Principles**
- **Modular Design:** Each file has a single, clear responsibility
- **Separation of Concerns:** UI, logic, validation, and storage layers are separated
- **Reusability:** 25+ UI components used throughout the application
- **Clean Code:** Readable, maintainable, and well-documented code

## 🚀 Installation & Usage

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/aryancodes12/Authentication-System.git
cd Authentication-System
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python main.py
```

## 📖 User Guide

### Main Menu
On launch, you'll see three options:
```
[1] Login
[2] Register new User
[3] Admin Access
[4] Exit
```

### Registration Process
1. Select option `2` from the main menu
2. Enter your details:
   - **First Name** and **Last Name**
   - **Email Address** (must contain @gmail.com)
   - **Username** (must be unique, lowercase)
   - **Password** (requirements below)
   - **Confirm Password**

**Password Requirements:**
- Minimum 8 characters
- At least one number
- At least one special character (@_!#$%^&*)
- Cannot match username

### Login
1. Select option `1` from the main menu
2. Enter your **username** or **email**
3. Enter your **password**
   - You have 3 attempts before being locked out
   - Failed attempts show remaining tries

### Dashboard Features
After successful login:

**[1] View Profile** - Display your account information
- Name, email, username
- Account status

**[2] Update Name** - Change your display name
- Enter new name
- Instant update

**[3] Change Password** - Update your password
- Verify current password
- Enter new password (must meet requirements)
- Confirm new password

**[4] Delete Account** - Coming in Phase 4

**[5] Logout** - End your session safely

## 🎨 UI Components

The system includes 25+ professionally designed components:

### Display Components
- `header()` - Cyberpunk ASCII art header with neon effects
- `info_panel()` - Information display panels
- `menu_panel()` - Numbered menu options
- `profile_table()` - User profile data table
- `space()` - Spacing between elements
- `rule()` - Horizontal divider lines

### Feedback Components
- `success()` / `success_panel()` - Green success messages
- `error()` / `error_panel()` - Red error messages
- `warn()` / `warn_panel()` - Yellow warnings
- `info()` - Cyan information messages

### Interactive Components
- `get_input()` - Text input with colored prompts
- `get_choice()` - Menu selection
- `wait_for_enter()` - Pause for user acknowledgment

### Animation Components
- `status()` - Animated spinner with message
- `fake_loading()` - Progress bar animation
- `animated_logo()` - Startup ASCII art animation

## 🎨 Themes

**Active Theme:** Cyberpunk (Neon colors on dark background)

| Element | Color | Usage |
|---------|-------|-------|
| **Primary** | Bright Cyan | Headers, prompts, borders |
| **Secondary** | Bright Magenta | Accents, dividers |
| **Accent** | Bright Yellow | Highlights, menu choices |
| **Success** | Bright Green | Success messages, checkmarks |
| **Error** | Bright Red | Error messages, failures |
| **Warning** | Yellow | Warnings, validation errors |
| **Info** | Cyan | Information, hints |
| **Muted** | Dim Cyan | Less important text |

**Additional Themes Available:**
Sunset, Ocean, Forest, Hacker Terminal, Dark Purple, Fire, Rainbow, Electric, Monochrome, Dracula, Nord, Solarized, Gruvbox, Monokai

> To switch themes: Open `auth/theme.py` and uncomment your preferred theme

## 🔐 Security Implementation

### Current Security Features
✅ Password validation (length, complexity)  
✅ Login attempt limiting (3 tries)  
✅ Session state management  
✅ Input sanitization  
✅ Username uniqueness checks  

### ⚠️ Security Limitations (Educational Project)

**DO NOT use in production without implementing:**
- ❌ Password hashing (currently plain text)
- ❌ Database encryption
- ❌ HTTPS/SSL
- ❌ Rate limiting
- ❌ Email verification
- ❌ Two-factor authentication
- ❌ Password reset mechanism

These features are planned for future phases (see Roadmap).

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Language** | Python 3.6+ | Core application logic |
| **Terminal UI** | [Rich](https://github.com/Textualize/rich) | Beautiful terminal formatting |
| **Data Storage** | JSON | User data persistence |
| **Architecture** | Modular | Clean separation of concerns |

**Dependencies:**
```
rich==13.7.0
```

## 📊 Project Statistics

- **Total Lines of Code:** 600+
- **Python Files:** 8 modular files
- **UI Components:** 25+
- **Themes Available:** 15
- **Commits:** 25+
- **Development Time:** 3 weeks
- **Current Phase:** 3 (Complete)

## 🗺️ Development Roadmap

### ✅ Phase 1: Registration (Complete)
- User registration system
- Input validation
- JSON-based storage

### ✅ Phase 2: Refactoring (Complete)
- Modular architecture
- Separated UI components
- Theme system implementation
- Code cleanup and documentation

### ✅ Phase 3: Authentication & Dashboard (Complete)
- Login system with retry logic
- Session management
- User dashboard
- Profile viewing
- Name updates
- Password changes
- Secure logout
- Account Delete 

### 🚧 Phase 4: Admin Features (Next)
- Admin login credentials
- View all registered users 
- Delete user accounts 
- [ ] User search and filtering

### 📋 Phase 5: Enhanced Security (Planned)
- [ ] Password hashing with bcrypt
- [ ] Password strength meter
- [ ] Security questions for recovery
- [ ] Account lockout after failed attempts
- [ ] Password history (prevent reuse)

### 📋 Phase 6: Database Integration (Planned)
- [ ] MySQL database setup
- [ ] Database schema design
- [ ] Migration from JSON to MySQL
- [ ] Connection pooling
- [ ] Prepared statements

## 🐛 Known Issues

- Email validation currently only accepts @gmail.com addresses 
- Passwords stored in plain text *(will be fixed with bcrypt hashing in Phase 5)*
- Session doesn't persist after application restart
- No password recovery mechanism yet

## 💡 What I Learned

Building this project taught me:
- ✅ Authentication flow patterns
- ✅ Input validation strategies
- ✅ Session state management
- ✅ Modular code architecture
- ✅ Terminal UI/UX design principles
- ✅ Security considerations in auth systems
- ✅ Error handling and user feedback
- ✅ Code reusability through components

## 🤝 Contributing

This is a personal learning project, but feedback and suggestions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 👨‍💻 Author

**Aryan Gupta**
- 🎓 B.Sc. Data Science & AI Student
- 📧 Email: [aryansynthh@gmail.com](mailto:aryansynthh@gmail.com)
- 💼 LinkedIn: [Aryan Rajesh Gupta](https://www.linkedin.com/in/aryan-rajesh-gupta-386449360)
- GitHub: [@aryancodes12](https://github.com/aryancodes12)
- Project: [Authentication-System](https://github.com/aryancodes12/Authentication-System)

*First-year B.Sc. Data Science & AI Student*

## 🙏 Acknowledgments

- [Rich](https://github.com/Textualize/rich) library by Will McGugan for beautiful terminal formatting
- Python community for excellent documentation and learning resources
- Inspiration from real-world authentication systems


---

⭐ **If you found this project helpful, please consider giving it a star!**

Built with 💙 by [Aryan Gupta](https://github.com/aryancodes12) | Learning by Building 🚀

*Last Updated: 15 April 2026 | Phase 3 Complete* 

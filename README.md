Password Strength Checker 🔒🛡️

Overview

The Password Strength Checker is a Python-based tool that evaluates the strength of a password according to various criteria. It checks whether the password meets security standards such as length, complexity, and variety of character types (uppercase, lowercase, numbers, and symbols). 🔑

Features ✨

Length Check: Ensures the password has a minimum and maximum length. 📏

Uppercase Letters: Password must contain at least one uppercase letter. 🔠

Lowercase Letters: Password must contain at least one lowercase letter. 🔡

Numerical Digits: Password must contain at least one numerical digit. 🔢

Special Characters: Password must contain at least one special character (e.g., @, #, $, etc.). ✨

Common Patterns: Detects if the password contains common words or patterns. 🔍

Installation ⚙️
Clone the repository to your local machine.

bash
Copy
git clone https://github.com/SyedaNabila559/Password-strength-checker/

Functions 🧑‍💻

check_password_strength(password: str) -> str: This function accepts a password and returns a strength score (e.g., 'Weak', 'Moderate', 'Strong') based on several checks. 🏅

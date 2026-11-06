# 🔐 Password Checker

A simple cybersecurity tool to check password strength and verify if it appears in known breaches.

## Features
- Strength scoring (Weak/Medium/Strong)
- Detects common weak passwords
- Optional HaveIBeenPwned API check
- Command-line usage

## Usage
```bash
python -m password_checker.cli          # asks for the password without showing it (recommended)
python -m password_checker.cli "YourPasswordHere"   # also works, but stays in your shell history
```

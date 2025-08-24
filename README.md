# SHA256 Hash Cracker 🔐

# Overview
The SHA256-PasswordCracker is a Python-based tool that automates the process of cracking a given SHA-256 hash by testing a list of commonly used passwords. Using the pwntools library, the script compares the hashed version of each password in the wordlist against the target hash. The tool is designed for educational purposes and penetration testing within authorized environments.

# Note
- Security and Ethical Notice: This script is intended for educational and ethical hacking purposes only. It must only be used in environments you own or have explicit permission to test. Do not use the provided code and techniques for illegal activities.

# Features
- Password List Reading: Reads passwords from a wordlist file (rockyou.txt by default).
- Automated Cracking Attempts: Iteratively hashes each password in the list and compares it against the provided target hash.
- Progress Reporting: Displays real-time progress during the cracking process.
- Success Detection: If the correct password is found, the script reports the success and stops further attempts.
- Failure Handling: If no match is found after testing all passwords, it notifies the user.

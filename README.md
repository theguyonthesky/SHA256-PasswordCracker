# SHA256 Hash Cracker 🔐

# Overview
The SHA256-PasswordCracker is a Python-based tool that automates the process of cracking a given SHA-256 hash by testing a list of commonly used passwords. Using the pwntools library, the script compares the hashed version of each password in the wordlist against the target hash. The tool is designed for educational purposes and penetration testing within authorized environments.

# Note
- Security and Ethical Notice: This script is intended for educational and ethical hacking purposes only. It must only be used in environments you own or have explicit permission to test. Do not use the provided code and techniques for illegal activities.

# Features
- Argument Validation: The script checks whether the correct number of arguments are provided. If not, it exits with an error message.
- Password List Reading: Reads passwords from a wordlist file (`rockyou.txt` by default).
- Automated Cracking Attempts: Iteratively hashes each password in the list and compares it against the provided target hash.
- Progress Reporting: Displays real-time progress during the cracking process.
- Success Detection: If the correct password is found, the script reports the success and stops further attempts.
- Failure Handling: If no match is found after testing all passwords, it notifies the user.

# How It Works
1. The script first checks if exactly one argument (the target SHA-256 hash) is provided via the command line using `sys.argv`. If not, it exits with an error message.

2. It opens the wordlist file (default `rockyou.txt`) and reads each password line by line.

3. For each password:
   - For each password, it strips any trailing newline characters and encodes the password.
   - It then hashes the password using SHA-256 and compares the result (`sha256sumhex`) to the provided target hash.
   - If the hash matches, the script reports success, displaying the cracked password and exits.

4. The script keeps track of how many attempts have been made and updates the progress accordingly.

5. If the password is found, the script terminates immediately using `exit()`. If no match is found after testing all passwords, the script notifies the user of the failure.
   
# Tools and Technologies Used
Python – Main programming language.

`pwntools` – Handles cryptographic funcions like hashing.

`sys` – Used for argument handling.

Linux (Kali) – Typical environment for running hash-cracking tools.

# Files
`hash_cracker.py`: The main Python script that performs the hash-cracking attack.

`rockyou.txt`: A wordlist file containing millions of commonly used passwords (You can use any .txt wordlist).

# How to Run
1. Clone or download this repository
2. Install the libraries: pip install pwntools (sys doesn't need to be installed, it's part of Python's standard library)
3. Place your wordlist file in the same directory as the script, or update the file path in the code.
4. Run the script using one of the following methods:
   - Terminal (macOS/Linux): 'python3 hash_cracker.py <target_hash>'
   - Windows (or IDEs like VS Code, PyCharm): 'python hash_cracker.py <target_hash>' or use the Run button

# Disclaimer
This project is created for research, ethical hacking, and educational purposes only. Unauthorized access to computer systems is illegal. Always ensure you have explicit permission before testing any systems. The developer is not responsible for any misuse of this code.

# Contribution and Feedback
Contributions, feedback, and issues can be submitted via the GitHub repository. Ensure that your interactions adhere to the GitHub Community Guidelines to maintain a respectful and collaborative environment.

# License
This project is licensed under the MIT License. Feel free to use or modify it for personal use or learning.
<br>**Stay safe and have fun! 😊**

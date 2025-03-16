# Cryptography Tasks

This repository contains two practical coding tasks demonstrating fundamental cryptographic operations: password hashing and symmetric encryption.

## Table of Contents

- [Task 1: Password Hashing](#task-1-password-hashing)
- [Task 2: Symmetric Encryption](#task-2-symmetric-encryption)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Task 1: Password Hashing

### Description
This task implements a function to hash passwords using the bcrypt algorithm. Password hashing is crucial for secure storage of user credentials, as it protects passwords even if the database is compromised.

#### Steps:
1. Set up a virtual environment by following the installation instructions.
2. Create a Python file called `password_hash.py`.
3. Use the bcrypt Python library to define a function that hashes a password string provided by the user.
4. Your function should first encode the user’s string before hashing.
5. Hash the password using bcrypt with a random salt.
6. Create a `requirements.txt` file containing all the dependencies for the project.
7. Deactivate the virtual environment once you have completed the task.

### Why it's important:
This task is crucial in cybersecurity, as it teaches how to safely store sensitive data like passwords. With the increasing importance of protecting user data from cyber threats, learning password hashing is a fundamental skill for any developer working on web applications.

### File: `password_hash.py`

This script defines a function `bcrypt_hasher` that takes a password string, encodes it, and applies the bcrypt hashing algorithm with a randomly generated salt.

---

## Task 2: Symmetric Encryption

### Description

This task demonstrates symmetric encryption and decryption using the Fernet implementation from the cryptography library. Symmetric encryption is essential for securing data in transit and at rest.

#### Steps:
1. Set up a virtual environment by following the installation instructions.
2. Research symmetric encryption.
3. Create a file named `encrypt.py`.
4. Define a function using the cryptography.fernet module that encrypts text with a provided key.
5. Create another function that decrypts the text using the same key.
6. Deactivate your virtual environment once the task is completed, and remember to delete the virtual environment folder.

### Why it's important:
Symmetric encryption is fundamental to data security and privacy. It ensures that both the sender and the receiver can protect and securely communicate sensitive data without exposure to third parties.

### File: `encrypt.py`

This script includes two functions:
1. `encrypt_text`: Encrypts a given text using a provided key.
2. `decrypt_text`: Decrypts the encrypted text using the same key.


---

## Installation

To run these scripts locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TasnimNiger/cryptography-tasks.git

2. **Navigate to the project directory**:
   cd cryptography-tasks

3. **Create and activate a virtual environment**:
   python -m venv venv
   source venv/bin/activate # On Windows use venv\Scripts\activate

4. **Install the required packages**:
   pip install -r requirements.txt

6. Ensure you have Python installed (version 3.6 or higher).


## Usage

Once the dependencies are installed, you can use the code for the tasks.

### Running Task 1:
Navigate to the directory containing the code for Task 1:
   cd task1

Run the password hashing script:
   python password_hash.py


### Running Task 2:
Navigate to the directory containing the code for Task 2:
   cd task2

Run the encryption script:
   python encrypt.py

### Example Output:
For Task 1 (Password Hashing)
![image](https://github.com/user-attachments/assets/e3059e62-0bdd-4ac3-930a-0ba9f85414b7)

For Task 2 (Symmetric Encryption)
![image](https://github.com/user-attachments/assets/be268d2b-0121-4066-a197-761164048c0b)


## Credits

This project was created and is maintained by [Tasnim Niger](https://github.com/TasnimNiger). The code and its organization are designed to help others learn essential concepts in cybersecurity and data encryption.


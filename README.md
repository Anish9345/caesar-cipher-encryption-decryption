# Caesar Cipher Encryption & Decryption

This project implements the **Caesar Cipher algorithm** to encrypt and decrypt text.  
The user can choose whether to encrypt or decrypt a message and can use either the **default Caesar Cipher shift (3)** or a **custom shift value**.

---

## 📌 What is Caesar Cipher?

Caesar Cipher is a classical cryptographic technique where each letter in the message is shifted by a fixed number of positions in the alphabet.

- Default shift used in Caesar Cipher: **3**
- Example:  
  - `A → D`  
  - `HELLO → KHOOR`

---

## ✨ Features

- Encrypt text using Caesar Cipher
- Decrypt encrypted text back to original form
- Default shift value **3** (as per Caesar Cipher algorithm)
- Option to use a **custom numeric shift**
- Supports:
  - Uppercase letters
  - Lowercase letters
  - Spaces and special characters (unchanged)
- Simple menu-driven program

---

## 🛠️ How the Program Works

1. User selects:
   - `1` → Encrypt  
   - `2` → Decrypt
2. User enters the message
3. User selects shift option:
   - `1` → Default shift (3)
   - `2` → Custom shift value (number only)
4. Program performs encryption or decryption accordingly

---

## ▶️ How to Run

1. Make sure Python is installed
2. Clone the repository:
   git clone https://github.com/your-username/caesar-cipher-encryption-decryption.git
3. Navigate to the project folder:
   cd caesar-cipher-encryption-decryption
4. Run the program:
   python caesar-cipher-encryption-decryption.py

## 🧪 Sample Output

Choose an option:
1. Encrypt
2. Decrypt
Enter your choice (1 or 2): 1

Enter the message: Hello World

Caesar Cipher uses a default shift of 3.
1. Use default shift (3)
2. Use custom shift
Enter your choice (1 or 2): 1

Encrypted Text: Khoor Zruog

## 📚 Concepts Used

- ASCII values
- Caesar Cipher algorithm
- Python built-in functions:
- ord()
- chr()
- Conditional statements
- Loops
- User input handling

## 🎯 Purpose of the Project

This project is created for learning and academic purposes to understand:

  - Basic cryptography concepts
  - Character encoding (ASCII)
  - Encryption and decryption logic



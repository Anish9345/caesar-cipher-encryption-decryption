def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result


def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char
    return result


# Menu for encryption or decryption
print("Choose an option:")
print("1. Encrypt")
print("2. Decrypt")

choice = int(input("Enter your choice (1 or 2): "))

message = input("Enter the message: ")

print("\nCaesar Cipher uses a default shift of 3.")
print("1. Use default shift (3)")
print("2. Use custom shift")

shift_choice = int(input("Enter your choice (1 or 2): "))

if shift_choice == 1:
    shift = 3
else:
    shift = int(input("Enter custom shift value (number only): "))

if choice == 1:
    print("Encrypted Text:", encrypt(message, shift))
elif choice == 2:
    print("Decrypted Text:", decrypt(message, shift))
else:
    print("Invalid choice!")

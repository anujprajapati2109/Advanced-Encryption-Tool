from cryptography.fernet import Fernet
import os

# Generate and save a key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("[+] Key generated and saved to secret.key")

# Load key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt file
def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    encrypted = f.encrypt(data)
    with open(filename + ".enc", "wb") as file:
        file.write(encrypted)
    print(f"[+] File encrypted: {filename}.enc")

# Decrypt file
def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    decrypted = f.decrypt(data)
    original_name = filename.replace(".enc", ".dec")
    with open(original_name, "wb") as file:
        file.write(decrypted)
    print(f"[+] File decrypted: {original_name}")

# Main menu
def main():
    while True:
        print("\n=== AES Encryption Tool ===")
        print("1. Generate Key")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            generate_key()
        elif choice == '2':
            key = load_key()
            filename = input("Enter file name to encrypt: ")
            encrypt_file(filename, key)
        elif choice == '3':
            key = load_key()
            filename = input("Enter file name to decrypt (e.g., file.txt.enc): ")
            decrypt_file(filename, key)
        elif choice == '4':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

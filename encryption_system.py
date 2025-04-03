from Crypto.Cipher import AES
import base64
import hashlib

def pad_key(key):
    return hashlib.sha256(key.encode()).digest()[:16]

def pad_data(data):
    padding_length = 16 - (len(data) % 16)
    return data + bytes([padding_length] * padding_length)

def unpad_data(data):
    return data[:-data[-1]]

def encrypt(data, key):
    key = pad_key(key)
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    padded_data = pad_data(data.encode())  
    encrypted_data = cipher.encrypt(padded_data)

    encrypted_output = base64.b64encode(iv + encrypted_data).decode()
    print("\n Encrypted Data (Copy & Share):", encrypted_output)
    print(" Encryption Key (Save this!):", key.hex(), "\n")

def decrypt(encrypted_data, key_hex):
    key = bytes.fromhex(key_hex)
    encrypted_data = base64.b64decode(encrypted_data)

    iv = encrypted_data[:16]
    encrypted_content = encrypted_data[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_content)

    print("\n Decrypted Message:", unpad_data(decrypted_data).decode(), "\n")

while True:
    print("\n 1: Encrypt a message")
    print(" 2: Decrypt a message")
    print(" 3: close encrypter/decrypter")
    
    choice = input("\nChoose an option (1/2/3): ").strip()

    if choice == "1":
        message = input("\nEnter the message to encrypt: ")
        key = input("Enter a secret key (any word or phrase): ")
        encrypt(message, key)
    elif choice == "2":
        encrypted_msg = input("\nPaste the encrypted data: ")
        key_hex = input("Enter the encryption key: ")
        decrypt(encrypted_msg, key_hex)
    elif choice == "3":
        print("\nthanks for using this ")
        break
    else:
        print("\n invalid option choose 1 2 or 3.")

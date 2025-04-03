import random
import os
import base64

# Generate a random encryption key
def generate_key(length):
    return os.urandom(length)

# Apply recursive fractal transformation to the data
def recursive_fractal(data, depth=5):
    if depth == 0:
        return data
    new_data = []
    for byte in data:
        new_data.append(byte)
        new_data.append(byte ^ 0xFF)  # XOR with 0xFF for variation
    return recursive_fractal(new_data, depth - 1)

# Apply random noise and XOR with key for better security
def noise_based_transformation(data, key):
    transformed = []
    for i, byte in enumerate(data):
        transformed.append(byte ^ key[i % len(key)])  # XOR with key
        transformed.append((byte + random.randint(1, 255)) % 256)  # Add random noise
    return bytearray(transformed)

# Apply chaotic transformation (Lorenz Attractor)
def lorenz_attractor(data, sigma=10, rho=28, beta=8/3, dt=0.01):
    x, y, z = random.random(), random.random(), random.random()
    transformed = []
    for _ in range(len(data)):
        dx = sigma * (y - x)
        dy = x * (rho - z) - y
        dz = x * y - beta * z
        x += dx * dt
        y += dy * dt
        z += dz * dt
        transformed.append(int((x + y + z) % 256))  # Convert to byte values
    return bytearray(transformed)

# Apply XOR substitution multiple times for enhanced encryption
def complex_xor_substitution(data, stages=5):
    transformed = data
    for _ in range(stages):
        transformed = bytearray([x ^ random.randint(0, 255) for x in transformed])  # Multiple XOR stages
    return transformed

# Encrypt the message using multiple transformation techniques
def encrypt(plaintext, key):
    byte_data = plaintext.encode()  # Convert plaintext to bytes
    encrypted_data = complex_xor_substitution(byte_data)
    encrypted_data = noise_based_transformation(encrypted_data, key)
    encrypted_data = recursive_fractal(encrypted_data)
    encrypted_data = lorenz_attractor(encrypted_data)
    return encrypted_data

# Encode the encrypted data to Base64 format for easy display
def encode_encrypted_data(encrypted_data):
    return base64.b64encode(encrypted_data).decode('utf-8')

def main():
    print("Encrypt a message")
    
    key = generate_key(16)  # Generate a random key

    plaintext = input("Enter the message to encrypt: ")
    encrypted = encrypt(plaintext, key)
    encrypted_base64 = encode_encrypted_data(encrypted)  # Convert the encrypted data to Base64
    print("Encrypted message (Base64 format):")
    print(encrypted_base64)  # Display the encrypted message

if __name__ == "__main__":
    main()

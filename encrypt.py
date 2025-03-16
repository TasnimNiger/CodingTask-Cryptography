from cryptography.fernet import Fernet

def encrypt_text(text, key):
    """
    Encrypts the given text using the provided key.
    
    :param text: The plaintext string to be encrypted
    :param key: The encryption key (must be a valid Fernet key)
    :return: The encrypted text (ciphertext)
    """
    cipher = Fernet(key)  # Initialize Fernet cipher with the given key
    encrypted_text = cipher.encrypt(text.encode())  # Encrypt the text
    return encrypted_text

def decrypt_text(encrypted_text, key):
    """
    Decrypts the given encrypted text using the provided key.
    
    :param encrypted_text: The encrypted string (ciphertext)
    :param key: The encryption key (must be the same key used for encryption)
    :return: The decrypted text (plaintext)
    """
    cipher = Fernet(key)  # Initialize Fernet cipher with the given key
    decrypted_text = cipher.decrypt(encrypted_text).decode()  # Decrypt the text
    return decrypted_text

# Generate a new encryption key (only once, store it safely!)
key = Fernet.generate_key()
print(f"Encryption Key: {key.decode()}")  # Save this key for later use

# Example usage
text_to_encrypt = "This is a secret message."
encrypted_message = encrypt_text(text_to_encrypt, key)
print(f"Encrypted: {encrypted_message}")

decrypted_message = decrypt_text(encrypted_message, key)
print(f"Decrypted: {decrypted_message}")

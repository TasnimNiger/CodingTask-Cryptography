import bcrypt

def bcrypt_hasher(password):
    """
    This function takes a password string, encodes it into a UTF-8 byte format, 
    and applies the bcrypt hashing algorithm with a randomly generated salt. 
    The resulting hashed password is returned as a string.
    """
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

# Call the function with a password string
hashed_password = bcrypt_hasher("_password-123_")

# Print the hashed password
print(f"Hashed Password: {hashed_password.decode()}")

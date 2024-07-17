from cryptography.fernet import Fernet, InvalidToken

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt a message
# secret_message = b'_247460_1'
# print(secret_message)
# encrypted_message = cipher_suite.encrypt(secret_message)
# print(encrypted_message)
# # Decrypt the message
# decrypted_message = cipher_suite.decrypt(encrypted_message)
# print(decrypted_message)

# unicode_str = "_247460_1"
# byte_str = unicode_str.encode('utf-8')
# encrypted_message = cipher_suite.encrypt(byte_str)
# decrypted_message = cipher_suite.decrypt(encrypted_message)
# original_message = decrypted_message.decode('utf-8')
# print(encrypted_message)
# print(decrypted_message)
# print(original_message)

from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Print the key to verify it remains consistent
print(f"Encryption Key: {key}")

# Original secret message
secret_message = b'_247460_1'
print(f"Original message: {secret_message}")

# Encrypt the message
encrypted_message = cipher_suite.encrypt(secret_message)
print(f"Encrypted message: {encrypted_message}")

# Decrypt the message
try:
    decrypted_message = cipher_suite.decrypt(encrypted_message)
    print(f"Decrypted message: {decrypted_message}")
except InvalidToken:
    print("Decryption failed: Invalid token")

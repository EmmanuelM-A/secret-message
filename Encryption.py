from Mappings import mapping_table
import random

def encrypt_message(message):
    key = []
    encrypted_message = []

    for _ in message:
        num = random.randint(0, len(mapping_table))

        encrypted_message.append(mapping_table[num])

        key.append(num)

    encrypted_message = str(encrypted_message)

    print(f"Encrypted message: {encrypted_message}")

    print(f"Key: {key}")

    
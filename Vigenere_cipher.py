
import string
import pandas as pd

# Define parameters
ciphertext = 'VVVRBACP'
key = 'COVER'

def Caesar_cipher(alphabet, key):
    """
    It creates a list containing the alphabet but in a new order, after moving it by KEY value like a Caesar cipher.
    :param alphabet: A string containing all letters of the English alphabet.
    :param key: The amount of spaces the alphabet will me moved.
    :return: A list containing all letters of the alphabet starting with a new letter (A if key = 0, B if key = 1, etc).
    """

    new_order_alphabet = []
    for idx in range(len(alphabet)):
        new_idx = idx + key
        if new_idx >= len(alphabet):
            new_idx -= len(alphabet)

        new_order_alphabet.append(alphabet[new_idx])

    return new_order_alphabet

def encrypt_text(plaintext, key, df_vigenere):
    ciphertext = ''
    for i, plaintext_letter in enumerate(plaintext):
        # Get the key letter we need to encrypt the code
        if i >= len(key):
            key_letter = key[i - len(key)]
        else:
            key_letter = key[i]

        # Get the position in the table
        encoded_letter = df_vigenere.loc[key_letter, plaintext_letter]

        # Append to the encoded text
        ciphertext += encoded_letter

    return ciphertext

def decrypt_text(ciphertext, key, df_vigenere):
    plaintext = ''
    for i, cipher_letter in enumerate(ciphertext):
        # Get the key letter we need to decrypt the code
        if i >= len(key):
            key_letter = key[i - len(key)]
        else:
            key_letter = key[i]

        # Get the position in the table
        decoded_letter = df_vigenere.index[df_vigenere[key_letter] == cipher_letter][0]

        # Append to the decoded text
        plaintext += decoded_letter

    return plaintext

alphabet = string.ascii_uppercase

# Create the Vigenere table using multiple Caesar ciphers
df_vigenere = pd.DataFrame()
for i, letter in enumerate(alphabet):
    df_vigenere[letter] = Caesar_cipher(alphabet, i)

# Set alphabet as index column
df_vigenere.index = [char for char in alphabet]

# Decipher the code
plaintext = decrypt_text(ciphertext, key, df_vigenere)
print(plaintext)
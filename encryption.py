def xor_cipher(binary_code, key):
    """
    This function takes in a binary Huffman code and a key, both as strings,
    and returns the result of applying the XOR operation on each corresponding
    bit of the two strings.

    Args:
    - binary_code: A binary string representing the Huffman code (e.g., '101', '110').
    - key: A binary string to XOR with the Huffman code (e.g., '1010').

    Returns:
    - The XOR result as a binary string.
    """
    # First, we ensure both binary_code and key are of the same length
    max_len = max(len(binary_code), len(key))
    
    # Padding the shorter string with leading zeros
    binary_code = binary_code.zfill(max_len)
    key = key.zfill(max_len)
    
    # Now perform the XOR operation bit by bit
    encrypted_code = ''
    for i in range(max_len):
        # XOR operation: '1' if the bits are different, '0' if they are the same
        if binary_code[i] == key[i]:
            encrypted_code += '0'
        else:
            encrypted_code += '1'
    
    return encrypted_code

def encrypt_decrypt_with_xor(huffman_codes, key):
    """
    This function takes a dictionary of Huffman codes and applies the XOR cipher
    to each Huffman code using the provided key. This function can be used both for
    encryption and decryption as XOR is a reversible operation.

    Args:
    - huffman_codes: A dictionary with characters as keys and their Huffman codes as values.
    - key: A binary string to XOR with each Huffman code.

    Returns:
    - A dictionary with characters as keys and their encrypted/decrypted Huffman codes as values.
    """
    encrypted_codes = {}
    
    # Loop through each character and its Huffman code
    for char, code in huffman_codes.items():
        # Apply the XOR cipher to each Huffman code and store the result
        encrypted_code = xor_cipher(code, key)
        encrypted_codes[char] = encrypted_code
    
    return encrypted_codes

# Testing the XOR encryption/decryption
# Example Huffman codes (these would come from the Huffman tree construction)
huffman_codes = {
    'a': '101',
    'b': '110',
    'c': '111',
    'd': '000',
    'e': '001',
}

# Example key (this key is used for both encryption and decryption)
key = '1010'

# Encrypt the Huffman codes
encrypted_codes = encrypt_decrypt_with_xor(huffman_codes, key)
print("Encrypted Huffman Codes: ", encrypted_codes)

# Decrypt the same Huffman codes (since XOR is reversible)
decrypted_codes = encrypt_decrypt_with_xor(encrypted_codes, key)
print("Decrypted Huffman Codes: ", decrypted_codes)

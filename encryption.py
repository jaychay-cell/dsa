def xor_cipher(binary_code, key):
    """
    Perform XOR encryption on a binary string using a key.
    This version is simplified and designed for beginners.

    Args:
    - binary_code (str): A binary string representing the Huffman code.
    - key (str): A binary string key used for the XOR operation.

    Returns:
    - str: The XOR result as a binary string.
    """
    # Step 1: Ensure both binary_code and key are of the same length
    max_length = max(len(binary_code), len(key))

    # Padding binary_code with leading zeros if necessary
    original_length = len(binary_code)  # Store the original length
    if len(binary_code) < max_length:
        padding_needed = max_length - len(binary_code)
        binary_code = "0" * padding_needed + binary_code

    # Padding key with leading zeros if necessary
    if len(key) < max_length:
        padding_needed = max_length - len(key)
        key = "0" * padding_needed + key

    # Step 2: Initialize an empty string to store the XOR result
    xor_result = ""

    # Step 3: Perform XOR operation bit by bit
    for i in range(max_length):
        if binary_code[i] == key[i]:
            xor_result += "0"  # Same bits result in '0'
        else:
            xor_result += "1"  # Different bits result in '1'

    # Step 4: Return the XOR result trimmed to match the original length
    return xor_result[-original_length:]


def encrypt_decrypt_with_xor(huffman_codes, key):
    """
    Apply XOR encryption or decryption on a dictionary of Huffman codes.

    Args:
    - huffman_codes (dict): A dictionary with characters as keys and binary strings as values.
    - key (str): A binary string key used for the XOR operation.

    Returns:
    - dict: A new dictionary with encrypted or decrypted Huffman codes.
    """
    # Step 1: Create an empty dictionary to store the updated codes
    updated_codes = {}

    # Step 2: Loop through every character and its Huffman code
    for char, code in huffman_codes.items():
        # Perform XOR operation on the Huffman code using the key
        encrypted_code = xor_cipher(code, key)

        # Store the result in the updated dictionary
        updated_codes[char] = encrypted_code

    # Step 3: Return the updated dictionary
    return updated_codes



#COMMENT OUT AFTER TESTING PURPOSES

def run_tests():
    """
    Run automated tests for the encryption/decryption logic using XOR.
    """
    # Define 20 test cases
    test_cases = [
        {"huffman_codes": {'a': '101', 'b': '110'}, "key": '1010'},  # Test case 1
        {"huffman_codes": {'x': '001', 'y': '111'}, "key": '1001'},  # Test case 2
        {"huffman_codes": {'m': '110110', 'n': '101'}, "key": '11'},
        {"huffman_codes": {'p': '0', 'q': '1'}, "key": '1'},
        {"huffman_codes": {'a': '101010'}, "key": '101'},
        {"huffman_codes": {'b': '111111'}, "key": '000000'},
        {"huffman_codes": {'z': '0000'}, "key": '1111'},
        {"huffman_codes": {'c': '010101'}, "key": '101010'},
        {"huffman_codes": {'d': '111000'}, "key": '000111'},
        {"huffman_codes": {'e': '10101'}, "key": '01010'},
        {"huffman_codes": {'f': '11001100'}, "key": '00110011'},
        {"huffman_codes": {'g': '00000000'}, "key": '11111111'},
        {"huffman_codes": {'h': '1111', 'i': '0000'}, "key": '1010'},
        {"huffman_codes": {'j': '1010', 'k': '0101'}, "key": '1111'},
        {"huffman_codes": {'l': '1001'}, "key": '1001'},
        {"huffman_codes": {'m': '111'}, "key": '010'},
        {"huffman_codes": {'n': '000'}, "key": '111'},
        {"huffman_codes": {'o': '101', 'p': '011'}, "key": '110'},
        {"huffman_codes": {'q': '111', 'r': '101'}, "key": '001'},
        {"huffman_codes": {'s': '11111111'}, "key": '00000000'},
    ]

    # Run each test case
    for idx, case in enumerate(test_cases):
        huffman_codes = case["huffman_codes"]
        key = case["key"]

        print("\nRunning Test Case", idx + 1)
        print("Huffman Codes:", huffman_codes)
        print("Key:", key)

        # Encrypt the Huffman codes
        encrypted_codes = encrypt_decrypt_with_xor(huffman_codes, key)
        print("Encrypted Codes:", encrypted_codes)

        # Decrypt the Huffman codes
        decrypted_codes = encrypt_decrypt_with_xor(encrypted_codes, key)
        print("Decrypted Codes:", decrypted_codes)

        # Check if the decryption matches the original Huffman codes
        if decrypted_codes == huffman_codes:
            print("Test case " + str(idx + 1) + ": PASSED")
        else:
            print("Test case " + str(idx + 1) + ": FAILED")
            print("Original:", huffman_codes)
            print("Encrypted:", encrypted_codes)
            print("Decrypted:", decrypted_codes)


# Main function to test the encryption and decryption
if __name__ == "__main__":
    # Step 1: Run the automated tests
    print("Running Automated Tests:")
    run_tests()
# Import required modules
from Priority_Queue import create_queue, enqueue_priority, dequeue_priority
from Trie import create_Trie, insert_trie, longest_match
from huffman_tree import extract, huffman_tree
from encryption import encrypt_decrypt_with_xor


# Function to process a file
def process_file(file_path, key):
    # Step 1: Read file content
    file = open(file_path, 'r')
    text = file.read()
    file.close()

    print(f"Processing file: {file_path} with key: {key}")
    print(f"File content (first 100 characters): {text[:100]}...")

    # Rest of the function


    # Step 2: Create Trie and insert substrings
    trie = create_Trie()
    for i in range(len(text)):
        insert_trie(trie, text[i:])

    # Step 3: Extract frequencies and build Huffman tree
    chunks = extract(trie)
    huffman_tree_structure = huffman_tree(chunks)

    # Step 4: Generate Huffman codes
    huffman_codebook = {}
    traverse_huffman_tree(huffman_tree_structure, '', huffman_codebook)

    # Step 5: Compress text
    compressed = encode_text(text, trie, huffman_codebook)

    # Step 6: Encrypt compressed data
    encrypted_codebook = encrypt_decrypt_with_xor(huffman_codebook, key)
    encrypted_text = encode_text(text, trie, encrypted_codebook)

    # Step 7: Decrypt and decompress
    decrypted_codebook = encrypt_decrypt_with_xor(encrypted_codebook, key)
    decompressed_text = decode_text(encrypted_text, huffman_tree_structure)

    # Step 8: Validate results
    if text == decompressed_text:
        print("Test PASSED for File: " + file_path)
        return True
    else:
        print("Test FAILED for File: " + file_path)
        return False

# Helper function to traverse Huffman tree and generate codes
def traverse_huffman_tree(node, current_code, codes):
    if node['type'] == 'leaf':  # When you reach a leaf node, add the code to the dictionary.
        codes[node['chunk']] = current_code
    else:
        if node.get('left') is not None:
            traverse_huffman_tree(node['left'], current_code + '0', codes)
        if node.get('right') is not None:
            traverse_huffman_tree(node['right'], current_code + '1', codes)

# Encode text using Huffman codes
def encode_text(text, trie, huffman_codes):
    encoded = ""
    i = 0
    while i < len(text):
        chunk, _ = longest_match(trie, text[i:])
        encoded += huffman_codes[chunk]
        i += len(chunk)
    return encoded

# Decode text using Huffman tree
def decode_text(encoded, huffman_tree):
    decoded = []
    current = huffman_tree
    for bit in encoded:
        if bit == '0':
            current = current['left']
        else:
            current = current['right']
        if current['type'] == 'leaf':
            decoded.append(current['chunk'])
            current = huffman_tree
    return ''.join(decoded)

# Main function
def main():
    # Test files with keys
    test_files = {
        'random_text1.txt': '1101',
        'random_text2.txt': '1010'
    }

    # Process each file
    for file_path in test_files:
        key = test_files[file_path]
        process_file(file_path, key)

if __name__ == "__main__":
    main()
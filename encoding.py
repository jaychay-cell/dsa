from Priority_Queue import *
from Trie import *
from huffman_tree import *

def traverse(node, current_code, codes): #recursive function to traverse the huffman tree
        if node['type'] == 'leaf':
            codes[node['chunk']] = current_code 
        else:
            traverse(node['left'], current_code + '0',codes) #updating code with left traversal as 0
            traverse(node['right'], current_code + '1',codes) #updating code with right traversal as 1

def huffman_codes(huffman_tree):
    codes = {} #building codebook
    traverse(huffman_tree, '',codes)
    return codes

def encode_text(lst,huffman_codes):

   encoded= []
   for chunk in lst:
        code = huffman_codes[chunk]
        encoded.append(code)
    
   return ''.join(encoded)

codebook = huffman_codes(huffman_tree)
print(codebook)
text = ["kwbkcbk","abcd","abaa"]
encoded = encode_text(text, tri, codebook)
print(encoded)

def decode_text(encoded, huffman_tree):
    
    decoded = []
    current = huffman_tree #traversing the huffman tree
    
    for bit in encoded:
        if bit == '0':
            current = current['left'] 
        else:  
            current = current['right']
        if current['type'] == 'leaf': #if leaf node is found, chunk is retrieved  
            decoded.append(current['chunk'])
            current = huffman_tree #resetting to original tree
    
    return ''.join(decoded)


decoded_text = decode_text(encoded, huffman_tree)
print(decoded_text)
    
    
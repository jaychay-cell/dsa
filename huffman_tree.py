from Priority_Queue import *
from Trie import *

def extract(trie): #extracting chunks from the trie
    chunks = {}
    traverse(trie,chunks, "")
    return chunks

def traverse(node, chunks, current): #traversing trie
        if '*' in node:
            chunks[current] = node['freq']
        for char, child in node.items():
            if char not in ['*', 'freq']:
                traverse(child, chunks, current + char)

def huffman_tree(chunks):
    pq = create_queue(len(chunks))
    for chunk, freq in sorted(chunks.items(), key=lambda x:x[1]):
        node = {
            'type': 'leaf',
            'chunk': chunk,
            'freq': freq
        }
        enqueue_priority(pq, node, freq) #enqueue chunk according to frequency

    while pq['n'] > 1:
        left = dequeue_priority(pq)[0] #lowest frequency
        right = dequeue_priority(pq)[0] 
        internal_node = {
            'type': 'internal',
            'left': left,
            'right': right,
            'freq': left['freq'] + right['freq']
        }
        enqueue_priority(pq, internal_node, internal_node['freq']) #parent node is the sum of two child nodes
    return dequeue_priority(pq)[0] 
chunks=extract(tri)
huffman_tree = huffman_tree(chunks)   
print(huffman_tree)  


    
    
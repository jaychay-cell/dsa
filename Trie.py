def create_Trie():
    return {}

def insert_trie(Trie,element):
    node = Trie
    for each in element: 
        if each not in node:
            node[each] = {}
        node = node[each]
    node['*'] = True
    if "freq" not in node:
        node["freq"] = 1
    else:
        node["freq"] += 1
    

def search_trie(Trie,element):
    node = Trie
    for each in element:
        if each in node:
            node = node[each]
    if "*" in node:
        return node['*']
    return None

def longest_match(trie, query):
    node = trie
    longest_match = ""
    longest_freq = 0
    current_match = ""
    for char in query:
        if char in node:
            node = node[char]
            current_match += char
            if '*' in node:
                if len(current_match) > len(longest_match):
                    longest_match = current_match
                    longest_freq = node.get("freq", 0)  
        else:
            break 
    
    return longest_match, longest_freq



#def delete_trie(Trie,element):
tri = create_Trie()
insert_trie(tri,"abaa")
insert_trie(tri,"abcd")
insert_trie(tri,"kwbkcbk")
insert_trie(tri,"abcd")
insert_trie(tri,"abaa")

print(tri)
print(longest_match(tri,"abcd"))

import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, frequency, symbol, left=None, right=None):
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    def __lt__(self, other):
        return self.frequency < other.frequency

def huffman_encoding(data):
    frequency = Counter(data)
    priority_queue = [Node(freq, symbol) for symbol, freq in frequency.items()]
    heapq.heapify(priority_queue)
    
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(left.frequency + right.frequency, left.symbol + right.symbol, left, right)
        heapq.heappush(priority_queue, merged)
        
    huffman_tree = priority_queue[0]
    huffman_codes = {}
    
    def generate_codes(node, code=""):
        if node:
            if not node.left and not node.right:
                huffman_codes[node.symbol] = code
            generate_codes(node.left, code + "0")
            generate_codes(node.right, code + "1")
    
    generate_codes(huffman_tree)
    encoded_data = ''.join(huffman_codes[symbol] for symbol in data)
    
    return encoded_data, huffman_tree

def huffman_decoding(encoded_data, huffman_tree):
    decoded_data = []
    node = huffman_tree
    
    for bit in encoded_data:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        
        if not node.left and not node.right:
            decoded_data.append(node.symbol)
            node = huffman_tree
    
    return ''.join(decoded_data)

# Example usage:
data = "ABCDE"
encoded_data, huffman_tree = huffman_encoding(data)
print("Encoded Data:", encoded_data)
decoded_data = huffman_decoding(encoded_data, huffman_tree)
print("Decoded Data:", decoded_data)

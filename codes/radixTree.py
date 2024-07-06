class RadixNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.value = None

class RadixTree:
    def __init__(self):
        self.root = RadixNode()

    def insert(self, key, value):
        current_node = self.root
        i = 0

        while i < len(key):
            for child_key in current_node.children.keys():
                if key[i:].startswith(child_key):
                    current_node = current_node.children[child_key]
                    i += len(child_key)
                    break
            else:
                break

        while i < len(key):
            new_node = RadixNode()
            current_node.children[key[i:]] = new_node
            current_node = new_node
            i = len(key)

        current_node.is_end_of_word = True
        current_node.value = value

    def search(self, key):
        current_node = self.root
        i = 0

        while i < len(key):
            for child_key in current_node.children.keys():
                if key[i:].startswith(child_key):
                    current_node = current_node.children[child_key]
                    i += len(child_key)
                    break
            else:
                return None

        if current_node.is_end_of_word:
            return current_node.value
        return None

    def delete(self, key):
        def _delete(node, key, depth):
            if depth == len(key):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0

            for child_key in node.children.keys():
                if key[depth:].startswith(child_key):
                    if _delete(node.children[child_key], key, depth + len(child_key)):
                        del node.children[child_key]
                        return not node.is_end_of_word and len(node.children) == 0
            return False

        _delete(self.root, key, 0)

# Example usage:
radix_tree = RadixTree()
radix_tree.insert("hello", "world")
radix_tree.insert("helium", "gas")

print(radix_tree.search("hello"))  # Output: world
print(radix_tree.search("helium"))  # Output: gas
print(radix_tree.search("helix"))   # Output: None

radix_tree.delete("hello")
print(radix_tree.search("hello"))  # Output: None
print(radix_tree.search("helium"))  # Output: gas
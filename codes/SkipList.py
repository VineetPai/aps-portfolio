import random

class Node:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level):
        self.max_level = max_level
        self.head = Node(None, self.max_level)
        self.level = 0

    def random_level(self):
        level = 0
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level

    def insert(self, value):
        update = [None] * (self.max_level + 1)
        current = self.head

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        level = self.random_level()

        if level > self.level:
            for i in range(self.level + 1, level + 1):
                update[i] = self.head
            self.level = level

        new_node = Node(value, level)

        for i in range(level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def search(self, value):
        current = self.head
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        current = current.forward[0]
        if current and current.value == value:
            return True
        return False

    def delete(self, value):
        update = [None] * (self.max_level + 1)
        current = self.head

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current and current.value == value:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            while self.level > 0 and self.head.forward[self.level] is None:
                self.level -= 1

# Example usage:
skiplist = SkipList(max_level=4)
skiplist.insert(3)
skiplist.insert(6)
skiplist.insert(7)
skiplist.insert(9)
skiplist.insert(12)
skiplist.insert(19)

print(skiplist.search(3))  # Output: True
print(skiplist.search(7))  # Output: True
print(skiplist.search(5))  # Output: False

skiplist.delete(3)
print(skiplist.search(3))  # Output: False
skiplist.delete(7)
print(skiplist.search(7))  # Output: False
skiplist.delete(19)
print(skiplist.search(19))  # Output: False
# The SkipList class has the following methods:
#
# random_level(): This method generates a random level for a new node. The level is generated based on the probability of 0.5. The higher the level, the lower the probability of generating it.
# insert(value): This method inserts a new node with the given value into the skip list.
# search(value): This method searches for a node with the given value in the skip list. It returns True if the node is found, otherwise False.
# delete(value): This method deletes a node with the given value from the skip list.
# The example usage demonstrates how to create a skip list, insert elements, search for elements, and delete elements from the skip list.


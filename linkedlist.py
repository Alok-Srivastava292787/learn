#linkedlist.py
#program to implement a linked list with insertion and deletion operations
class Node:
    """A class to represent a node in a linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """A class to represent a singly linked list."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node at the end of the linked list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        """Display the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self, key):
        """Delete the first occurrence of a node with the given key."""
        current = self.head

        # If the head node itself holds the key
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the key to be deleted
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not present in the linked list
        if not current:
            print(f"Key {key} not found in the list.")
            return

        # Unlink the node from the linked list
        prev.next = current.next
        current = None
# traverse method to find a node with a specific key
    def traverse(self, key):
        """Traverse to a specific node with the given key."""
        current = self.head
        position = 0  # To track the position of the node
        while current:
            if current.data == key:
                print(f"Node with key {key} found at position {position}.")
                return current
            current = current.next
            position += 1
        print(f"Node with key {key} not found in the list.")
        return None


# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(50)
    ll.append(60)
    print("Linked List after insertion:")
    ll.display()

    ll.delete(20)
    print("Linked List after deleting 20:")
    ll.display()

    print("\nTraverse to node with key 20:")
    ll.traverse(20)

    print("\nTraverse to node with key 40:")
    ll.traverse(40)
    
    ll.delete(40)
    print("Attempt to delete a non-existent key (40):")
    ll.display()

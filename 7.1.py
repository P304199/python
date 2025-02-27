class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  


class LinkedList:
    def __init__(self):
        self.head = None  

    def display(self):
        current = self.head
        if not current:
            print("The linked list is empty.")
            return
        print("Linked List: ", end="")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node  
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node  

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head  
        self.head = new_node  
    def insert_after_node(self, prev_data, data):
        current = self.head
        while current:
            if current.data == prev_data:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Node with data {prev_data} not found.")

    def delete_node(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next  
            current = None  
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            print(f"Node with data {key} not found.")
            return

        prev.next = current.next  
        current = None  
    def delete_at_end(self):
        if not self.head:
            print("The list is empty. Cannot delete.")
            return
        current = self.head
        if not current.next:
            self.head = None  
            return
        while current.next and current.next.next:
            current = current.next
        current.next = None  

    def delete_at_start(self):
        
        if not self.head:
            print("The list is empty. Cannot delete.")
            return
        self.head = self.head.next  


# Driver Code
if __name__ == "__main__":
    # Create a linked list
    linked_list = LinkedList()

    # Insert nodes
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_start(5)
    linked_list.insert_after_node(20, 25)

    # Display the list
    linked_list.display()

    # Delete a specific node
    linked_list.delete_node(20)
    print("\nAfter deleting node with data 20:")
    linked_list.display()

    # Delete the first node
    linked_list.delete_at_start()
    print("\nAfter deleting the first node:")
    linked_list.display()

    # Delete the last node
    linked_list.delete_at_end()
    print("\nAfter deleting the last node:")
    linked_list.display()

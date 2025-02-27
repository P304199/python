class Queue:
    def __init__(self):
        
        self.queue = []

    def enqueue(self, element):
       
        self.queue.append(element)
        print(f"Enqueued: {element}")

    def dequeue(self):
        
        if len(self.queue) == 0:
            print("Queue is empty. Cannot dequeue.")
        else:
            removed_element = self.queue.pop(0)
            print(f"Dequeued: {removed_element}")
            return removed_element

    def display(self):
        
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            print("Queue:", end=" ")
            for element in self.queue:
                print(element, end=" ")
            print()

    def is_empty(self):
        
        return len(self.queue) == 0

    def peek(self):
        
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            print(f"Front element: {self.queue[0]}")

# Driver Code
if __name__ == "__main__":
    q = Queue()

    # Display an empty queue
    q.display()

    # Enqueue some elements
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)

    # Display the queue
    q.display()

    # Peek the front element
    q.peek()

    # Dequeue some elements
    q.dequeue()
    q.dequeue()

    # Display the updated queue
    q.display()

    # Peek the front element after dequeue
    q.peek()

    # Dequeue all elements to test the empty queue condition
    q.dequeue()
    q.dequeue()

    # Try to dequeue from an empty queue
    q.dequeue()

    # Display the final state of the queue
    q.display()

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def size(self):
        return len(self.items)

def main():
    my_queue = Queue()

    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Front")
        print("4. Size")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            item = input("Enter the item to enqueue: ")
            my_queue.enqueue(item)
            print(f"{item} has been enqueued.")
        elif choice == '2':
            item = my_queue.dequeue()
            if item is not None:
                print(f"{item} has been dequeued.")
            else:
                print("Queue is empty.")
        elif choice == '3':
            if not my_queue.is_empty():
                print(f"Front of the queue: {my_queue.items[0]}")
            else:
                print("Queue is empty.")
        elif choice == '4':
            print(f"Queue size: {my_queue.size()}")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4/5).")

if __name__ == "__main__":
    main()

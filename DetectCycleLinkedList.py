class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create linked list: 1 -> 2 -> 3 -> 4
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

# Uncomment this line to create a cycle
# head.next.next.next.next = head.next

slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        print("Cycle Found")
        break
else:
    print("No Cycle")
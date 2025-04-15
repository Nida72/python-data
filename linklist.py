"""
class Node:
   def_init_(self,data) # type: ignore
   self.data= data # type: ignore
   self.next= None # type: ignore

   node1 = Node(10) # type: ignore
   node2 = Node(20) # type: ignore
   node3 = Node(30) # type: ignore
   node4 = Node(40) # type: ignore

   node1.next = node2
   node2.next = node3
   node3.next = node4

   current = node1
   while current is not None:
      print(current.data, end="->")
      current = current.next
      print("None")

"""
# Define a Node
class Node:
    def __init__(self, data):
        self.data = data  # value of the node
        self.next = None  # pointer to the next node

# Define a LinkedList
class LinkedList:
    def __init__(self):
        self.head = None  # initially empty list

    # Add a new node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head     
        self.head = new_node            

    # Display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Create LinkedList and insert some elements
ll = LinkedList()   
ll.insert_at_beginning(30)
ll.insert_at_beginning(20)
ll.insert_at_beginning(10)

ll.display()  # Output: 10 -> 20 -> 30 -> None

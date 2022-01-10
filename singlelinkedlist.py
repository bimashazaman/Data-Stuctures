
#linkedlist class
class Linkedlist:
    #initial linkedlist head is none
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    #append at the last
    def append(self , data):
        new_node = Node(data)

        #if the head is none
        if self.head is None :
            #new node will be the head
            self.head = new_node
            return

            #self head is the last node
        last_node = self.head
        #if last node has a next node
        while last_node.next :
            last_node = last_node.next
            #last node's next node will be the new node
            last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

llist = Linkedlist()
llist.append("A")
llist.append("B")
llist.prepend("C")
llist.print_list()

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_item(self,head, data):
        new_node = SinglyLinkedListNode(data)
        if self.head is None:
            self.head = new_node

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node



    def print_llist(self):
        last_node = self.head
        while last_node.next:
            print("-",last_node.data,"->")
            last_node = last_node.next



if __name__ == '__main__':
    llist_count = int(input())
    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = llist.add_item(llist.head, llist_item)

    llist.print_llist()

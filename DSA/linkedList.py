class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        itr = self.head

        while itr:
            print(itr.data)
            itr = itr.next

    def insertAtBeg(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def insertAtEnd(self,data):
        if self.head == None:
            self.head = Node(data)
            print(self.head.next)
        else:
            newnode = Node(data)
            ptr = self.head

            while(ptr.next != None):
                ptr = ptr.next
            ptr.next = newnode

    def insertAtAny(self,nodePos,data):
        if nodePos < 0:
            print("Not a valid position")
            return
        if nodePos == 0:
            self.insertAtBeg(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == nodePos -1:
                newnode = Node(data, itr.next)
                itr.next = newnode
                break
            itr = itr.next
            count +=1

    def deleteNode(self,nodePos):
        if nodePos < 0:
            print("This is not a valid Position")
            return

        if nodePos == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == nodePos -1:
                itr.next = (itr.next).next
                break
            itr = itr.next
        count +=1

if __name__ == '__main__':
    ll = LinkedList()
    ll.insertAtBeg(5)
    ll.insertAtBeg(20)

    ll.insertAtEnd(20)
    ll.insertAtEnd(30)
    ll.deleteNode(2)
    ll.insertAtAny(3, 55)
    ll.print()

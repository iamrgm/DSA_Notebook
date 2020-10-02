#Singly Linked List
#Insert Beginning
#Delete Beginning

class Node:
    def __init__(self, value=None):
        self.value = value
        self.nextnode = None
        
class LinkedList:
    def __init__(self):
        self.headnode = None
        
    def insert(self,new_data):
        new = Node(new_data)
        new.next = self.headnode
        self.headnode = new
        
    def delete(self):
        p = self.headnode
        self.headnode = p.next
    
    def printL(self):
        temp = self.headnode
        while(temp):
            print(temp.value)
            temp = temp.next
            
    
if __name__ == "__main__":
    llist = LinkedList()
    while(1):
        print("\nEnter the numbers: ")
        print("\n1.Insert\t2.Delete\t3.Print\t4.Exit\n")
        i = int(input())
        if i == 1:
            data = int(input())
            llist.insert(data)
        elif i == 2:
            llist.delete()
        elif i == 3:
            llist.printL()
        elif i == 4:
            break
        else:
            print("\nEnter proper choice!\n")

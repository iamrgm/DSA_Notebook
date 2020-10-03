class Node:
    def __init__(self, value=None):
        self.value = value
        self.nextnode = None
        
class LinkedList:
    def __init__(self):
        self.headnode = None
        
    def insert_beg(self,new_data):
        new = Node(new_data)
        if self.headnode == None:
            self.headnode = new
            new.nextnode = None
            return
        new.nextnode = self.headnode
        self.headnode = new
        
    def insert_end(self, new_data):
        new = Node(new_data)
        if self.headnode == None:
            self.headnode = new
            return
        temp = self.headnode
        while(temp.nextnode!=None):
            temp = temp.nextnode
        temp.nextnode = new
        new.nextnode = None
        
    def delete_beg(self):
        if self.headnode == None:
            print("\nNo Elements Present\n")
            return
        p = self.headnode
        self.headnode = p.nextnode
        
    def delete_end(self):
        if self.headnode == None:
            print("\nNo Elements Present\n")
            return
        p = self.headnode
        if p.nextnode == None:
            self.headnode == None
            return
        while(p.nextnode.nextnode!=None):
            p = p.nextnode
        p.nextnode = None
    
    def printL(self):
        if self.headnode == None:
            print("\nNo Elements Present\n")
        temp = self.headnode
        while(temp):
            print(temp.value)
            temp = temp.nextnode
            
    def printrev(self, temp):
        if self.headnode == None:
            print("\nNo Elements Present\n")
            return
        if temp: 
            self.printrev(temp.nextnode) 
            print(temp.value)
            return
        
            
    
if __name__ == "__main__":
    llist = LinkedList()
    while(1):
        print("\nEnter the numbers: ")
        print("\n1.Insert Beginning\n2.Insert End\n3.Delete Beginning\n4.Delete End\n5.Print\n6.Print Reverse\n7.Exit\n")
        i = int(input())
        if i == 1:
            data = int(input())
            llist.insert_beg(data)
        elif i== 2:
            data = int(input())
            llist.insert_end(data)
        elif i == 3:
            llist.delete_beg()
        elif i == 4:
            llist.delete_end()
        elif i == 5:
            llist.printL()
        elif i == 6:
            llist.printrev(llist.headnode)
        elif i == 7:
            break
        else:
            print("\nEnter proper choice!\n")

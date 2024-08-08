class Node:
    def __init__(self,value):
        self.Value=value
        self.Next=None

class Queue:
    def __init__(self,value):
        New_Node=Node(value)
        self.first=New_Node
        self.last=New_Node
        self.length=1
    def print_Queue(self):
        temp=self.first
        while temp is not None:
            print(temp.Value)
            temp=temp.Next

    def Enqueue(self,value):
        new_node = Node(value)
        if self.length==0:
            self.first=new_node
            self.last=new_node
        else:
            self.last.Next=new_node
            self.last=new_node
        self.length+=1
    
    def Dequeue(self):
        if self.length==0:
            return None
        temp=self.first
        if self.length==1:
            self.first=None
            self.last=None
        else:
            self.first=self.first.Next
            temp.Next=None
        self.length-=1
        return temp


my_queue= Queue(1)
my_queue.Enqueue(2)
my_queue.Dequeue()
my_queue.print_Queue()
class Node:
    def __init__(self,value):
        self.Value=value
        self.Next=None

class Stack:
    def __init__(self,value):
        new_Node = Node(value)
        self.Top=new_Node
        self.Height=1
    
    def Print_Stack(self):
        cureent= self.Top
        while cureent is not None:
            print(cureent.Value)
            cureent=cureent.Next
    
    def Push(self,value):
        new_node= Node(value)
        if self.Height==0:
            self.Top=new_node
        else:
            new_node.Next=self.Top
            self.Top=new_node
        self.Height+=1

    def Pop(self):
        if self.Height==0:
            return None
        else:
            temp =self.Top
            self.Top=self.Top.Next
            temp.Next=None
        self.Height-=1
            



myStack = Stack(4)
#myStack.Print_Stack()
myStack.Push(5)
myStack.Push(6)
myStack.Pop()
myStack.Print_Stack()
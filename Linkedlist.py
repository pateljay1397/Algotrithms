#Creating Node
class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    #    print('Where do you wish to insert node ?')
    #   print('Select any of this(Number) 1 At beginning, 2 In between two nodes, 3 At end')
    #    select = int(input())
    #    if(select == 1):

    def AtBegining (self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode
    #elif(select==2):

    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("Mention node is absent")
            return
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode
    #elif(select == 3):

    def AtEnd (self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode
    #else:
    #    print('Please select any option: ')


list = SLinkedList()  #Class Object
list.headval = Node("Monday")
e2 = Node("Tuesday")
e3 = Node("Wednesday")

list.headval.nextval = e2

e2.nextval = e3

list.AtBegining("Sun")
list.AtEnd("Thu")
list.Inbetween(list.headval.nextval,"Fri")
list.listprint()
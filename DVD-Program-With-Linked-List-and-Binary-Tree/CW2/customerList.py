#create and maintain a list of customers for the DVD store using linked list
from customer import customer

class node:
    def __init__(self,id):
        self.value = customer()
        self.value.id = id
        self.next = None
        self.previous = None

    def add_next(self):
        self.next = node()

    def print_data(self):
        self.value.print_data()

class customerList:
    def __init__(self):
        self.size = 0
        self.start = None

    def add_customer(self):
        if self.start == None:
            self.size += 1
            self.start = node(self.size)
            self.node = self.start
        else:
            self.size += 1
            self.node.next = node(self.size)
            self.node.next.previous = self.node
            self.node = self.node.next


    def return_to_the_beginning(self):
        self.node = self.start
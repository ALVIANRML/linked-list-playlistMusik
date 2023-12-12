from dvd import dvd

class node:
    def __init__(self,id):
        #create a new dvd object
        self.value = dvd()
        self.value.id = id
        self.next = None
        self.previous = None

    def print_data(self):
        self.value.print_data()


class dvdList:
    def __init__(self):
        self.size = 0
        # create a starting node
        self.start = None

    def add_dvd(self):
        if self.start == None:
            self.size += 1
            self.start = node(self.size)
            self.node = self.start
        else:
            self.size += 1
            self.node.next = node(self.size)
            self.node.next.previous = self.node
            self.node = self.node.next





    def return_to_the_beginning(self): # goes back to the beginning movie node
        self.node = self.start




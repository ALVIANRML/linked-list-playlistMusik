from customer import customer

class customerBTree:

    def __init__(self):
        # In a binary tree, there will be a starting node and the rest will be inserted into that starting node
        self.size = 0
        self.start_node = None

    def add_customer(self):
        if self.start_node == None:
            self.size += 1
            newcustomer = customer()
            self.start_node = node(self.size, newcustomer)
        else:
            self.size += 1
            newcustomer = customer()
            self.start_node.insert(self.size, newcustomer)


class node:
    def __init__(self,id,newcustomer):
        self.value = newcustomer
        self.value.id = id
        self.left = None
        self.right = None
        self.comparer = self.value.account_number
        self.previous = None


    def print_data(self):
        self.value.print_data()

    def insert(self, id,newcustomer):
        newcustomer.id = id

    #Note: Since the account number is unique, there won't be a situation where two customers have the same account number
        if newcustomer.account_number < self.comparer:
            #Goes to the left side if the account number value is less than that of the current node

            if self.left is None:
                self.left = node(id,newcustomer)
            else:
                self.left.insert(id,newcustomer)
        elif newcustomer.account_number > self.comparer:
            # Goes to the right side if the account number value is greater than that of the current node
            if self.right is None:
                self.right = node(id,newcustomer)
            else:
                self.right.insert(id,newcustomer)

    def exists(self, account_number):
        if account_number == self.value.account_number:
            return self

        if account_number < self.value.account_number:
            if self.left == None:
                return None
            return self.left.exists(account_number)

        if self.right == None:
            return None
        return self.right.exists(account_number)

    def delete(self, account_number):
        if self == None:
            return self
        if account_number < self.value.account_number:
            if self.left:
                self.left = self.left.delete(account_number)
            return self
        if account_number > self.value.account_number:
            if self.right:
                self.right = self.right.delete(account_number)
            return self

        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        temporary_node = self.right
        while temporary_node.left:
            temporary_node = temporary_node.left
        self.val = temporary_node.val
        self.right = self.right.delete(temporary_node.val)
        return self


    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        self.print_data()
        if self.right:
            self.right.PrintTree()



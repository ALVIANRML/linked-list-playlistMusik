# first name, last name, account number, list of DVDs rented

class customer:
    def __init__(self):
        self.id = 0
        self.first_name = input("Enter the first name of the customer: ")
        self.last_name = input("Enter the last name of the customer: ")
        self.account_number = input("Enter the account number: ")
        self.rented_dvds = list()

    def add_rented_dvd(self, dvd):
        self.rented_dvds.append(dvd)

    def remove_rented_dvd(self,dvd):
        self.rented_dvds.remove(dvd)

    def print_data(self):
        print("\n\n\nFirst Name: "+self.first_name)
        print("Last Name: "+self.last_name)
        print("Account Number: "+self.account_number)
        if len(self.rented_dvds)==0:
            print("Rented DVDs: None")
        else:
            print("Rented DVDs: ")
            for dvd in self.rented_dvds:
                print(dvd.movie_name)


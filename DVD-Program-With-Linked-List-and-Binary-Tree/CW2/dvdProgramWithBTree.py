# 1. Rent a DVD (check out)    ------- done  checked
# 2. Return a DVD (check in)   ------- done   checked
# 3. Create a list of DVS owned by the store ------- done    checked
# 4. Show the details of a particular DVD  ---------- done    checked
# 5. Print a list of all the DVDs in the store -------- done     checked
# 6. Check whether a particular DVD is in the store  -------- done    checked
# 7. Maintain a customer database  -------- done       checked
# 8. Print a list of all the DVDs rented by each customer ------------- done checked
import sys

from dvdList import dvdList
from dvd import dvd
from customer import customer
from customerBTree import customerBTree


def return_movie_index_to_beginning():
    try:
        dvd_list.return_to_the_beginning()
        #print("\n\nDVD index returned to the starting point\n\n")
    except:
        pass


def print_all_dvds(): # 5. Print a list of all the DVDs in the store
    return_movie_index_to_beginning()
    print("\n\n Printing out all the movies\n\n")
    while dvd_list.node is not None:
        dvd_list.node.print_data()
        dvd_list.node = dvd_list.node.next

def print_all_customers():   # 8. Print a list of all the DVDs rented by each customer
    customer_list.start_node.PrintTree()



def rent_dvd():   # 1. Rent a DVD (check out)
    account_number = input("Enter your account number: ")
    customer_acc = customer_list.start_node.exists(account_number)
    if customer_acc != None:
        while True:
            print_all_dvds()
            movie_name = input("Enter the name of the movie to rent: ")
            return_movie_index_to_beginning()
            while dvd_list.node != None:
                if dvd_list.node.value.movie_name == movie_name:
                    print("DVD found")
                    if dvd_list.node.value.copies>=1:
                        dvd_list.node.value.copies-=1
                        customer_acc.value.add_rented_dvd(dvd_list.node.value)
                        print(dvd_list.node.value.movie_name+" has been rented")
                    else:
                        print("\n\nThere isn't any dvds to rent")
                    break
                dvd_list.node = dvd_list.node.next


            stop = input("Enter stop to stop or enter anything else to rent another DVD: ")
            if stop == "stop":
                return
    print("Customer account not found")


def return_dvd(): # 2. Return a DVD (check in)
    account_number = input("Enter your account number: ")
    customer_acc = customer_list.start_node.exists(account_number)
    if customer_acc != None:
        while True:
            movie_name = input("Enter the name of the movie to return: ")
            return_movie_index_to_beginning()
            while dvd_list.node != None:
                if dvd_list.node.value.movie_name == movie_name:
                    print("DVD found")
                    if customer_acc.value.rented_dvds.__contains__(dvd_list.node.value):
                        dvd_list.node.value.copies += 1
                        customer_acc.value.remove_rented_dvd(dvd_list.node.value)
                        print(dvd_list.node.value.movie_name + " has been returned")
                    else:
                        print(
                            "The customer account " + customer_acc.value.account_number + " has not rented the movie " +
                            dvd_list.node.value.movie_name)
                    break
                dvd_list.node = dvd_list.node.next

            stop = input("Enter stop to stop or enter anything else to return another DVD: ")
            if stop == "stop":
                return
    print("Customer account not found")

def remove_dvd():
    movie_name = input("Enter the name of the movie to remove: ")
    return_movie_index_to_beginning()
    while dvd_list.node != None:
        if dvd_list.node.value.movie_name == movie_name:
            print("DVD found")
            if dvd_list.node.previous != None and dvd_list.node.next != None:
                dvd_list.node.previous.next = dvd_list.node.next
            elif dvd_list.node.previous == None:
                dvd_list.start = dvd_list.node.next
            elif dvd_list.node.next == None:
                dvd_list.node.previous.next = None
            print(movie_name+" has been removed")
            return
        else:
            dvd_list.node = dvd_list.node.next

def remove_customer():
    account_number = input("Enter the account number to remove: ")
    customer_list.start_node.delete(account_number)

def display_dvd_info(): # 4. Show the details of a particular DVD
    movie_name = input("Enter the name of the movie(DVD): ")
    return_movie_index_to_beginning()
    while dvd_list.node != None:
        if dvd_list.node.value.movie_name == movie_name:
            dvd_list.node.value.print_data()
            return
        dvd_list.node = dvd_list.node.next

def check_if_dvd_exists():    # 6. Check whether a particular DVD is in the store
    movie_name = input("Enter the name of the DVD: ")
    return_movie_index_to_beginning()
    while dvd_list.node != None:
        if dvd_list.node.value.movie_name == movie_name:
            if dvd_list.node.value.copies>0:
                print(dvd_list.node.value.movie_name+" is available")
            else:
                print("DVD is in the list but there is no more copies to rent")
            display = input("Display info (y/n): ")
            if display == "y":
                dvd_list.node.value.print_data()
            return
        dvd_list.node = dvd_list.node.next
    print("DVD does not exist")


print("\n\nRegistering all DVDs\n\n")
dvd_list = dvdList()     # 3. Create a list of DVS owned by the store
print("\n\nRegistering all customers\n\n")
customer_list = customerBTree() # 7. Maintain a customer database

while True:
    main_menu = "1. Rent a DVD\n2. Return a DVD\n3.Display details on a DVD\n4.Display all DVDs\n5.Check if a DVD is available" \
                "\n6. Display the rented DVDs\n From point 7 onwards is what an admin will do \n7. Remove a dvd\n8. Remove a customer\n9. Add a dvd\n10. Add a customer"
    print(main_menu)
    temp_boolean = True
    while temp_boolean:
        try:
            main_menu_option = int(input("Enter a number: "))
            temp_boolean = False
        except:
            print("Pls enter numbers only!")
    temp_boolean = True
    while temp_boolean:
        if main_menu_option==1:
            if customer_list.size>0 and dvd_list.size>0:
                rent_dvd()
            else:
                if customer_list.size==0:
                    print("The customer account list is empty")
                elif dvd_list.size==0:
                    print("The dvd list is empty")
        elif main_menu_option==2:
            if customer_list.size>0 and dvd_list.size>0:
                return_dvd()
            else:
                if customer_list.size==0:
                    print("The customer account list is empty")
                elif dvd_list.size==0:
                    print("The dvd list is empty")
        elif main_menu_option==3:
            if dvd_list.size>0:
                display_dvd_info()
            else:
                print("The dvd list is empty")
        elif main_menu_option==4:
            if dvd_list.size>0:
                print_all_dvds()
            else:
                print("The dvd list is empty")
        elif main_menu_option==5:
            if dvd_list.size>0:
                check_if_dvd_exists()
            else:
                print("The dvd list is empty")
        elif main_menu_option==6:
            if customer_list.size>0:
                print_all_customers()
            else:
                print("The customer list is empty")
        elif main_menu_option==7:
            if dvd_list.size>0:
                remove_dvd()
            else:
                print("The dvd list is empty")
        elif main_menu_option==8:
            if customer_list.size>0:
                remove_customer()
            else:
                print("The customer list is empty")
        elif main_menu_option==9:
            dvd_list.add_dvd()
        elif main_menu_option==10:
            customer_list.add_customer()
        else:
            print("Invalid option number")
        temp_boolean = False
        finished = input("Stop the program? (y/n): ")
        if finished == "y":
            sys.exit()

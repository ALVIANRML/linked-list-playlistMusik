#movie name, names of the stars, name of the producer, name of the director, name of the production company,
# number of copies in the store

class dvd:
    def __init__(self):
        self.movie_name = input("Enter the name of the movie: ")
        self.stars_names = list()
        self.id = 0
        temp = input("Enter the name(s) of the star(s) (For multiple stars, seperate them with a comma) :")
        names = temp.split(",")
        for name in names:
            self.stars_names.append(name)
        self.producer_name = input("Enter the name of the producer: ")
        self.director_name = input("Enter the name of the director: ")
        self.company_name = input("Enter the name of the production company: ")
        while True:
            try:
                self.copies = int(input("Enter the number of copies: "))
                break
            except:
                print("Pls enter numbers only")

    def print_data(self):
        print("\n\n\nID: "+ str(self.id))
        print("Movie Name: "+self.movie_name)
        print("Stars: ")
        for star in self.stars_names:
            print(star)
        print("Producer: "+self.producer_name)
        print("Director: "+self.director_name)
        print("Production Company: "+self.company_name)
        print("Number of copies: "+str(self.copies))

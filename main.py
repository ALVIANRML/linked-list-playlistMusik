import matplotlib.pyplot as plt
import networkx as nx

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None
        self.current_song = None  # Added to keep track of the current song

    def add_song(self, title, artist):
        new_song = Song(title, artist)
        if self.head is None:
            self.head = new_song
            self.current_song = self.head  # Set the current song when adding the first song
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_song

    def display_playlist(self):
        current = self.head
        while current is not None:
            print("Title:", current.title, ", Artist:", current.artist, end="")
            if current.next is not None:
                print(" --> ", end="")
            current = current.next
        print()  # Add a new line after displaying the playlist

    def visualize_playlist(self):
        G = nx.DiGraph()
        current = self.head
        while current is not None:
            G.add_node(current.title, label=f'{current.title}\n{current.artist}')
            if current.next is not None:
                G.add_edge(current.title, current.next.title)
            current = current.next

        pos = nx.spring_layout(G)
        labels = nx.get_node_attributes(G, 'label')
        nx.draw(G, pos, with_labels=True, labels=labels, node_size=1000, node_color='skyblue', font_size=8, font_color='black', font_weight='bold', arrowsize=15)
        plt.show()

def main():
    playlist = Playlist()

    while True:
        choose = int(input("SPOTIFY:\n MENU:\n1. Make Playlist\n2. My playlist\n3. Visualize Playlist\n0. Exit\nChoose: "))

        if choose == 1:
            print("Add your song")
            while True:
                song = input("Song: ")
                artist = input("Artist:")
                choose = input("1. Stay add your playlist\n"
                               "2. See your playlist\n"
                               "3. Visualize Playlist\n"
                               "0. Back to menu \n"
                               "Choose: ")

                if choose == "0":
                    break
                playlist.add_song(song, artist)
                if choose == "2":
                    print("\nMY PLAYLIST:")
                    playlist.display_playlist()
                if choose == "3":
                    print("\nVisualizing Playlist...")
                    playlist.visualize_playlist()

        elif choose == 2:
            print("\nMY PLAYLIST:")
            playlist.display_playlist()

        elif choose == 3:
            print("\nVisualizing Playlist...")
            playlist.visualize_playlist()

        elif choose == 0:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()

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

    def add_song(self, title, artist):
        new_song = Song(title, artist)
        if self.head is None:
            self.head = new_song
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_song

    def display_playlist(self):
        current = self.head
        while current is not None:
            print(f"Title: {current.title}, Artist: {current.artist}")
            current = current.next

    def visualize_playlist(self, graph, playlist_name):
        current = self.head
        while current is not None:
            graph.add_node(current.title, label=f'{current.title}\n{current.artist}')
            if current.next is not None:
                graph.add_edge(current.title, current.next.title)
            current = current.next

        return graph


class PlaylistManager:
    def __init__(self):
        self.playlists = {}

    def create_new_playlist(self, name):
        new_playlist = Playlist()
        print(f"Add songs for {name}")
        while True:
            song = input("Song: ")
            artist = input("Artist: ")
            new_playlist.add_song(song, artist)
            add_more = input("Add another song? (y/n): ")
            if add_more.lower() != 'y':
                break

        self.playlists[name] = new_playlist
        print(f"Created new playlist: {name}")

    def display_all_playlists(self):
        for name, playlist in self.playlists.items():
            print(f"\n{name} PLAYLIST:")
            playlist.display_playlist()

    def visualize_all_playlists(self):
        g = nx.DiGraph()
        for name, playlist in self.playlists.items():
            g = playlist.visualize_playlist(g, name)

        pos = nx.spring_layout(g)
        labels = nx.get_node_attributes(g, 'label')
        nx.draw(g, pos,
                with_labels=True,
                labels=labels,
                node_size=1000,
                node_color='blue',
                font_size=8,
                font_color='black',
                font_weight='bold',
                arrowsize=15)
        plt.show()

    def visualize_conjugate(self, playlist1_name, playlist2_name):
        if playlist1_name not in self.playlists or playlist2_name not in self.playlists:
            print("Error: One or more playlist names are invalid.")
            return

        g1 = self.playlists[playlist1_name].visualize_playlist(nx.DiGraph(), playlist1_name)
        g2 = self.playlists[playlist2_name].visualize_playlist(nx.DiGraph(), playlist2_name)

        # Connect the last song of the first playlist to the first song of the second playlist
        last_song_g1 = list(g1.nodes())[-1]
        first_song_g2 = list(g2.nodes())[0]
        g1.add_edge(last_song_g1, first_song_g2)

        # Create the conjugate graph
        conjugate_graph = nx.compose(g1, g2)

        # Draw the conjugate graph
        pos = nx.spring_layout(conjugate_graph)
        labels = nx.get_node_attributes(conjugate_graph, 'label')
        nx.draw(conjugate_graph, pos,
                with_labels=True,
                labels=labels,
                node_size=1000,
                node_color='orange',  # You can choose another color for the conjugate graph
                font_size=8,
                font_color='black',
                font_weight='bold',
                arrowsize=15)
        plt.show()

def main():
    playlist_manager = PlaylistManager()

    while True:
        choose = int(input("SPOTIFY:\n "
                           "MENU:\n"
                           "1. Make Playlist\n"
                           "2. My playlists\n"
                           "3. Visualize Playlist\n"
                           "4. Visualize Conjugate Playlist\n"
                           "0. Exit\n"
                           "Choose: "))

        if choose == 1:
            playlist_name = input("Enter playlist name: ")
            playlist_manager.create_new_playlist(playlist_name)

        elif choose == 2:
            print("\nMY PLAYLISTS:")
            playlist_manager.display_all_playlists()

        elif choose == 3:
            print("\nVisualizing Playlist...")
            playlist_manager.visualize_all_playlists()

        elif choose == 4:
            print("\nVisualizing Conjugate Playlist...")
            playlist1_name = input("Enter the first playlist name: ")
            playlist2_name = input("Enter the second playlist name: ")
            playlist_manager.visualize_conjugate(playlist1_name, playlist2_name)

        elif choose == 0:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()

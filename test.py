
count = 1

class iter_song:

    def __init__(self, song_list, count):
        self.song = song_list
        self.count = count

    @staticmethod
    def return_song(song_list, count):
        return song_list[count]

    def count_add(self, count):
        count += 1
        return count

   
songs = iter_song(['a','b','c','d'], 0)

print(songs.return_song)


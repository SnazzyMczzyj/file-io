import csv

file_name = input("Enter file name: ")
if len(file_name) == 0:
    file_name = "spotify-2023.csv"


def song_count(file_name):
    song_num = -1

    with open (file_name, 'r') as file:
        content = csv.reader(file)

        for i in content:
            song_num += 1

        print("Number of songs in the file:", song_num)
    

def songs_in_E(file_name):
    key_num = 0

    with open (file_name, 'r') as file:
        content = csv.reader(file)

        for i in content:
            if i[15] == 'E':
                key_num += 1

        print("Number of songs in the key of E:", key_num)


def most_common_artist(file_name):
    artists = []
    artists_sublists = []
    current_track = None
    track_count = 0
    artist_name = ''

    with open (file_name, 'r') as file:
        content = csv.reader(file)

        for i in content:
            artists.append(i[1])

        artists.sort()

        for artist_name in artists:
            if artist_name != current_track:
                current_track = artist_name
                artists_sublists.append([artist_name])
            else:
                artists_sublists[-1].append(artist_name)

        for i in artists_sublists:
            if track_count <= len(i):
                track_count = len(i)
                artist_name = i[0]

        print("The most common artist:", artist_name + ",", track_count, "tracks")
    

song_count(file_name)
songs_in_E(file_name)
most_common_artist(file_name)
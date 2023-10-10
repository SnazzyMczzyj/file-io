import csv
with open ("spotify-2023.csv", 'r') as file:
    content = csv.reader(file)

# Initialize variables
    song_num = -1
    key_num = 0
    artists = []

    # Count the number of songs
    for i in content:
        song_num += 1
        
        # Count the number of songs in the key of E
        if i[15] == 'E':
            key_num += 1

        # Put all artists in list
        artists.append(i[1])
    artists.sort()

    # Arrange artists in sublists
    artists_sublists = []
    current_track = None

    for artist_name in artists:
        if artist_name != current_track:
            current_track = artist_name
            artists_sublists.append([artist_name])
        else:
            artists_sublists[-1].append(artist_name)

    # Count largest sublist
    sub = 0
    artist_name = ''

    for i in artists_sublists:
        if sub <= len(i):
            sub = len(i)
            artist_name = i[0]
    

    print("Number of songs in the file:", song_num)
    print("Number of songs in the key of E:", key_num)
    print("The most common artist:", artist_name + ",", sub)
liked_songs = {
    "Bad Habits": "Ed Sheeran",
    "I'm Just Ken": "Ryan Gosling",
    "Mastermind": "Taylor Swift",
    "Uptown Funk": "Mark Ronson ft. Bruno Mars",
    "Ghost": "Justin Bieber"
}
def write_liked_songs_to_file(liked_songs, file_name):
    file = open(file_name, "w")
    file.write("Liked Songs:\n")
    for song, artist in liked_songs.items():
        file.write(f"{song} by {artist}\n")
    file.close()
    print(f"Successfully added Liked songs to {file_name} ❤️")
write_liked_songs_to_file(liked_songs, "liked_songs.txt")



# Tuples Challenge

# Given the tuple below that represents the Imelda May album
# "More Mayhem", write code to print the album details, followed by
# a listing of all the track in the album.

#
# Indent the tracks by a single tab when printing them (remember
# that you can pass more than one item to print the function,
# separating them with a comma).

imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
)

name, artist, year, tracks = imelda
print(f"Album details:\n"
      f"Title: {name},\n"
      f"Artist: {artist},\n"
      f"Year: {year},\n"
      f"Tracks: \n\t{tracks[0][1]},\n\t{tracks[1][1]},\n\t{tracks[2][1]},\n\t{tracks[3][1]}.")

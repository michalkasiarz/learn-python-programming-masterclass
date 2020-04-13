import pickle

# Reading pickle

with open("imelda.pickle", "rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)

print(imelda2)

album, artist, year, track_list = imelda2
print(album)
print(artist)
print(year)

for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)

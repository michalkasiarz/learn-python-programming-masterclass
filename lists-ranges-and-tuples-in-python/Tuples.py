# Introduction to tuples
# Tuples are immutable!

t = "a", "b", "c"
print(t)

print("a", "b", "c")
print(("a", "b", "c"))

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

# sneaky way to "edit" a tuple
imelda = imelda[0], "Imelda May", imelda[2]     # assigned to new object
print(imelda)

metallica2 = ["Ride the Lightning", "Metallica", 1984]
print(metallica2)
# lists are directly editable
metallica2[0] = "Master of Puppets"
print(metallica2)

# unpacking a tuple
title, artist, year = imelda
print(title)
print(artist)
print(year)

import shelve

# printing built-in functions

for f in dir(__builtins__):
    print(f)

print("=" * 40)

print("SHELVE FUNCTIONS:")
for obj in dir(shelve.Shelf):
    if obj[0] != "_":
        print(obj)

print("=" * 40)

# Help shelve
help(shelve)

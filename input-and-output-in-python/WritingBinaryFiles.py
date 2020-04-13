# Writing binary files

with open("binary", "bw") as bin_file:
    for i in range(17):
        bin_file.write(bytes([i]))  # [] - list is a bytes-like object


# Reading binary file
with open("binary", "br") as binFile:
    for b in binFile:
        print(b)

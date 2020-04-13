# Writing binary files

with open("binary", "bw") as bin_file:
    for i in range(17):
        bin_file.write(bytes([i]))


# Reading binary file
with open("binary", "br") as binFile:
    for b in binFile:
        print(b)

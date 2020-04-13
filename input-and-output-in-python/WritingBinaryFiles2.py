# Writing binary files 2

a = 65534  # FF FE
b = 65535  # FF FF
c = 65535  # 00 01 00 00
d = 2998302  # 00 2D C0 1E

with open("binary2", "bw") as bin_file:
    bin_file.write(a.to_bytes(2, "big"))
    bin_file.write(b.to_bytes(2, "big"))
    bin_file.write(c.to_bytes(4, "big"))
    bin_file.write(d.to_bytes(4, "big"))
    bin_file.write(d.to_bytes(4, "little"))

with open("binary2", "br") as bin_file:
    e = int.from_bytes(bin_file.read(2), "big")
    print(e)    # 65534
    f = int.from_bytes(bin_file.read(2), "big")
    print(f)    # 65535
    g = int.from_bytes(bin_file.read(4), "big")
    print(g)    # 65535
    h = int.from_bytes(bin_file.read(4), "big")
    print(h)    # 2998302
    i = int.from_bytes(bin_file.read(4), "big")  # big int format
    print(i)    # 515910912

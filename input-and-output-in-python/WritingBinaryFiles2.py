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



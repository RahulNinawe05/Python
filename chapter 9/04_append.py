# t = "00011001001110"

# f = open ("myfile", "a+")

# f.write(t)
# f.close()

t = b"00011001001110"  # Binary string
with open("myfile", "ab") as f:  # 'ab' for appending in binary mode
    f.write(t)  # Write binary data

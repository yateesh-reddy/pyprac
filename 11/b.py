with open("file1.txt") as f1, open("file2.txt") as f2:
    data = f1.read() + f2.read()

with open("file3.txt", "w") as f3:
    f3.write(data)
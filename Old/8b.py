with open("file1.txt", "r") as f1, \
     open("file2.txt", "r") as f2, \
     open("file3.txt", "w") as f3:

    f3.write(f1.read())
    f3.write("\n")
    f3.write(f2.read())

print("Files merged successfully")
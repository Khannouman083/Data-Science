# f=open(r"sample.txt", "at")
# f.write("\nAppending new data to my file")
# f.close()

# f=open(r"newFile.txt", "x")
# f.write("Creating new file and wrtiting to it")
# f.close()

# f=open(r"newFile.txt", "r+")
# f.write("Developing")
# print(f.read())

# f=open(r"newFile.txt", "w+")
# f.write("Developing new file")
# print(f.read())

f=open(r"newFile.txt", "a+")
f.write("\nAppending new data to a file")
print(f.read())

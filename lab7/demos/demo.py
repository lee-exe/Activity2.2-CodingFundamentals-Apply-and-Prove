colours_file = open("colour.txt")
print(colours_file)

data = colours_file.readline()
print(data)

colours_list = data.split(", ")
print(colours_list)

for line in colours_list:
    print(line)

colours_file.close()


# With command: opens and closes file automatically
# r - read
# w - write (clear file and add new test)
# a - append (adds new text to end of file)

with open("colour.txt", "r") as file:
    for line in file:
        print(line)


# TASK: Download the file ”artists.txt”
# read the content of the file into a variable,
# and print the content in a loop, one line at a time

# open the file
file_handle = open("artists.txt", "r")

print("Some of the best-selling music albums in history:\n")

# read all contents to a variable
content = file_handle.read()
lines = content.split("\n")

# because lines is just a Python list, we can use loops
for line in lines:
    print(f"-> {line}")

# close the connection in the end
# to avoid strange file locking bugs
file_handle.close()
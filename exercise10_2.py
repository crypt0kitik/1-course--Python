# TASK: create a guestbook application
# ask the user whether they want to read
# or write into the guestbook

# ask a user about choice
user_choice = input("Would you like to read or write into the guestbook? (r/w)\n")

# if a user wants to read the file
if user_choice == "r":
    # open file for reading
    file_handle = open("guestbook.txt", "r")
    content = file_handle.read()
    lines = content.split("\n")
    # print content of the file into separate lines
    for line in lines:
        print(line)
    # close file
    file_handle.close()

# if a user wants to write to the file
elif user_choice == "w":
    message = input("Write a new message:\n")
    # open file for writing
    file_handle = open("guestbook.txt", "a", encoding="utf-8")
    # write to the file
    file_handle.write(message + "\n")
    # close file
    file_handle.close()
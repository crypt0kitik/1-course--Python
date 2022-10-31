# ask text from user
text = input("Give some text: \n")

# reverse text
reversed_text = text[::-1]
print(reversed_text)

# check for Palindrome
if text == "":
    print("Your text is empty.")
elif text == reversed_text:
    print("Palindrome: YES")
else:
    print("Palindrome: NO")

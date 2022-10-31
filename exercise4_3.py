# save text and print
text = "The quick brown fox jumps over the lazy dog. That \
sentence contains every letter in the English alphabet. Neat!"
print(text)

# "fox" replace by "duck"
text = text.replace("fox", "duck")
print(text)

# ask for a word to remove from text
word = input("Which word should be removed? \n")
if word in text:
    text = text.replace(word, '')
    print(text)
else:
    print("Word not found.")

# count and print number of characters and words
text_length = len(text)
print(f"In the text there are {text_length} characters.")

word_list = text.split()
word_number = len(word_list)
print(f"In the text there are {word_number} words.")

# replace the dots/periods into newlines
text = text.replace(".", "\n")
print(text)

# ask for a new text
usertext = input("Write a new sentence: ")

# check 20 characters and short it or print original
usertext_lenght = len(usertext)

if usertext_lenght <= 20:
    print(usertext)
else:
    subtext = usertext[0:20]
    print(f"{subtext} ...")

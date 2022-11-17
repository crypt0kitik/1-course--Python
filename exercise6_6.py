# task: ask the user for a word
# after this, print content
# but do not print the word the user gave as input

# list called "basket"
basket = ["apple", "banana", "cherry", "carrot",
          "potato", "tomato", "cabbage"]

new_list = []

# create a loop for word in basket
for product in basket:
    word = input("Which word to ignore?\n")

    # if a user inputs number
    if word.isnumeric():
        word = int(word)
        # minus 1 because of index
        word = word - 1
        # remove this word and create a new basket
        basket.remove(basket[word])
        new_list.append(basket)
        # print the result
        print(*basket, sep='\n')

    # if a user inputs text
    elif word.isalpha():
        if word in basket:
            # remove this word and create a new basket
            basket.remove(word)
            new_list.append(basket)
            # print the result
            print(*basket, sep='\n')
        elif word not in basket:
            print("Word not found.")

    # if user inputs incorrect value
    else:
        print("incorrect value")
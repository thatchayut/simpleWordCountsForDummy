# get input
favorite_word = input( " I want to find this word: ")
sentence = input(" From this sentence => ")

# split sentence into words
splitted_sentence = sentence.split(" ")

# This process in to delete special charaters
# iterate through words in splitted sentence
print()
print(" # PROCESS : Eliminating special characters")

# define special characters
special_characters = ['"', "."]

# create array for words after trimming special charaters
new_sentence = []

for word in splitted_sentence:
    print(" This word is " + str(word))

    # split word to see its characters using the property of "list"
    characters = list(word)
    print(" This word contains : " + str(characters))
    
    # find and eliminate special charaters
    valid_character = []
    for character in word:
        # if this charater is not special character, keep it as a valid character
        if character not in special_characters:

            # use "append" instead of "push" because "character" variable is "list"
            valid_character.append(character)
    
    # convert array to string using "join"
    valid_word = ''.join(valid_character)

    print(" Valid word for this word => " + str(valid_word))
    print()
            
    # add word to new sentence
    new_sentence.append(valid_word)

print(" Sentence after trimming special characters => " + str(new_sentence))
print()

print(" # PROCESS : Counting words")

counter = 0

for word in new_sentence:
    if word == favorite_word:
        counter += 1

print(" # RESULT : ")
print("The word '" + str(favorite_word) +"' appears " + (str(counter)) + " times in this sentence.")

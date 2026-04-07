text = input("Enter a string: ")
#split the sentence into a list of words and print the list
words = text.split()
print(type(words))
print("The list of words is: " + str(words))
#then join the list of words back into a sentence and print the sentence with each word separated by a hyphen
sentence = "-".join(words)
print("The sentence with hyphens is: " + sentence)
TEXT_NAMES = {"a": "2", "collection": "1", "fun": "1", "is": "3",
               "it": "1", "nice": "1", "of": "2","thing":"1","this":"2","words":"2"}
text=str(input("Enter the text"))
word = input("Enter the word: ")
while word != "":

    if word in TEXT_NAMES:

        print(word, ":", TEXT_NAMES[word])

    else:

        print("Invalid word")

    word = input("Enter the word: ")

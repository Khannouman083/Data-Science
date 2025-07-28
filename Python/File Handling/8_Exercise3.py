def word_find(word):
    with open(r"Exercise.txt", "r") as f:
        data=f.read()
        if(word in data):
            print("Word Found")
        else:
            print("Word not found")


word_find("Python")

def word_find_line(word):
    line_no=1
    data=True
    with open(r"Exercise.txt", "r") as f:
        while data:
         data=f.readline()
         if(word in data):
            print(line_no)
            return
         line_no+=1

word_find_line("programming")



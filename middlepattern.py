def middle_pattern(word):
    if len(word)% 2 == 0:
        print("This is not a odd length word")
        return
    middle_index = len(word)// 2

    for i in range(len(word)):
        end_index=middle_index + i + 1
        if end_index > len(word):
            print(word[middle_index:] + word[:end_index - len(word)])
        else:
            print(word[middle_index:end_index])


word= input("Enter the word:")
middle_pattern(word)
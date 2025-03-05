def count_unique_words():

    words = []
    while True:
        word = input("Word: ")
        if word in words:
            print(f"You typed in {len(words)} different words")
            break
        else:
            words.append(word)

if __name__ == "__main__":
    count_unique_words()
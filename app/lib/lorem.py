from random import choice, randint

class Lorem():
    def __init__(self, words_file):
        with open(words_file, 'r') as lorem_file:
            all_lorem_text = lorem_file.read()

        self.words = all_lorem_text.split(" ")

    def get_lorem_text(self, min_words=50, max_words=200):
        num_words = randint(min_words, max_words)
        selected_words = [
            choice(self.words)
            for x in range(num_words)
        ]



        return cap_start_of_sentence(selected_words)

def cap_start_of_sentence(words):
    end_marks = ["!", ".", "?"]
    new_words = []

    previous_word = ""
    for word in words:
        # Above is same as
        # if previous_word[-1:] in end_marks:
        #     new_word = word.title()
        # else:
        #     new_word = word

        new_word = (word.title() 
            if previous_word[-1:] in end_marks
            else word)

        previous_word = word
        new_words.append(new_word)

    return " ".join(new_words)


#! /usr/bin/python3
# original author: Emil Khaibrakhmanov
# I the author grant the use of this code for teaching: yes

# Find all words in sentence that end in "a" and print them together separated by an hyphen -.
#
# sample input / output
# >>> cyberpunk replica doom dota supermarket formula good bad banana
#     replica-dota-formula-banana

def a_letter_finder(sentence):
    sent = sentence.split()
    words = []
    for word in sent:
        if word[-1] == "a":
            words.append(word)
    return "-".join(words)


if __name__ == '__main__':
    user_input = input("Please write a sentence and I will find all words that ending on 'a' and split them with -\n")
    print(a_letter_finder(user_input))

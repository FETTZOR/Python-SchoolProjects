input("Press Enter to start chat...")

answer = input("Hello, how are you? 'fine' 'good' 'nothing much' 'bad': ").lower()  # Fine, Good, Perfect. Bad

if answer == 'fine' or answer == 'good' or answer == 'perfect':
    age = int(input("Lovely to hear! How old are you by the way? 'in integers please': "))
    if 18 <= age < 65:
        answer = input("Ok, then you are welcome. Where are you now? 'in school''at the university''on work' ").lower()
        if answer == 'in school' or answer == 'at the university' or answer == 'on work':
            answer = input("I wish you luck. Do you like listening to music? 'Yes' 'Sure''no': ").lower()
            if answer == 'yes' or answer == 'sure':
                answer = input("Me too! which genre of music is your favorite? 'Rock' 'rock' 'Hip-hop' 'Rap': ").lower()
                if answer == 'hardrock' or answer == 'rock':
                    answer = input("YEAH!!!! Maybe then you like computer games also? yea''hm not really': ").lower()
                    if answer == 'yea' or answer == 'joo':
                        print("That`s cool but sorry i need to go!")
                    elif answer == 'hm not really' or answer == 'hm nope':
                        print("That`s not cool but sorry i need to go!")
                    else:
                        print("Sorry I cannot understand your answer!")
                elif answer == 'hip-hop' or answer == 'rap':
                    answer = input("Yoooo!!!! Maybe then you like computer games also?'I like it!'\
'Absolutely''hm not really''hm nope': ").lower()
                    if answer == 'i like it!' or answer == 'absolutely':
                        print("That`s cool but sorry i need to go!")
                    elif answer == 'hm not really' or answer == 'hm nope':
                        print("That`s not cool but sorry i need to go!")
                    else:
                        print("Sorry I cannot understand your answer!")
                #elif answer != 'hip-hop' or answer != 'rap':
                #    print("wrong message sorry!")
                else:
                    print("Wrong message sorry!")
            else:
                print("Wrong input!")
        else:
            print("Can not understand!")
            if answer == 'of course!' or answer == 'yeah':
                print("That`s cool but sorry I need to go!")
    elif age >= 65:
        print("Unfortunately this software is not recommended for elderly people")
    else:
        print("Unfortunately you are too young to use this software")
elif answer == 'nothing much' or answer == 'bad' or answer == 'nothing special':
    answer = input("Oh :C, Where are you now?'at the university''in school' ").lower()
    if answer == 'in school' or answer == 'at the university':
        answer = input("I wish you luck. Do you like cooking?'sure''yes': ").lower()
        if answer == 'yes' or answer == 'sure':
            answer = input("Me too! Which type of food is your favorite?'rice''sausages' ").lower()
            if answer == 'sausages' or answer == 'rice':
                answer = input("Cool!!!! Maybe then you like computer games also?'yea''yep': ").lower()
                if answer == 'yep' or answer == 'yea':
                    print("That`s cool but sorry i need to go!")
                elif answer == 'hm not really' or answer == 'hm no':
                    print("That`s not cool but sorry i need to go!")
                else:
                    print("Can not understand")
            elif answer == 'hip-hop' or answer == 'rap':
                answer = input("Yoooo!!!! Maybe then you like computer games also?'yea''hm.. not really': ").lower()
                if answer == 'yea' or answer == 'yea':
                    print("That`s cool but sorry i need to go!")
                elif answer == 'hm.. not really' or answer == 'hm.. no':
                    print("That`s not cool but sorry i need to go!")
                else:
                    print("cant understand...")
            else:
                print("I cant understand...")
    elif answer == 'no' or answer == 'not really':
        answer = input("okay.Maybe then you like computer games?'hm nope''yeah': ").lower()
        if answer == 'hm nope' or answer == 'yeah':
            print("That`s cool but sorry i need to go!")
        else:
            print('Sorry Can not understand!!!!!')
    else:
        print("Cant understand your input sir")

else:
    print("Can not understand")


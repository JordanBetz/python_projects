import getpass
from collections import Counter

if __name__ == '__main__':

    # Ersetzt die Benutzereingabe mit getpass
    user_word = getpass.getpass(prompt='Type your word: ')
    user_word = user_word.upper()

    word = user_word

    # Gibt eine Hinweisnachricht aus
    print('Guess the word!')

    # Initialisiert Variablen
    for i in word:
        print('_', end=' ')
    print()

    playing = True
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    fail = 0
    case = ["\n+---+\n|   |\n|\n|\n|\n|\n=========", "\n+---+\n|   |\nO   |\n|\n|\n|\n=========", "+---+\n|   |\nO   |\n|   |\n|\n|\n=========", "+---+\n|   |\nO   |\n/|   |\n|\n|\n=========", "+---+\n|   |\nO   |\n/|\  |\n|\n|\n=========", "+---+\n|   |\nO   |\n/|\  |\n/    |\n|\n=========", " +---+\n|   |\nO   |\n/|\  |\n/ \  |\n|\n========="]
    current_case_index = 0
    
    try:
        while (chances != 0) and flag == 0:
            print()
            chances -= 1
            try:
                guess = str(input('Enter a letter to guess: '))
                guess = guess.upper()
            except:
                print('Enter only a letter!')
                continue

            # Validierung des eingegebenen Buchstabens
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue
            

            # Überprüft, ob der geratene Buchstabe im Wort ist
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess
            else:
                print("This letter is not in the word you are looking for.")
                fail += 1
                print(case[current_case_index])
                current_case_index += 1

            # Gibt das Wort mit geratenen Buchstaben aus
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1
                elif (Counter(letterGuessed) == Counter(word)):
                    print('The word is:', end=' ')
                    print(word)
                    flag = 1
                    print('Congratulations, You won!')
                    break
                else:
                    print('_', end=' ')

        # Wenn keine Chancen mehr übrig sind und das Wort nicht erraten wurde
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()
        
#
#                                         .                  .
#                                     ....                    ....
#                                 .....                          .....
#                               ......                            ......
#                             .......                              .......
#                  .......   .......         ......                 .......
#                  .......   .......         ......                 .......
#                  .......  ........         ......                 ........
#                  .......  ........         ......                 ........
#                 ........  .........        ...........           .........
#           .............. ......   .....    .............  ......   ...... ..... ....      ......
#         ........ ....... ......  .... .... ......  ...... ......   ...... ............  ..........
#         ........ ....... ...... ....  .... ......  ...... ......   ...... .....    ... .....  .....
#         ........ ....... ...... ....  .... ......  ...... ......   ...... .....        .....  .....
#          ............... ......  ...  .... .............   .....   ...... .....         ....  ....
#            ..........    ......  .... .....  .........      ............. .....           ......

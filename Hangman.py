def secret_word():  # The secret word is created within this function.
    secret_word = str(input("please enter the secret word" "\n")).lower()
    secret_word_letters = []
    for letters in secret_word:
        secret_word_letters.append(letters)

    return secret_word, secret_word_letters  # Return the secret word; Returns its letters as an extra list


def index_finder(guess, solution_letters):  # Takes the player guess and the solution list as arguments
    begin = -1
    index_list = []
    while True:
        try:
            index = solution_letters.index(guess, begin + 1)
        except ValueError:
            break
        else:
            index_list.append(index)
            begin = index
    return index_list  # Returns a new list that contains the positions of the guessed the guess within the solution


def play():
    solution = secret_word()
    solution_word = solution[0]
    solution_letters = solution[1]
    #   print(solution_word, solution_letters) #Uncomment to display the secret word after declaring it
    tries = 7

    word_blank = "_" * len(solution_word)
    word_blank_list = list(word_blank)
    string = ""
    for i in word_blank_list:
        string += i
    guessed = False

    while guessed == False:
        print(string)
        if tries != 0:
            print("You have " + str(tries - 1) + " wrong guesses left")
            guess = input("Please guess a letter" "\n").lower()

            if len(guess) > 1:
                guess_list = list(guess)
                if guess_list == solution_letters:
                    print('Congratulations, you won! The solution was: "' + str(solution_word) + '"')
                    break
                else:
                    tries = 0
                    print('Sorry, that was the wrong word. Better luck next time! The solution was: "' + str(
                        solution_word) + '"')
                    break

            if guess in solution_letters:
                #               right_letters.append(guess)
                print("Correct guess")
                index = index_finder(guess, solution_letters)
                for number in index:
                    word_blank_list[number] = guess
                string = ""
                for i in word_blank_list:
                    string += i
                if word_blank_list == solution_letters:
                    print('Congratulations, you won! The solution was: "' + str(solution_word) + '"')
                    break
            else:
                #               wrong_letters.append(guess)
                print("Wrong guess")
                if tries > 0:
                    tries -= 1
        else:
            print('Looks like you ran out of guesses. The solution was: "' + str(solution_word) + '"')
            break

    repeat = input("Would you like to play again? Y/N" "\n").lower()
    if repeat == "y":
        play()


def main():
    play()


main()

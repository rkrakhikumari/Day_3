import random

def choose_word():
    word_list = ["python","java","javascript","css","html","django"]
    return random.choice(word_list)

def display_word(word, guessed_letter):
    display =""
    for letter in word:
        if letter in guessed_letter:
            display += letter
        else:
            display += "_"
    return display

def display_hangman(attempts):
    stages = [
        """
            ---------
            |       |
                    |
                    |
                    |
                    |

        """,
        """
            ---------
            |       |
            o       |
                    |
                    |
                    |

        """,
        """
            ---------
            |       |
            o       |
            |       |
                    |
                    |

        """,
        """
            ---------
            |       |
            o       |
           /|       |
                    |
                    |

        """,
                
        """
            ---------
            |       |
            o       |
           /|\\      |
                    |
                    |

        """,
        """
            ---------
            |       |
            o       |
           /|\\      |
           /        |
                    |

        """,
        """
            ---------
            |       |
            o       |
           /|\\      |
           / \\      |
                    |

                    
        """
]
    return stages[attempts]


def hangman():
    max_attempts = 6
    word_to_guess = choose_word()
    guessed_letter = []
    attempts = 0

    print("Welcome to hangman!!!")

    while True:
        print("\n" + display_hangman(attempts))
        print("\n" + display_word(word_to_guess,guessed_letter))
        guess = input("Guess a letter:").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("please enter a single letter.")
            continue
        if guess in guessed_letter:
            print("You have already guessed that letter.")
            continue

        guessed_letter.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            attempts +=1
            print("wrong guess")
            print(f"attempt left: {max_attempts - attempts}")

        if "_" not in display_word(word_to_guess,guessed_letter):
            print("Congratrulation! you guessed the word: "+word_to_guess)
            break

        if attempts>= max_attempts:
            print("you are out of attempts! the word was: "+word_to_guess)
            break

if __name__ == "__main__":
    hangman()

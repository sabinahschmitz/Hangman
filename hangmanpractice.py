def hangman(word): 
    wrongtries = 0
    hanging = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    letterlist = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to the game of Hangman")
    while wrongtries < len(hanging) - 1:
        print("\n")
        prompt = "Guess a letter: "
        char = input(msg)
        if char in letterlist:
            charposition = letterlist.index(char)
            board[charposition] = char 
            letterlist[charposition] = '$'
        else: 
            wrongtries += 1
        print((" ".join(board)))
        e = wrongtries + 1
        print("\n".join(hanging[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("you lose :( - The word was {}").format(word)
        print("\n".join(hanging[0:wrongtries]))
hangman("cat")
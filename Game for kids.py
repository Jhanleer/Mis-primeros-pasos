import random, sys
#GUESS THE NUMBER GAME

print("Witch game do you want to play? 1. Guess the number 2. Rock, Paper, Scissors")
game = int(input("Enter the number of the game: "))

if game==1:

    print("Guess the secret number between 1 and 20")
    for i in range(5):
        secret = random.randint(1, 20)
        guess = int(input("Enter your guess: "))

        if guess>secret:
            print("The secret number is smaller")
        elif guess<secret:
            print("The secret number is bigger")
        else:
            break
    
    if guess == secret:
        print("You guessed the secret number")
    else:
        print(f"You didn't guess the secret number{secret}")
        
elif game==2:

    print("ROCK, PAPER, SCISSORS")

    win=0
    lose=0
    tie=0

    while True:
        print("%s Wins, %s Losses, %s Ties" % (win, lose, tie))
        while True: #Player move
            print("Enter your move: (r)Rock, (p)Paper, (s)Scissors or (q)Quit")
            playerMove=input()
            if playerMove=="q":
                sys.exit()
            if playerMove=="r" or playerMove=="p" or playerMove=="s":
                break #Exit the player move loop
            print("Type one of r, p, s or q")
        #player move
        if playerMove == "r":
            print("Rock versus...")
        if playerMove == "p":
            print("Paper versus...")
        if playerMove == "s":
            print("Scissor versus...")

        #Display what the computer move
        randomNumber= random.randint(1, 3)

        if randomNumber==1:
            computerMove="r"
            print("Rock")
        elif randomNumber==2:
            computerMove="p"
            print("Paper")
        elif randomNumber==3:
            computerMove="s"
            print("Scissors")

        # Display and record the win/loss/tie:   
        if playerMove==computerMove:
            print("It's a tie!")
            tie+=1
        elif playerMove=="r" and computerMove=="s":
            print("You win!")
            win+=1
        elif playerMove=="p" and computerMove=="r":
            print("You win!")
            win+=1
        elif playerMove=="s" and computerMove=="p":
            print("You win!")
            win+=1
        elif playerMove=="r" and computerMove=="P":
            print("You lose!")
            lose+=1
        elif playerMove=="p" and computerMove=="s":
            print("You lose!")
            lose+=1
        elif playerMove=="s" and computerMove=="r":
            print("You lose!")
            lose+=1
    
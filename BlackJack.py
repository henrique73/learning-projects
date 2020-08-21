import random

money = int(250)

def bid():
    global money
    global GameBid
    print("")
    print ("Your Money total is : ",money)
    print("")
    PlayerInput = input('How much do you want to bid? : ')
    if PlayerInput.isdigit():
        PlayerInput = int(PlayerInput)
        if PlayerInput <= money:
            GameBid = PlayerInput
        else:
            print("You don't have enough money")
            bid()
    else:
        print("That's not a valid input")
        bid()


def game():
    global P1st
    global P2nd
    global total
    print("")
    print("")
    print("")
    print("--Welcome to the game of BlackJack!--")
    P1st = random.randrange(1,11)
    P2nd = random.randrange(1,11)
    total = P1st + P2nd
    print ("Your First Card : ",P1st)
    print ("Your Second Card : ",P2nd)
    print ("-----------------------")
    print ("Your Total :",P1st+P2nd)
    if (P1st+P2nd) == 21:
        print("A Natural! You Win!")
        print ("*-----------------------*")
        bid()
        game()
    question()

def question():
    global money
    global GameBid
    global total
    Pergunta = str(input('Do you want to Stand or Hit? : '))
    if Pergunta.lower() == "hit" or Pergunta.lower() == "h":
        hit = random.randrange(1,11)
        print("")
        print("")
        total = total+hit
        print ("Your Card : ",hit)
        print ("Your Total :",total)
        if total > 21:
            print("You Went over 21! You Lose!")
            money = money - GameBid
            bid()
            game()
        if total == 21:
            print("BlackJack! You have a 21")
            print ("*-----------------------*")
            money = money + GameBid
            bid()
            game()
        else:
            question()
    if Pergunta.lower() == "stand" or Pergunta.lower() == "s":
        D1st = random.randrange(1,11)
        D2nd = random.randrange(1,11)
        Dtotal = D1st+D2nd
        if Dtotal > 21:
            print("You Win,Dealer Went over 21, With :",Dtotal)
            money = money + GameBid
            bid()
            game()
        if Dtotal >= 17:
            if Dtotal > total:
                print("You Lost! Dealer has",Dtotal)
                money = money - GameBid
                bid()
                game()
        else:
            while Dtotal <= 17:
                D3rd = random.randrange(1,11)
                Dtotal = Dtotal + D3rd
                if Dtotal > 21:
                    print("You Win,Dealer Went over 21, With :",Dtotal)
                    money = money + GameBid
                    bid()
                    game()
            if Dtotal > 21:
                print("You Win,Dealer Went over 21, With :",Dtotal)
                money = money + GameBid
                bid()
                game()
            if Dtotal > total:
                print("You Lost! Dealer has",Dtotal)
                money = money - GameBid
                bid()
                game()
            if Dtotal == total:
                print("None Wins! Dealer and player has the same Total!")
                bid()
                game()
            else:
                print("You Win! You have a",total)
                print("And the Dealer Had a",Dtotal)
                money = money + GameBid
                bid()
                game()

bid()
game()
question()


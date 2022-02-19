#roulette
import random
import time
import string
spinner = [[00,"no","no"],[0,"no","no"],[1,"red","1st12"],[2,"black","1st12"],[3,"red","1st12"],[4,"black","1st12"],[5,"red","1st12"],[6,"black","1st12"],
           [7,"red","1st12"],[8,"black","1st12"],[9,"red","1st12"],[10,"black","1st12"],[11,"black","1st12"],[12,"red","1st12"],[13,"black","2nd12"],
           [14,"red","2nd12"],[15,"black","2nd12"],[16,"red","2nd12"],[17,"black","2nd12"],[18,"red","2nd12"],[19,"red","2nd12"],[20,"black","2nd12"],
           [21,"red","2nd12"], [22,"black","2nd12"], [23,"red","2nd12"], [24,"black","2nd12"], [25,"red","3rd12"], [26,"black","3rd12"],
           [27, "red","3rd12"],[28,"black","3rd12"],[29,"black","3rd12"],[30,"red","3rd12"],[31,"black","3rd12"],[32,"red","3rd12"], [33,"red","3rd12"],
           [34,"red","3rd12"],[35,"black","3rd12"],[36,"red","3rd12"]]
chips =  15
def game():
    global spinner
    global chips
    global play
    bet = 0
    print("Here we go!")
    time.sleep(1)
    print("You have " , chips, "chips.")
    time.sleep(1.5)
    bett=string.capwords(input("What would you like to bet on?(red, black, evens, odds, 1st-3rd 12, any number from 00 to 36), or zeroes."))
    if bett == "Black" or bett == "Blacks":
        bet=int(input("How much would you like to bet?"))
        if bet < 0:
            print("Your bet cannot be less than zero. That is blatant cheating. You have beed kicked.")
            time.sleep(3)
            exit()
        while bet > chips or bet == 0:
            bet = int(input("You cannot bet more chips than you have. Please bet a legal number."))
        if not bet > chips and not bet <0 and not bet == 0:
            input("Player bet on Black! Press enter to spin the wheel!")
            print("Wheel is spinning!...")
            time.sleep(4)
            landed = random.choice(spinner)
            if landed[1] == "black":
                chips = chips + bet
                print("Ball landed on a black" , landed[0], "! You win!")
                print("You now have ", chips," chips!")
                if chips == 0:
                    print("Oh no, you've gone bust! Please remove yourself from the game.")
                    time.sleep(2.5)
                    exit()
                play = string.capwords(input("Would you like to play again? Type Y/N Type Y/N"))
                if play == "Y" or play == "Yes":
                    print("Ok, playing again!")
                    time.sleep(1)
                    game()
                elif not play == "Y" or not play == "Yes":
                    print("Ok then, good playing. You finished the game with ", chips," chips.")
                    time.sleep(2.5)
                    exit()
            elif landed[1] == "red":
                chips = chips - bet
                print("oh no, the ball landed on a red " , landed[0], "! You lost!")
                print("You now have ", chips," chips!")
                if chips == 0:
                    print("Oh no, you've gone bust! Please remove yourself from the game.")
                    time.sleep(2.5)
                    exit()
                play = string.capwords(input("Would you like to play again? Type Y/N Type Y/N"))
                if play == "Y" or play == "Yes":
                    print("Ok, playing again!")
                    time.sleep(1)
                    game()
                elif not play == "Y" or not play == "Yes":
                    print("Ok then, good playing. You finished the game with ", chips," chips.")
                    time.sleep(2.5)
                    exit()
            elif landed[1] == "no":
                chips = chips - bet
                print("You unlucky bastard, you landed on a colorless" , landed[0], "! You impressively lost.")
                print("You now have ", chips," chips!")
                if chips == 0:
                    print("Oh no, you've gone bust! Please remove yourself from the game.")
                    time.sleep(2.5)
                    exit()
                play = string.capwords(input("Would you like to play again? Type Y/N Type Y/N"))
                if play == "Y" or play == "Yes":
                    print("Ok, playing again!")
                    time.sleep(1)
                    game()
                elif not play == "Y" or not play == "Yes":
                    print("Ok then, good playing. You finished the game with ", chips," chips.")
                    time.sleep(2.5)
                    exit()
        exit()
    elif bett == "Red" or bett == "Reds":
        bet=int(input("How much would you like to bet?"))
        if bet < 0:
            print("Your bet cannot be less than zero. That is blatant cheating. You have beed kicked.")
            time.sleep(3)
            exit()
        while bet > chips or bet == 0:
            bet = int(input("You cannot bet more chips than you have. Please bet a legal number."))
        if not bet > chips and not bet <0 and not bet == 0:
            input("Player bet on Red! Press enter to spin the wheel!")
            print("Wheel is spinning!...")
            time.sleep(4)
            landed = random.choice(spinner)
            if landed[1] == "red":
                chips = chips + bet
                print("Ball landed on a red" , landed[0], "! You win!")
                print("You now have ", chips," chips!")
                if chips == 0:
                    print("Oh no, you've gone bust! Please remove yourself from the game.")
                    time.sleep(2.5)
                    exit()
                play = string.capwords(input("Would you like to play again? Type Y/N"))
                if play == "Y" or play == "Yes":
                    print("Ok, playing again!")
                    time.sleep(1)
                    game()
                elif not play == "Y" or not play == "Yes":
                    print("Ok then, good playing. You finished the game with ", chips," chips.")
                    time.sleep(2.5)
                    exit()
            elif landed[1] == "black":
                chips = chips - bet
                print("oh no, the ball landed on a black " , landed[0], "! You lost!")
                print("You now have ", chips," chips!")
                if chips == 0:
                    print("Oh no, you've gone bust! Please remove yourself from the game.")
                    time.sleep(2.5)
                    exit()
                play = string.capwords(input("Would you like to play again? Type Y/N"))
                if play == "Y" or play == "Yes":
                    print("Ok, playing again!")
                    time.sleep(1)
                    game()
                elif not play == "Y" or not play == "Yes":
                    print("Ok then, good playing. You finished the game with ", chips," chips.")
                    time.sleep(2.5)
                    exit()
            elif landed[1] == "no":
                chips = chips - bet
                print("You unlucky bastard, you landed on a colorless" , landed[0], "! You impressively lost.")
                print("You now have ", chips," chips!")
                if chips == 0:
                    print("Oh no, you've gone bust! Please remove yourself from the game.")
                    time.sleep(2.5)
                    exit()
                play = string.capwords(input("Would you like to play again? Type Y/N"))
                if play == "Y" or play == "Yes":
                    print("Ok, playing again!")
                    time.sleep(1)
                    game()
                elif not play == "Y" or not play == "Yes":
                    print("Ok then, good playing. You finished the game with ", chips," chips.")
                    time.sleep(2.5)
                    exit()
        exit()
    elif bett == "Evens":
        bet=int(input("How much would you like to bet?"))
        if bet < 0:
            print("Your bet cannot be less than zero. That is blatant cheating. You have beed kicked.")
            time.sleep(3)
            exit()
        while bet > chips or bet ==0:
            bet = int(input("You cannot bet more chips than you have. Please bet a legal number."))
        if not bet > chips and not bet <0 and not bet == 0:
            input("Player bet on Evens! Press enter to spin the wheel!")
            print("Wheel is spinning!...")
            time.sleep(4)
            landed = random.choice(spinner)
            if landed[0] % 2 == 0:
                chips = chips + bet
                print("Ball landed on a red" , landed[0], "! You win!")
                print("You now have ", chips," chips!")
                if chips == 0:
                    print("Oh no, you've gone bust! Please remove yourself from the game.")
                    time.sleep(2.5)
                    exit()
                play = string.capwords(input("Would you like to play again? Type Y/N"))
                if play == "Y" or play == "Yes":
                    print("Ok, playing again!")
                    time.sleep(1)
                    game()
                elif not play == "Y" or not play == "Yes":
                    print("Ok then, good playing. You finished the game with ", chips," chips.")
                    time.sleep(2.5)
                    exit()
            elif landed[0] == "0" or landed[0]=="00":
                hips = chips - bet
                print("You unlucky bastard, you landed on a colorless" , landed[0], "! You impressively lost.")
                print("You now have ", chips," chips!")
                if chips == 0:
                    print("Oh no, you've gone bust! Please remove yourself from the game.")
                    time.sleep(2.5)
                    exit()
                play = string.capwords(input("Would you like to play again? Type Y/N"))
                if play == "Y" or play == "Yes":
                    print("Ok, playing again!")
                    time.sleep(1)
                    game()
                elif not play == "Y" or not play == "Yes":
                    print("Ok then, good playing. You finished the game with ", chips," chips.")
                    time.sleep(2.5)
                    exit()
            else:
                chips = chips - bet
                print("Oh no, you landed on the ",landed[1]," ",landed[0],".")
                print("You now have ", chips," chips!")
                if chips == 0:
                    print("Oh no, you've gone bust! Please remove yourself from the game.")
                    time.sleep(2.5)
                    exit()
                play = string.capwords(input("Would you like to play again? Type Y/N"))
                if play == "Y" or play == "Yes":
                    print("Ok, playing again!")
                    time.sleep(1)
                    game()
                elif not play == "Y" or not play == "Yes":
                    print("Ok then, good playing. You finished the game with ", chips," chips.")
                    time.sleep(2.5)
                    exit()
        exit()
    elif bett == "Odds":
        bet=int(input("How much would you like to bet?"))
        if bet < 0:
            print("Your bet cannot be less than zero. That is blatant cheating. You have beed kicked.")
            time.sleep(3)
            exit()
        while bet > chips or bet ==0:
            bet = int(input("You cannot bet more chips than you have. Please bet a legal number."))
        if not bet > chips and not bet <0 and not bet == 0:
            input("Player bet on Evens! Press enter to spin the wheel!")
            print("Wheel is spinning!...")
            time.sleep(4)
            landed = random.choice(spinner)
            if landed[0] % 2 == 0:
                chips = chips - bet
                print("Oh no ball landed on a ",landed[1]," ", landed[0], "! You lost!")
                print("You now have ", chips," chips!")
                if chips == 0:
                    print("Oh no, you've gone bust! Please remove yourself from the game.")
                    time.sleep(2.5)
                    exit()
                play = string.capwords(input("Would you like to play again? Type Y/N"))
                if play == "Y" or play == "Yes":
                    print("Ok, playing again!")
                    time.sleep(1)
                    game()
                elif not play == "Y" or not play == "Yes":
                    print("Ok then, good playing. You finished the game with ", chips," chips.")
                    time.sleep(2.5)
                    exit()
            elif landed[0] == "0" or landed[0]=="00":
                hips = chips - bet
                print("You unlucky bastard, you landed on a colorless" , landed[0], "! You impressively lost.")
                print("You now have ", chips," chips!")
                if chips == 0:
                    print("Oh no, you've gone bust! Please remove yourself from the game.")
                    time.sleep(2.5)
                    exit()
                play = string.capwords(input("Would you like to play again? Type Y/N"))
                if play == "Y" or play == "Yes":
                    print("Ok, playing again!")
                    time.sleep(1)
                    game()
                elif not play == "Y" or not play == "Yes":
                    print("Ok then, good playing. You finished the game with ", chips," chips.")
                    time.sleep(2.5)
                    exit()
            else:
                chips = chips + bet
                print("The ball landed on the ",landed[1]," ",landed[0],". You win!")
                print("You now have ", chips," chips!")
                if chips == 0:
                    print("Oh no, you've gone bust! Please remove yourself from the game.")
                    time.sleep(2.5)
                    exit()
                play = string.capwords(input("Would you like to play again? Type Y/N"))
                if play == "Y" or play == "Yes":
                    print("Ok, playing again!")
                    time.sleep(1)
                    game()
                elif not play == "Y" or not play == "Yes":
                    print("Ok then, good playing. You finished the game with ", chips," chips.")
                    time.sleep(2.5)
                    exit()
        exit()
    elif bett == "First 12" or bett == "1st 12" or bett == "First Twelve" or bett == "1st Twelve":
        bet=int(input("How much would you like to bet?"))
        if bet < 0:
            print("Your bet cannot be less than zero. That is blatant cheating. You have beed kicked.")
            time.sleep(3)
            exit()
        while bet > chips or bet ==0:
            bet = int(input("You cannot bet more chips than you have. Please bet a legal number."))
        if not bet > chips and not bet <0 and not bet == 0:
            input("Player bet on on the First 12! Payouts are 2:1, press enter to spin the wheel!")
            print("Wheel is spinning!...")
            time.sleep(4)
            landed = random.choice(spinner)
            if landed[2]=="1st12":
                chips = chips + (2*bet)
                print("Ball landed on a ",landed[1]," " , landed[0], "! You win!")
                print("You now have ", chips," chips!")
                if chips == 0:
                    print("Oh no, you've gone bust! Please remove yourself from the game.")
                    time.sleep(2.5)
                    exit()
                play = string.capwords(input("Would you like to play again? Type Y/N"))
                if play == "Y" or play == "Yes":
                    print("Ok, playing again!")
                    time.sleep(1)
                    game()
                elif not play == "Y" or not play == "Yes":
                    print("Ok then, good playing. You finished the game with ", chips," chips.")
                    time.sleep(2.5)
                    exit()
            elif landed[0] == "0" or landed[0]=="00":
                hips = chips - bet
                print("You unlucky bastard, you landed on a colorless" , landed[0], "! That is not counted in the first 12. You impressively lost.")
                print("You now have ", chips," chips!")
                if chips == 0:
                    print("Oh no, you've gone bust! Please remove yourself from the game.")
                    time.sleep(2.5)
                    exit()
                play = string.capwords(input("Would you like to play again? Type Y/N"))
                if play == "Y" or play == "Yes":
                    print("Ok, playing again!")
                    time.sleep(1)
                    game()
                elif not play == "Y" or not play == "Yes":
                    print("Ok then, good playing. You finished the game with ", chips," chips.")
                    time.sleep(2.5)
                    exit()
            else:
                chips = chips - bet
                print("Oh no, you landed on the ",landed[1]," ",landed[0],".")
                print("You now have ", chips," chips!")
                if chips == 0:
                    print("Oh no, you've gone bust! Please remove yourself from the game.")
                    time.sleep(2.5)
                    exit()
                play = string.capwords(input("Would you like to play again? Type Y/N"))
                if play == "Y" or play == "Yes":
                    print("Ok, playing again!")
                    time.sleep(1)
                    game()
                elif not play == "Y" or not play == "Yes":
                    print("Ok then, good playing. You finished the game with ", chips," chips.")
                    time.sleep(2.5)
                    exit()
    elif bett == "Second 12" or bett == "2nd 12" or bett == "Second Twelve" or bett == "2nd Twelve":
        bet=int(input("How much would you like to bet?"))
        if bet < 0:
            print("Your bet cannot be less than zero. That is blatant cheating. You have beed kicked.")
            time.sleep(3)
            exit()
        while bet > chips or bet ==0:
            bet = int(input("You cannot bet more chips than you have. Please bet a legal number."))
        if not bet > chips and not bet <0 and not bet == 0:
            input("Player bet on Second 12! Press enter to spin the wheel!")
            print("Wheel is spinning!...")
            time.sleep(4)
            landed = random.choice(spinner)
            if landed[1] == "2nd12":
                chips = chips + (2*bet)
                print("Ball landed on a ",landed[1]," " , landed[0], "! You win!")
                print("You now have ", chips," chips!")
                if chips == 0:
                    print("Oh no, you've gone bust! Please remove yourself from the game.")
                    time.sleep(2.5)
                    exit()
                play = string.capwords(input("Would you like to play again? Type Y/N"))
                if play == "Y" or play == "Yes":
                    print("Ok, playing again!")
                    time.sleep(1)
                    game()
                elif not play == "Y" or not play == "Yes":
                    print("Ok then, good playing. You finished the game with ", chips," chips.")
                    time.sleep(2.5)
                    exit()
            elif landed[0] == "0" or landed[0]=="00":
                hips = chips - bet
                print("You unlucky bastard, you landed on a colorless" , landed[0], "! You impressively lost.")
                print("You now have ", chips," chips!")
                if chips == 0:
                    print("Oh no, you've gone bust! Please remove yourself from the game.")
                    time.sleep(2.5)
                    exit()
                play = string.capwords(input("Would you like to play again? Type Y/N"))
                if play == "Y" or play == "Yes":
                    print("Ok, playing again!")
                    time.sleep(1)
                    game()
                elif not play == "Y" or not play == "Yes":
                    print("Ok then, good playing. You finished the game with ", chips," chips.")
                    time.sleep(2.5)
                    exit()
            else:
                chips = chips - bet
                print("Oh no, you landed on the ",landed[1]," ",landed[0],".")
                print("You now have ", chips," chips!")
                if chips == 0:
                    print("Oh no, you've gone bust! Please remove yourself from the game.")
                    time.sleep(2.5)
                    exit()
                play = string.capwords(input("Would you like to play again? Type Y/N"))
                if play == "Y" or play == "Yes":
                    print("Ok, playing again!")
                    time.sleep(1)
                    game()
                elif not play == "Y" or not play == "Yes":
                    print("Ok then, good playing. You finished the game with ", chips," chips.")
                    time.sleep(2.5)
                    exit()
        exit()
    elif bett == "Third 12" or bett == "3rd 12" or bett == "Third Twelve" or bett == "3rd Twelve":
        bet=int(input("How much would you like to bet?"))
        if bet < 0:
            print("Your bet cannot be less than zero. That is blatant cheating. You have beed kicked.")
            time.sleep(3)
            exit()
        while bet > chips or bet ==0:
            bet = int(input("You cannot bet more chips than you have. Please bet a legal number."))
        if not bet > chips and not bet <0 and not bet == 0:
            input("Player bet on the Third 12! Press enter to spin the wheel!")
            print("Wheel is spinning!...")
            time.sleep(4)
            landed = random.choice(spinner)
            if landed[1] == "3rd12":
                chips = chips + (2*bet)
                print("Ball landed on a ", landed[1]," " , landed[0], "! You win!")
                print("You now have ", chips," chips!")
                if chips == 0:
                    print("Oh no, you've gone bust! Please remove yourself from the game.")
                    time.sleep(2.5)
                    exit()
                play = string.capwords(input("Would you like to play again? Type Y/N"))
                if play == "Y" or play == "Yes":
                    print("Ok, playing again!")
                    time.sleep(1)
                    game()
                elif not play == "Y" or not play == "Yes":
                    print("Ok then, good playing. You finished the game with ", chips," chips.")
                    time.sleep(2.5)
                    exit()
            elif landed[0] == "0" or landed[0]=="00":
                hips = chips - bet
                print("You unlucky bastard, you landed on a colorless" , landed[0], "! You impressively lost.")
                print("You now have ", chips," chips!")
                if chips == 0:
                    print("Oh no, you've gone bust! Please remove yourself from the game.")
                    time.sleep(2.5)
                    exit()
                play = string.capwords(input("Would you like to play again? Type Y/N"))
                if play == "Y" or play == "Yes":
                    print("Ok, playing again!")
                    time.sleep(1)
                    game()
                elif not play == "Y" or not play == "Yes":
                    print("Ok then, good playing. You finished the game with ", chips," chips.")
                    time.sleep(2.5)
                    exit()
            else:
                chips = chips - bet
                print("Oh no, you landed on the ",landed[1]," ",landed[0],". You lost!")
                print("You now have ", chips," chips!")
                if chips == 0:
                    print("Oh no, you've gone bust! Please remove yourself from the game.")
                    time.sleep(2.5)
                    exit()
                play = string.capwords(input("Would you like to play again? Type Y/N"))
                if play == "Y" or play == "Yes":
                    print("Ok, playing again!")
                    time.sleep(1)
                    game()
                elif not play == "Y" or not play == "Yes":
                    print("Ok then, good playing. You finished the game with ", chips," chips.")
                    time.sleep(2.5)
                    exit()
        exit()
    elif bett == "Zeroes":
        bet=int(input("How much would you like to bet?"))
        if bet < 0:
            print("Your bet cannot be less than zero. That is blatant cheating. You have beed kicked.")
            time.sleep(3)
            exit()
        while bet > chips or bet ==0:
            bet = int(input("You cannot bet more chips than you have. Please bet a legal number."))
        if not bet > chips and not bet <0 and not bet == 0:
            input("Player bet on ZEROES! Payout is 17:1, please press enter to spin the wheel!")
            print("Wheel is spinning!...")
            time.sleep(4)
            landed = random.choice(spinner)
            if landed[2] == "no":
                chips = chips + (17*bet)
                print("THE BALL LANDED ON " , landed[0], "! YOU WIN!")
                print("You now have ", chips," chips!")
                if chips == 0:
                    print("Oh no, you've gone bust! Please remove yourself from the game.")
                    time.sleep(2.5)
                    exit()
                play = string.capwords(input("Would you like to play again? Type Y/N"))
                if play == "Y" or play == "Yes":
                    print("Ok, playing again!")
                    time.sleep(1)
                    game()
                elif not play == "Y" or not play == "Yes":
                    print("Ok then, good playing. You finished the game with ", chips," chips.")
                    time.sleep(2.5)
                    exit()
            else:
                chips = chips - bet
                print("Oh no, you landed on the ",landed[1]," ",landed[0],". You lost!")
                print("You now have ", chips," chips!")
                if chips == 0:
                    print("Oh no, you've gone bust! Please remove yourself from the game.")
                    time.sleep(2.5)
                    exit()
                play = string.capwords(input("Would you like to play again? Type Y/N"))
                if play == "Y" or play == "Yes":
                    print("Ok, playing again!")
                    time.sleep(1)
                    game()
                elif not play == "Y" or not play == "Yes":
                    print("Ok then, good playing. You finished the game with ", chips," chips.")
                    time.sleep(2.5)
                    exit()
    elif bett == "A Number" or bett== "Number" or bett == "Numbers":    
            betnum= int(input("What number would you like to bet on?"))
            while betnum> 36:
                betnum= int(input("The wheel goes up to 36. What number would you like to bet on?"))
            bet = int(input("How much would you like to bet on your number?"))
            if bet < 0:
                print("Your bet cannot be less than zero. That is blatant cheating. You have beed kicked.")
                time.sleep(3)
                exit()
            while bet > chips or bet ==0:
                bet = int(input("You cannot bet more chips than you have. Please bet a legal number."))
            if not bet > chips and not bet <0 and not bet == 0:
                betelse= string.capwords(input("Would you like to bet on anything else?"))
                if betelse == "No" or betelse == "N":
                    print("Player bet " , bet," chips on ", betnum,". Payout for one number is 35:1!")
                    input (" Press enter to spin the wheel!")
                    print("Wheel is spinning!...")
                    time.sleep(4)
                    landed = random.choice(spinner)
                    if betnum == landed[0]:
                        chips = chips +(35*bet)
                        print("YOU LANDED ON YOUR NUMBER! YOU WIN!!!")
                        print("YOU NOW HAVE " , chips, " CHIPS!")
                        play = string.capwords(input("Would you like to play again? Type Y/N Type Y/N"))
                        if play == "Yes" or play == "Y":
                            print("Ok, playing again!")
                            time.sleep(2)
                            game()
                        elif play == "No" or play == "N":
                            print("Ok then. Exiting the game.")
                            time.sleep(2)
                            exit()
                    if chips == 0:
                        print("Oh no, you've gone bust! Please remove yourself from the game. ")
                        time.sleep(2)
                        exit()
                    else:
                        chips = chips - bet
                        print("Oh no, you landed on " ,landed[0], ". You lost.")
                        print("You have" ,chips, " chips")
                        if chips == 0:
                            print("Oh no, you've gone bust! Please remove yourself from the game. ")
                            time.sleep(2)
                            exit()
                        if play == "Yes" or play == "Y":
                            print("Ok, playing again!")
                            time.sleep(2)
                            game()
                        elif play == "No" or play == "N":
                            print("Ok then. Exiting the game.")
                            time.sleep(2)
                            exit()
                elif betelse == "Yes" or betelse == "Y":
                    bett2 = int(input("What other number would you like to bet on your number?"))
                    bet2 = int(input("How much would you like to bet on your number?"))
                    if bet < 0:
                        print("Your bet cannot be less than zero. That is blatant cheating. You have beed kicked.")
                        time.sleep(3)
                        exit()
                    while bet2 > chips or bet2 ==0:
                        bet = int(input("You cannot bet more chips than you have. Please bet a legal number."))
                    if not bet2 > chips and not bet <0 and not bet2 == 0:
                        betelse= string.capwords(input("Would you like to bet on anything else?"))
                        if betelse == "No" or betelse == "N":
                            print("Player bet " , bet2," chips on ", bett2,". Payout for two numbers is 17:1!")
                            input (" Press enter to spin the wheel!")
                            print("Wheel is spinning!...")
                            time.sleep(4)
                            landed = random.choice(spinner)
                            if betnum == landed[0] or bet2 == landed[0]:
                                chips = chips +(17*bet)
                                print("You won your bet on " , landed[0],"!!!")
                                print("You now have " , chips, " chips!")
                                play = string.capwords(input("Would you like to play again? Type Y/N Type Y/N"))
                                if play == "Yes" or play == "Y":
                                    print("Ok, playing again!")
                                    time.sleep(2)
                                    game()
                                elif play == "No" or play == "N":
                                    print("Ok then. Exiting the game.")
                                    time.sleep(2)
                                    exit()
                            if chips == 0:
                                print("Oh no, you've gone bust! Please remove yourself from the game. ")
                                time.sleep(2)
                                exit()
                            else:
                                chips = chips - bet
                                chips = chips - bet2
                                print("Oh no, you landed on " ,landed[0], ". You lost.")
                                print("You have" ,chips, " chips")
                                if chips == 0:
                                    print("Oh no, you've gone bust! Please remove yourself from the game. ")
                                    time.sleep(2)
                                    exit()
                                if play == "Yes" or play == "Y":
                                    print("Ok, playing again!")
                                    time.sleep(2)
                                    game()
                                elif play == "No" or play == "N":
                                    print("Ok then. Exiting the game.")
                                    time.sleep(2)
                                    exit()
                       
                        elif betelse == "Yes" or betelse == "Y":
                            bett3 = int(input("What other number would you like to bet on your number?"))
                            bet3 = int(input("How much would you like to bet on ?"))
                            if bet < 0:
                                print("Your bet cannot be less than zero. That is blatant cheating. You have beed kicked.")
                                time.sleep(3)
                                exit()
                            while bet3 > chips or bet3 ==0:
                                bet = int(input("You cannot bet more chips than you have. Please bet a legal number."))
                            if not bet3 > chips and not bet3 <0 and not bet3 == 0:
                                betelse= string.capwords(input("Would you like to bet on anything else?"))
                                if betelse == "N" or betelse == "No":
                                    print("Player bet " , bet3," chips on ", bett3,". Payout for three number is 11:1!")
                                    input (" Press enter to spin the wheel!")
                                    print("Wheel is spinning!...")
                                    time.sleep(4)
                                    landed = random.choice(spinner)
                                    if bett3 == landed[0] or bett2 == landed[0] or betnum== landed[0]:
                                        chips = chips +(11*bet)
                                        print("You landed on ", landed[0],"! You win!")
                                        print("YOU NOW HAVE " , chips, " CHIPS!")
                                        play = string.capwords(input("Would you like to play again? Type Y/N Type Y/N"))
                                        if play == "Yes" or play == "Y":
                                            print("Ok, playing again!")
                                            time.sleep(2)
                                            game()
                                        elif play == "No" or play == "N":
                                            print("Ok then. Exiting the game.")
                                            time.sleep(2)
                                            exit()
                                    if chips == 0:
                                        print("Oh no, you've gone bust! Please remove yourself from the game. ")
                                        time.sleep(2)
                                        exit()
                                    else:
                                        chips = chips - bet
                                        chips = chips - bet2
                                        chips = cheps - bet3
                                        print("Oh no, you landed on " ,landed[0], ". You lost.")
                                        print("You have" ,chips, " chips")
                                        if chips == 0:
                                            print("Oh no, you've gone bust! Please remove yourself from the game. ")
                                            time.sleep(2)
                                            exit()
                                        if play == "Yes" or play == "Y":
                                            print("Ok, playing again!")
                                            time.sleep(2)
                                            game()
                                        elif play == "No" or play == "N":
                                            print("Ok then. Exiting the game.")
                                            time.sleep(2)
                                            exit()
                            elif betelse == "Yes" or betelse == "Y":
                                bett4 = int(input("What other number would you like to bet on your number?"))
                                bet4 = int(input("How much would you like to bet on ?"))
                                if bet < 0:
                                    print("Your bet cannot be less than zero. That is blatant cheating. You have beed kicked.")
                                    time.sleep(3)
                                    exit()
                                while bet4 > chips or bet4 ==0:
                                    bet = int(input("You cannot bet more chips than you have. Please bet a legal number."))
                                if not bet4 > chips and not bet4 <0 and not bet4 == 0:
                                    print("That is the maximum amount of bets that you can place")
                                    time.sleep(2)
                                    print("Player bet " , bet4," chips on ", bett4,". Payout for three numbers is 11:1!")
                                    input (" Press enter to spin the wheel!")
                                    print("Wheel is spinning!...")
                                    time.sleep(4)
                                    landed = random.choice(spinner)
                                    if bett3 == landed[0] or bett2 == landed[0] or betnum== landed[0] or bett4 == landed[0]:
                                        chips = chips +(8*bet)
                                        print("You landed on ", landed[0],"! You win!")
                                        print("YOU NOW HAVE " , chips, " CHIPS!")
                                        play = string.capwords(input("Would you like to play again? Type Y/N"))
                                        if play == "Yes" or play == "Y":
                                            print("Ok, playing again!")
                                            time.sleep(2)
                                            game()
                                        elif play == "No" or play == "N":
                                            print("Ok then. Exiting the game.")
                                            time.sleep(2)
                                            exit()
                                    if chips == 0:
                                        print("Oh no, you've gone bust! Please remove yourself from the game. ")
                                        time.sleep(2)
                                        exit()
                                    else:
                                        chips = chips - bet
                                        chips = chips - bet2
                                        chips = chips - bet3
                                        chips = chips - bet4
                                        print("Oh no, you landed on " ,landed[0], ". You lost.")
                                        print("You have" ,chips, " chips")
                                        if chips == 0:
                                            print("Oh no, you've gone bust! Please remove yourself from the game. ")
                                            time.sleep(2)
                                            exit()
                                        if play == "Yes" or play == "Y":
                                            print("Ok, playing again!")
                                            time.sleep(2)
                                            game()
                                        elif play == "No" or play == "N":
                                            print("Ok then. Exiting the game.")
                                            time.sleep(2)
                                            exit()


 
       
play = string.capwords(input("Welcome to roulette! Would you like to play?"))
while play == "Y" or play == "Yes":
    infobet = string.capwords(input("Do you know what you can bet on and their payouts? If not, type N."))
    if infobet == "N":
        print('Single number bet pays 35 to 1. Double number bet pays 17 to 1. If you bet on three numbes, the payout is 11 to 1. Four number bet pays 8 to 1.Five number bet pays 6 to 1. Only one specific bet which includes the following numbers: 0-00-1-2-3 .Six number bets pays 5 to 1. Example: 7, 8, 9, 10, 11, 12. Also called a “line.')
        input("Press enter to continue.")
        print("Betting on black or red offers a 1:1 payout. Same with evens and odds. First, Second, and Third of 12 means first, second, or third set of 12 numbers. That pays 2:1")
        input("press enter to continue.")
    input("DEVELOPER'S NOTE-- YOU CAN ONLY BET ON UP TO FOUR NUMBERS, AND IF YOU BET ON A NUMBER THAN YOU CAN ONLY BET ON OTHER NUMBERS. Press enter to play the game.")
    game()

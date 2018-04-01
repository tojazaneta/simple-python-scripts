"""Heads or tails game"""
import random

coin = ["HEADS", "TAILS"]
flip = random.choice(coin)

print("Hello, wanna play in heads/tails game? Of course you want."
      "")

def heads_tails_game():
    while True:
        user_choice = str(input("Please choose: heads [h] or tails [t]? ")).upper()
        if user_choice == "H" or user_choice == "HEADS":
            heads_choice = "HEADS"
            print("Okay, so you picked heads.\nLet's flip a coin now.\n*coin flip*")
            print(flip)
            if heads_choice == flip:
                print("Congrats! You won!")

            else:
                print("Maybe next time!")
            break
        if user_choice == "T" or user_choice == "TAILS":
            tails_choice = "TAILS"
            print("Okay, so you picked tails.\nLet's flip a coin now.\n*coin flip*")
            print(flip)
            if tails_choice == flip:
                print("Congrats! You won!")
            else:
                print("Maybe next time!")
            break
        else:
            print("Sorry, I don't understand. Pick heads [h] or tails [t]. ")

heads_tails_game()
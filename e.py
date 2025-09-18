import random
from abc import ABC, abstractmethod
import time
import os
food = ""
complete = "Yes"
client = ""
def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

Non_chicken = [ "Burger", "Hot dog", "Grilled cheese"]
Chicken = [ "Chicken nuggets", "Chicken sandwhich"]
Sauce = ["Ketchup", "Sweet n' Sour", "Mustard", "Mayonaise", "Spicy", "no sauce"]
sides = [ "Fruit cup", "Fries", "Brussel sprouts", "Salad", "Tomato soup", "no side"] 
curse_main = ["'Mystery Meat' sandwhich", "'worker' sandwhich", "you know what I want.", "your shift is over."]
curse_side =["rocks","potentially lethal rocks", "'fries' dipped in 'red sauce'", "broccoli "] 
n_a =[]
one = "A customer walks up and starts to order, looking up at the board." # add on code to randomize there order
two = "A elegantly dressed lady walks in, seeming rather out of place although confident in what she wants to order."
three = "A shady man walks up to the counter, wallet in hand as he glances at the menu"
# ten = "a wisp appears in front of you, holding out its order on a card" add later if you have time
next_customer =[one, two, three]

reg_list = [Non_chicken, Chicken]

class Stage(ABC):
    
    
    def __init__(self,customers,main):
        self.customers =customers 
        self.main = main 
        main = Non_chicken or Chicken
        pass 
    
    def answer(self):
        self.answer != complete
        print(client)
        time.sleep(1)
        print(food)
        time.sleep(2)
        print("What did the customer order?", end = "\r")
        input("what type of main did they order?")
        if input == food:
            print("yay")
            self.answer = complete 
            print("yes")
    
    def order(self):
        food = random.choice(self.main)
        client = random.choice(next_customer)
        


    def stage_setup(self):
        for i in range(self.customers):
            self.order()
            time.sleep(1)
            self.answer()
            if self.answer == complete:
                continue 
            
    def stage_complete(self):
        pass 

test =Stage(n_a, n_a)
class StageOne(Stage):
    def __init__(self, customers, main):
        self.customers = customers
        self.main = main 
    def order(self):
        super().order() 
        print(client) 

class StageThree(Stage):
    def __init__(self,customers,main, side, sauce):
        pass

class StageFour(Stage):
    def __init__(self,customers,main,main2,side,sauce):
        pass

        

s1 =StageOne(2, Non_chicken)

def game_start():
    global s1
    print("You wake up, you realize you start your new job today. Time to get driving.You arrive at the restauraunt, walking in. The manager greets you. Hi! Welcome to your new job at '!@#&*$%#@*'")
    name = input("What's your name? ")
    if name != "skip":
        print("Welcome '" + name + "' to your new job. You can get started over there.")
        print("You walk over to the cash register, a manual sitting next to it") 
        input("the person operating this game will tell you how it works or there will be some sort of guide in person, type anything to continue; ")
        print("Get ready! Your shift begins in 3")
        time.sleep(1)
        print("2!")
        time.sleep(1)
    print("1!")
    time.sleep(1)
    print("Go!")
    clear_terminal()
    time.sleep(1)
    s1.order()
    s1.answer()
    
game_start()
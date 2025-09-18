import random
from abc import ABC, abstractmethod
import time
import os

complete = "Yes"
client = ""
def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

Meat = [ "Cheeseburger", "Hot dog", "Single patty burger", "Burger", "Kid's hotdog"]
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

reg_list = [Meat, Chicken]

class Stage(ABC):
    
    
    def __init__(self,customers,main):
        self.customers =customers 
        self.main = main 
        pass 
    

    
    def order(self):
        client = random.choice(next_customer)
        print(client)
        


    def stage_setup(self):
        for i in range(self.customers):
            self.order()
            time.sleep(1)
            self.answer()
            
            
    def answer(self): #fix the printing system 
        self.answer != complete
        question = input("what type of main did they order? A Chicken or a Meat main?")
        if question == self.main: 
            print("What did they order from this category?")
            response = input(print(self.main + "?"))
            if response == self.food:
                self.answer = complete 
                print("yes")    
                
        # elif:
        #     if question != self.main:
        #         print("Please try again. This is what the customer wanted for their main.")
        #         print(self.food)
            
    def stage_complete(self):
        pass 

test =Stage(n_a, n_a)
class StageOne(Stage):
    def __init__(self, customers):
        self.customers = customers
        self.main = Meat 
    def order(self):
        food = random.choice(self.main)
        super().order() 
        print("The customer wants:" + food )
    def stage_setup(self):
        self.main = Meat
        super().stage_setup()

class StageThree(Stage):
    def __init__(self,customers,main, side, sauce):
        pass

class StageFour(Stage):
    def __init__(self,customers,main,main2,side,sauce):
        pass

        

s1 =StageOne(2)

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
    # clear_terminal()
    s1.stage_setup()
    
game_start()
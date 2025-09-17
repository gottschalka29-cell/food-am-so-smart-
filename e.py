import math
import random
from abc import ABC, abstractmethod

Non_chicken = [ "Burger", "Hot dog", "Grilled cheese"]
Chicken = [ "Chicken nuggets", "Chicken sandwhich"]
Sauce = ["Ketchup", "Sweet n' Sour", "Mustard", "Mayonaise", "Spicy", "no sauce"]
sides = [ "Fruit cup", "Fries", "Brussel sprouts", "Salad", "Tomato soup", "no side"] 
curse_main = ["'Mystery Meat' sandwhich", "'worker' sandwhich", "you know what I want.", "your shift is over."]
curse_side =["rocks","potentially lethal rocks", "'fries' dipped in 'red sauce'", "broccoli "] 

reg_list = [Non_chicken, Chicken]
class Stage(ABC):
    def __init__(self,customers):
        self.customers =customers 
        pass 
    
    

    def order(self):
        for i in range(self.customers): 
            print("A customer walks up and starts to order, looking up at the board.") # add on code to randomize there order 
            choice = (random.choice(reg_list))
            item = random.choice(choice)
            item2 = random.choice(choice)
            print("I would like to have " + item + " and " item2)
            
    

s = Stage(4)

def game_start():

    print("You wake up, you realize you start your new job today. Time to get driving.You arrive at the restauraunt, walking in. The manager greets you. Hi! Welcome to your new job at '!@#&*$%#@*'")
    name = input("What's your name? ")
    print("Welcome " + name + " to your new job. You can get started over there.")
    print("You walk over to the cash register, a manual sitting next to it") 
    input("the person operating this game will tell you how it works or there will be some sort of guide in person, type anything to continue; ")
   #stage one begins 
   
game_start()
s.order()
# Part 1 - Quizz :

# What is a class?
# It is like a recipe for creating something or an object. It says what data and actions that the object will have.

# What is an instance? 
# The instance are the "things" you use for the class. Each "thing" is an instance.

# What is encapsulation? 
# It's like putting all the important stuff, the data and how to use it inside a container that is the class. Encapsulation is very useful for keeping "things" organized.

# What is abstraction? 
# Abstraction is the process of hiding complex implementation details and showing only the necessary information to the user.

# What is inheritance?
# Inheritance it is a class the attributes and methods of an existing class (the base or parent class).

# What is multiple inheritance?
# Multiple inheritance is a feature in some object-oriented programming languages where a class can inherit attributes and methods from more than one parent class.

# What is polymorphism?
# Polymorphism is the ability of objects of different classes to respond to the same method call in their own specific ways

# What is method resolution order or MRO?
# This method, in cases of inheritance, especially multiple inheritance, is useful to determine which inherited method should be executed

#Part 2 : Create a deck of Cards Class 

import random

class Deck:
    def __init__(self):
        self.cards = []
        self._build_deck()

    def _build_deck(self):
        suits = ["Heart", "Diamond", "Club", "Spade"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        for suit in suits:
            for value in values:
                new_card = Card(suit, value)
                self.cards.append(new_card)

    def shuffle(self):
        if len(self.cards) == 52:
            random.shuffle(self.cards)
        else:
            print("The deck doesn't have all the 52 cards, impossible to blend.")

    def deal(self):
        
        if self.cards:
            dealt_card = self.cards.pop()
            return dealt_card
        else:
            print("The deck is empty, impossible to spread.")
            return None

    def __str__(self):
        return f"Deck from{len(self.cards)} cartds : {[str(card) for card in self.cards]}"

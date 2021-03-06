import json
import random

class Deck:
    def __init__(self, deckName):
        f = open("cards.json")
        cardDict =  json.load(f)
        self.deck = cardDict[deckName]
        self.size = len(cardDict[deckName])
        self.index = random.randint(0, self.size - 1)

    def increment(self):
        if (self.index == self.size - 1):
            self.index = 0
        else:
            self.index += 1
    
    def getCard(self):
        return self.deck[self.index]

    def getFrontCard(self):
        return self.getCard()[0]
    
    def getBackCard(self):
        return self.getCard()[1]
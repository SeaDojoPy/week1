"""
place to do OOPy things
"""
import random

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class CoolNode(Node):
    def __init__(self, data):
        super(CoolNode, self).__init__(data)
        self.prev = None

class List(object):
    def __init__(self):
        self.head = None
    
    def addFront(self, data):
        neo = CoolNode(data)
        if not self.head:
            self.head = neo
        else:
            temp = self.head
            neo.next = temp
            self.head = neo
        return self
    

class Card(object):
    def __init__(self, val, suit, name):
        self.val = val
        self.suit = suit
        self.name = name
    
    def __repr__(self):
        return "<Card object name: {}, suit: {}, value: {}>".format(self.name, self.suit, self.val)

class Deck(object):

    @classmethod
    def build_deck(self):
        suits = ['hearts', 'clubs', "diamonds", "spades"]
        face_cards = {
            10: "Jack",
            11: "Queen",
            12: "King",
            13: "Ace"
        }
        deck = []
        for i in xrange(1,10):
            for suit in suits:
                deck.append(Card(i, suit, i))
        for i in xrange(10,14):
            for suit in suits:
                deck.append(Card(i, suit, face_cards[i]))
        return deck

    def shuffle(self, arr):
        back = len(arr)-1
        while back > 0:
            rand_idx = random.randint(0, back)
            arr[rand_idx], arr[back] = arr[back], arr[rand_idx]
            back = back-1
        return arr
        


    def __init__(self):
        self.cards = self.shuffle(Deck.build_deck())
    
    def __repr__(self):
        print "This is a Deck with these things in it"
        for card in self.cards:
            print card
        return "yoyoyo!"
    
class Player(object):
    def __init__(self):
        self.name = "alan"



class Bike(object):
    '''
    this is a bike. it has price max speed and miles
    '''
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def display_info(self):
        '''
        be informed
        '''
        print self
        return self
    
    def ride(self):
        '''
        put 10 miles on the bike
        '''
        self.miles = self.miles+10
        return self

    def reverse(self):
        '''
        go backwards...
        '''
        self.miles = self.miles-5 if self.miles-5 > 0 else 0
        return self

    def __repr__(self):
        return "<Bike! price: {}, max_speed: {}, miles travailed: {}>".format(self.price, self.max_speed, self.miles)


if __name__ == "__main__":
    bob = Deck()
    print bob


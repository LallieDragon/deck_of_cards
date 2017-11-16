import random

class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def show(self):
		print('{} of {}'.format(self.value, self.suit))
	
class Deck:
	def __init__(self):
		self.cards = []
		self.buildDeck()

	def buildDeck(self):
		for suits in ["Spades", "Diamonds", "Hearts", "Clubs"]:
			for values in range(1,14):
				self.cards.append(Card(suits, values))
				
	def show(self):
		for card in self.cards:
			card.show()

	def shuffle(self):
		random.shuffle(self.cards)
		
	def drawCard(self):
		return self.cards.pop()

class Hand:
	def __init__(self):
		self.hand = []

	def draw(self, deck):
		self.hand.append(deck.drawCard())
		return self 
		
	def showHand(self):
		for card in self.hand:
			card.show()

deck1 = Deck()
deck1.shuffle()
hand = Hand()

hand.draw(deck1).draw(deck1)
for i in range(3):
	hand.draw(deck1)

hand.showHand()
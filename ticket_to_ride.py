from random import shuffle
import csv
# import networkx as nx
import functions as fx

# Tracks
class Track(object):
	def __init__(self, origin, destination, distance, list_of_colours):
		self.origin = origin
		self.destination = destination
		self.distance = distance
		self.colours = list_of_colours
		self.colours_list = list_of_colours.split()
		self.owner = "No one"

	def __str__(self):
		return """
		%s to %s, Distance: %d, Colour(s): %s
		""" % (self.origin, self.destination, self.distance, self.colours)

# Player
class Player (object):
	def __init__(self, name):
		self.name = name
		self.tickets = []
		self.hand = {"Black": 0, "Blue": 0, "Green": 0, "Orange": 0, "Pink": 0, "Red": 0, "White": 0, "Yellow": 0, "Wildcard": 0}
		self.score = 0
		self.trains = 45
		self.cards_in_hand = sum(self.hand.values())
		self.tickets_in_hand = len(self.tickets)
		# self.graph = nx.Graph()
		# for city in cities:
		# 	self.graph.add_node(city)


	def __str__(self):
		return """
		%s
		Score: %d
		Trains Remaining: %d
		Cards in Hand: %d
		Tickets in Hand: %d
		""" % (self.name, self.score, self.trains, self.cards_in_hand, self.tickets_in_hand)
# Tickets
class Ticket(object):
	def __init__(self, origin, destination, points):
		self.origin = origin
		self.destination = destination
		self.points = int(points)
		self.status = "Incomplete"

	def __str__(self):
		return """
		%s to %s
		%d points
		%s
		""" % (self.origin, self.destination, self.points, self.status)

# Ticket Deck
class TicketDeck(object):
	def __init__(self):
		shuffle(tickets)
		self.ticket_deck = tickets
		self.choices = []

	def __str__(self):
		return "The Ticket Deck has %d tickets in it." % len(self.ticket_deck)

	def draw_a_ticket(self):
		return self.ticket_deck.pop()

	def ticket_choice(self, n, player):

		print "\n\n" + player.name

		for i in range(2):
			self.choices.append(self.draw_a_ticket())
		for i in range(len(self.choices)):
			print chr(i) + ". "
			print self.choices[i]
		print "Enter the number ?"
		print "You must select at least %d tickets." % n

		

# Card Deck
class Deck(object):
	def __init__(self):
		track_colours = ["Black", "Blue", "Green", "Orange", "Pink", "Red", "White", "Yellow"]
		self.deck = track_colours * 12
		for i in range(14):
			self.deck.append("Wildcard")
		shuffle(self.deck)

	def __str__(self):
		return "The deck has %d cards in it." % len(self.deck)

	def draw_a_card(self):
		return self.deck.pop()
# Cards on Table


# set up the map

cities = []
routes = []
tickets = []
deck = Deck()

track_reader = csv.reader(open("TTR - tracks.csv"))
track_reader.next()
for row in track_reader:
	routes.append(Track(row[0], row[1], int(row[2]), row[3]))
	cities.append(row[0])
	cities.append(row[1])

cities = set(cities)

ticket_reader = csv.reader(open("TTR - tickets.csv"))
ticket_reader.next()
for row in ticket_reader:
	tickets.append(Ticket(row[0], row[1], row[2]))

ticket_deck = TicketDeck()

print "=-=-=-=-=-=-" * 3 + "="
print ""
print "      Welcome to Ticket to Ride"
print ""
print "=-=-=-=-=-=-" * 3 + "="


# print "How many players?"
# is there an assign function so I can do this better?
player1_name = raw_input("Enter name for Player One: ")
player1 = Player(player1_name)

player2_name = raw_input("Enter name for Player Two: ")
player2 = Player(player2_name)

players = [player1, player2]

for player in players:
	fx.first_draw(player, deck, ticket_deck)


print('\n******')
print "outside"
print player1.hand
print deck
print ticket_deck
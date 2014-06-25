from random import shuffle
import csv

# Cities

# Tracks
class Track(object):
	def __init__(self, origin, destination, distance, list_of_colours):
		self.origin = origin
		self.destination = destination
		self.distance = distance
		self.colours = list_of_colours
		self.colours_list = list_of_colours.split()
		# self.colours = []
		# self.colours_string = ""
		self.owner = "None"
		# for colour in list_of_colours:
		# 	self.colours.append(colour)
		# 	self.colours_string = self.colours_string + colour + " "

	def __str__(self):
		return """
		%s to %s
		Distance: %d
		Colour(s): %s
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
		self.points = points
		self.status = "Incomplete"

	def __str__(self):
		return """
		%s to %s
		%d points
		%s
		""" % (self.origin, self.destination, self.points, self.status)


# Ticket Deck

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

routes = []
route_reader = csv.reader(open("routes.csv"))

route_reader.next()

for row in route_reader:
	routes.append(Track(row[0], row[1], int(row[2]), row[3]))

print routes[0].origin





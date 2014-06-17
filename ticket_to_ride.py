# Classes

# Cities

# Tracks
class Track(object):
	def __init__(self, origin, destination, distance, list_of_colours):
		self.origin = origin
		self.destination = destination
		self.distance = distance
		self.colours = []
		self.colours_string = ""
		for colour in list_of_colours:
			self.colours.append(colour)
			self.colours_string = self.colours_string + colour + " "

	def __str__(self):
		return """
		%s to %s
		Distance: %d
		Colour(s): %s
		""" % (self.origin, self.destination, self.distance, self.colours_string)

# Player
class Player (object):
	def __init__(self, name):
		self.name = name
		self.tickets = []
		self.hand = {"Black": 0, "Blue": 0, "Green": 0, "Orange": 0, "Pink": 0, "Red": 0, "White": 0, "Yellow": 0, "Wildcard": 0}
		self.score = 0
		self.trains = 0
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

	def __str__(self):
		return """
		%s to %s
		%d points
		""" % (self.origin, self.destination, self.points)

# Card

# Ticket Deck

# Card Deck

# Cards on Table



# jude = Player("Jude")
# print jude		

# thing = Ticket("Kansas City", "Houston", 5)
# print thing


a_track = Track("Denver", "Kansas City", 4, ["Black", "Orange"])
print a_track
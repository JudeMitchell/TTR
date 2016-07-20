def turn(player):
	print """
	What would you like to do this turn?
	B - Build a new track
	C - Draw more cards
	T - Draw more tickets
	"""
	action = raw_input("Enter the letter of the action you wish to take. ")
	if action == 'b' or action == "B":
		build(player)
	elif action == 'c' or action == "C":
		draw_cards(player)
	elif action == 't' or action == "T":
		draw_tickets(player)
	else:
		print "Sorry, what was that?"
		turn(player)



def build(player):
	print "Which track would you like to build?"
	print 'Type "back" at any time to chose a different action.'
	possible_tracks = []
	for i in range(len(routes)):
		if route.owner == "No one":
			print i + ". " + routes[i]
			possible_tracks.append(i)
	
	track = routes[raw_input("Enter the track number: ")]

	if track == "back":
		turn(player)
	elif track not in possible_tracks:
		print "You can't build there!"
		build(player)
	
	# confirm sufficient trains
	if player.trains < track.distance:
		print "You don't have enough trains for that!"
		build(player)
	
	# confirm sufficicent cards
	possible_building_colours = []
	for colour in track.colours_list:
		if player.hand[colour] + player.hand['Wildcard'] >= track.distance:
			possible_building_colours.append(colour)
	if len(possible_building_colours) == 0:
		print "You don't have enough train car cards for that!"
		build(player)
	elif len(possible_building_colours) == 1:
		build_colour = possible_building_colours[0]
	else:
		print "Which colour would you like to build in?"
		for colour in possible_building_colours:
			print colour
		build_colour = raw_input("Enter the colour: ").lower()
		if build_colour == 'back':
			turn(player)
		elif build_colour not in possible_building_colours:
			print "Not an option"
			turn(player)


	# add track to map
	player.graph.add_edge(origin, destination)
	# remove cards
	cards_to_remove = track.distance
	 
	# remove train tokens
	player.trains -= track.distance

	# Update track
	track.owner = player.name

	# check number of player trains is > 2
	if player.trains <= 2:
		end_game(player)


def first_draw(player, deck, ticket_deck):
	for i in range(4):
		new_card = deck.draw_a_card()
		player.hand[new_card] += 1
	ticket_deck.ticket_choice(1, player)

		
def end_game(player):
	print "The game is over!!"

	# let everyone else have 1 turn
	# score completed tickets per each player
	# determine who has the longest track
	# compare scores
	# celebrate

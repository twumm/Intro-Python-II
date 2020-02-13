import textwrap
from room import Room
from player import Player
from item import Item

# Declare all the items

sword = Item('sword', 'Cuts through all things')
dagger = Item('dagger', 'Stabs all things')
diamond = Item('diamond', 'Sell for some money')
health = Item('health', 'Restores health')

item_one = [sword, diamond, health]
item_two = [dagger, sword, health]


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", item_one),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", item_two),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", item_one),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", item_two),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", item_two),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_one = Player('Ready Player', 'outside')
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#


def print_room_details(room_label):
    print('Location: ' + room[room_label].name)
    text_to_wrap = textwrap.wrap(room[room_label].description, 40)
    print('Description: ')
    for text in text_to_wrap:
        print(text)


def set_travel_direction(direction):
    direction_selected = f'{direction}_to'
    # checks to see if there is an attribute that matches what is in the method
    if getattr(room[player_one.current_room], direction_selected) != '':
        next_room = getattr(room[player_one.current_room], direction_selected)
        player_one.current_room = list(room.keys())[
            list(room.values()).index(next_room)]  # same Room memory address for the next_room
        print_room_details(player_one.current_room)
    else:
        print(
            f"You can't go in direction {direction}. Try the other 3 options")


for key in room:
    if key == player_one.current_room:
        print_room_details(key)
        for item in room[key].items:
            print(item.name)

    user_input = ''

    while not user_input:
        user_input = input(
            'Where thou moveth to?\n[n] - north\n[s] - south\n[e] - east\n[w] - west\n').split(' ')
        if len(user_input) == 2:
            if user_input[0].lower() in ['get', 'take']:
                for item in room[player_one.current_room].items:
                    if user_input[1].lower() == item.name:
                        player_one.items.append(item)
                        item.on_take()
                        room[player_one.current_room].items.remove(item)
                    else:
                        print(f'{user_input[1]} is not available in location - {player_one.current_room}')
            if user_input[0].lower() in ['drop', 'remove']:
                for item in player_one.items:
                    if user_input[1].lower() == item.name:
                        player_one.items.remove(item)
        elif len(user_input) == 1:
            if user_input[0] in ['i', 'inventory']:
                for item in player_one.items:
                    print(item.name)
            if user_input[0] == 'q':
                quit()
            elif user_input[0] in ['n', 's', 'e', 'w']:
                set_travel_direction(user_input[0])
            else:
                print('Direction not allowed. Press [n], [s], [e] or [w] keys')


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

#
# If the user enters "q", quit the game.


""" Old but working code
# elif player_one.current_room == 'outside' and user_input == 'n':
        #     print_room_details('foyer')
        #     player_one.current_room = 'foyer'
        # elif player_one.current_room == 'foyer' and user_input == 's':
        #     print_room_details('outside')
        #     player_one.current_room = 'outside'
        # elif player_one.current_room == 'foyer' and user_input == 'n':
        #     print_room_details('overlook')
        #     player_one.current_room = 'overlook'
        # elif player_one.current_room == 'foyer' and user_input == 'e':
        #     print_room_details('narrow')
        #     player_one.current_room = 'narrow'
        # elif player_one.current_room == 'overlook' and user_input == 's':
        #     print_room_details('foyer')
        #     player_one.current_room = 'foyer'
        # elif player_one.current_room == 'narrow' and user_input == 'w':
        #     print_room_details('foyer')
        #     player_one.current_room = 'foyer'
        # elif player_one.current_room == 'narrow' and user_input == 'n':
        #     print_room_details('treasure')
        #     player_one.current_room = 'treasure'
        # elif player_one.current_room == 'treasure' and user_input == 's':
        #     print_room_details('narrow')
        #     player_one.current_room = 'narrow'
"""

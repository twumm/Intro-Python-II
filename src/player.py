# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
  # constructor
    def __init__(self, name, current_room, items = []):
        self.name = name
        self.current_room = current_room
        self.items = items

    # def __str__(self):

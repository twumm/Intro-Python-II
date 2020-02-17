# Implement a class to hold room information. This should have name and
# description attributes.
# `name` and `description` attributes.

#   * The room should also have `n_to`, `s_to`, `e_to`, and `w_to` attributes
#     which point to the room in that respective direction.


class Room:
  # constructor
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.n_to = ''
        self.s_to = ''
        self.e_to = ''
        self.w_to = ''
        self.items = items

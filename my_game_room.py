# Specific imports
import my_game_utils

class RoomState(object):
    """Object to abstract out concept of a room's state."""

    def __init__(self):
        self._sid = None
        self._desc = None

    @property
    def sid(self):
        return self._sid

    @sid.setter
    def sid(self, i):
        self._sid = i

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, d):
        self._desc = d

    def __str__(self):
        return str(self.sid)


class RoomStateMapper(object):
    """Class to maintain all configured room states.

    This class, when instantiated, acts like a datastore mapping between a state
    ID and a description of a room.
    """

    def __init__(self):
        self._all_states = {}

    @property
    def all_states(self):
        return self._all_states

    def AddState(self, sid, desc):
        """Add or potentially override an existing room state description.

        Args:
          sid:  Integer room state ID.
          desc:  String description.
        """
        self._all_states[sid] = desc

    def GetState(self, sid):
        """Returns the description of the game state.

        Args:
          sid:  Integer room state ID.
        
        Returns:
          A string description of the room state, None if the ID does not exist
          in the mapping.
        """
        return self._all_states.get(sid, None)


class Room(object):
    """Object to abstract out concept of a room in the game."""
    
    def __init__(self):
        # A state class must implement a __str__ method for debugging.
        self._state = None
        # Contents are kept sorted.
        # Every content class must implement a __str__ method for debugging.
        # Every content class must implement an sort_id method to be able to
        # order these objects.
        self._contents = []
    
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, s):
        self._state = s

    @property
    def contents(self):
        return self._contents

    def AddContent(self, item):
        """Add content to this room.

        Takes ownership of the item.

        Args:
          item:  Name of an item to put into the room.

        Raises:
          Attribute error if sort_id is undefined.
        """
        self._contents.append(item)
        self._contents.sort()

    def RemoveContent(self, content_name):
        # Removing an item from a sorted list should still preserve the sorted
        # order of the list.
        return my_game_utils.RemoveContent(self._contents, content_name)

    def GetContentsDisplay(self):
        """Get the contents of the room to display."""
        return my_game_utils.GetContentsDisplay(self._contents)

    def TryChangeState(self, new_state):
        if new_state == self._state:
            return False
        self._state = new_state
        return True

    def __str__(self):
        return self.state.sid

    def DebugInfo(self):
        """Returns a list of debug info."""
        return ["STATE: %s" % str(self.state),
                "CONTENTS: [%s]" % ", ".join(self.GetContentsDisplay())
               ]

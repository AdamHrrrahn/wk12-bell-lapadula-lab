########################################################################
# COMPONENT:
#    MESSAGE
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of a message
########################################################################

import control

##################################################
# MESSAGE
# One message to be displayed to the user or not
##################################################
class Message:

    # Static variable for the next id
    _id_next = 100

    ##################################################
    # MESSAGE DEFAULT CONSTRUCTOR
    # Set a message to empty
    ##################################################
    def __init__(self):
        self._empty = True
        self._text = "Empty"
        self._author = ""
        self._date = ""
        self._id = Message._id_next
        Message._id_next += 1

    ##################################################
    # MESSAGE NON-DEFAULT CONSTRUCTOR
    # Create a message and fill it
    ##################################################   
    def __init__(self, control_level, text, author, date):
        self.control_level = control_level
        self._text = text
        self._author = author
        self._date = date
        self._id = Message._id_next
        Message._id_next += 1
        self._empty = False

    ##################################################
    # MESSAGE :: GET ID
    # Determine the unique ID of this message
    ##################################################   
    def get_id(self):
        if self._empty:
            return 0
        else:
            return self._id

    ##################################################
    # MESSAGE :: DISPLAY PROPERTIES
    # Display the attributes/properties but not the
    # content of this message
    ##################################################  
    def display_properties(self, subControl):
        if self._empty or  not control.check_read_access(subControl, self.control_level):
            return
        print(f"\t[{self._id}] Message from {self._author} at {self._date}")

    ##################################################
    # MESSAGE :: DISPLAY TEXT
    # Display the contents or the text of the message
    ################################################## 
    def display_text(self, subControl):
        if self._empty or  not control.check_read_access(subControl, self.control_level):
            return False
        print(f"\tMessage: {self._text}")
        return True

    ##################################################
    # MESSAGE :: UPDATE TEXT
    # Update the contents or text of the message
    ################################################## 
    def update_text(self, fun, subControl):
        choice = False
        changing_sec_level = False
        if not control.check_write_access(subControl, self.control_level):
            choice = input("Your security level is higher than the messages. Edditing the message will require an increase in the security level of hte message. Continue? y/n > ").upper() == "Y"
            if choice:
                changing_sec_level = True
            else:
                return
        new_text = fun('message')
        self._text = new_text
        if not changing_sec_level:
            changing_sec_level = input("Change security level of the message? y/n > ").upper() == "Y"
        if changing_sec_level:
            self.control_level = control.get_write_sec_level(subControl)

    ##################################################
    # MESSAGE :: CLEAR
    # Delete the contents of a message and mark it as empty
    ################################################## 
    def clear(self, subControl):
        if (control.check_write_access(subControl, self.control_level)):
            self.control_level = -1
            self._text = "Empty"
            self._author = ""
            self._date = ""
            self._empty = True

########################################################################
# COMPONENT:
#    INTERACT
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class allows one user to interact with the system
########################################################################

import messages, control



###############################################################
# USER
# User has a name and a password
###############################################################
class User:
    def __init__(self, name, password, secLevel):
        self.name = name
        self.password = password
        self.secLevel = secLevel

userlist = [
   [ "AdmiralAbe",     "password", 3],  
   [ "CaptainCharlie", "password", 2], 
   [ "SeamanSam",      "password", 1],
   [ "SeamanSue",      "password", 1],
   [ "SeamanSly",      "password", 1]
]

###############################################################
# USERS
# All the users currently in the system
###############################################################
users = [*map(lambda u: User(*u), userlist)]

ID_INVALID = -1

######################################################
# INTERACT
# One user interacting with the system
######################################################
class Interact:

    ##################################################
    # INTERACT CONSTRUCTOR
    # Authenticate the user and get him/her all set up
    ##################################################
    def __init__(self, username, password, messages):
        self._controlLevel = 0
        self._username = 'Anon'
        # self.control = control.Control()
        self._authenticate(username, password)
        # self._username = username
        self._p_messages = messages

    ##################################################
    # INTERACT :: SHOW
    # Show a single message
    ##################################################
    def show(self):
        id_ = self._prompt_for_id("display")
        if not self._p_messages.show(id_, self._controlLevel):
            print(f"ERROR! Message ID \'{id_}\' does not exist")
        print()

    ##################################################
    # INTERACT :: DISPLAY
    # Display the set of messages
    ################################################## 
    def display(self):
        print("Messages:")
        self._p_messages.display(self._controlLevel)
        print()

    ##################################################
    # INTERACT :: ADD
    # Add a single message
    ################################################## 
    def add(self):
        self._p_messages.add(control.get_write_sec_level(self._controlLevel),
                             self._prompt_for_line("message"),
                             self._username,
                             self._prompt_for_line("date"))

    ##################################################
    # INTERACT :: UPDATE
    # Update a single message
    ################################################## 
    def update(self):
        id_ = self._prompt_for_id("update")
        if not self._p_messages.show(id_, self._controlLevel):
            print(f"ERROR! Message ID \'{id_}\' does not exist\n")
        self._p_messages.update(id_, self._prompt_for_line, self._controlLevel)
        print()
            
    ##################################################
    # INTERACT :: REMOVE
    # Remove one message from the list
    ################################################## 
    def remove(self):
        self._p_messages.remove(self._prompt_for_id("delete"), self._controlLevel)

    ##################################################
    # INTERACT :: PROMPT FOR LINE
    # Prompt for a line of input
    ################################################## 
    def _prompt_for_line(self, verb):
        return input(f"Please provide a {verb}: ")

    ##################################################
    # INTERACT :: PROMPT FOR ID
    # Prompt for a message ID
    ################################################## 
    def _prompt_for_id(self, verb):
        return int(input(f"Select the message ID to {verb}: "))

    ##################################################
    # INTERACT :: AUTHENTICATE
    # Authenticate the user: find their control level
    ################################################## 
    def _authenticate(self, username, password):
        id_ = self._id_from_user(username)
        # return 
        self._username = username
        if ID_INVALID != id_ and password == users[id_].password:
            self._controlLevel = users[id_].secLevel
        else:
            print("Sorry, that username and password combination was not found. Access allowed with public clearance.")
            self._controlLevel = 0

    ##################################################
    # INTERACT :: ID FROM USER
    # Find the ID of a given user
    ################################################## 
    def _id_from_user(self, username):
        for id_user in range(len(users)):
            if username == users[id_user].name:
                return id_user
        return ID_INVALID

#####################################################
# INTERACT :: DISPLAY USERS
# Display the set of users in the system
#####################################################
def display_users():
    for user in users:
        print(f"\t{user.name}")

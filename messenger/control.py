########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################

from secEnum import security

# you may need to put something here...
def check_read_access(sub_sec_level, asset_sec_level):
    return sub_sec_level >= asset_sec_level

def check_write_access(sub_sec_level, asset_sec_level):
    return sub_sec_level <= asset_sec_level

def get_write_sec_level(sub_sec_level):
    options = list(range(sub_sec_level, 4))
    options.reverse()
    print("Select a security level")
    for i in options:
        print(f"\t{i} .. {security(i).name}")
    while(True):
        level = -1
        try:
            level = int(input(">"))
        except ValueError:
            print("Please enter an Integer")
            continue
        if level in options:
            return level
        else:
            print("Invalid security level.")
#hahaha
import json

def openJson(filename="test_user.json") -> dict:
    ## Open json file with file path of <filename>, return dictionary
    file = open(filename, 'r+')
    users = json.load(file)
    file.close()
    return users

def createUser(userID, users):
    ## Creates a new user (if does not exist), return None
    if userID not in users.keys():
        users[userID] = 0
    return None

def changePoints(newPoints, userID, users):
    ## Add or subtract points for the user, return None
    users[userID] += newPoints
    return None

def changeQty(item, market, confirmation):
    ## Add or subtract the item's quantity in the market, return None
    if confirmation == 'Y':
        market[item]["Qty"] += 1
    else:
        market[item]['Qty'] -= 1
    return None

def commitJson(users, filename):
    ## Open json file, dump into json, return None
    """
    users is a dict of user IDs with their associated points

    filename is the filepath for the json file

    return val: None
    """
    file = open(filename, 'r+')
    json.dumps(users, file)
    file.close()
    return None

def getPoints(item, filename="test_market.json") -> int:
    ## Opens market dictionary, checks the appropriate points of the item, 
    # returns the points the item is worth
    ## Dictionary is in the format of { item : {"Qty": X, "Points": Y} }
    file = open(filename, 'r+')
    market = json.load(file)
    file.close()
    points=0
    if item not in market.keys():
        print("New Item! Please contact admin support.")
    else:
        points = market[item]["Points"]
    return points

def main():
    ## Main loop
    # Get user login, check if they exist in the system already
    username = str(input("Enter your username: "))
    users = openJson()
    createUser(username, users)

    # Format the market dictionary to display to the user
    file = open("test_market.json", 'r+')
    market = json.load(file)
    file.close()
    print('===========================================================')
    print('     Material     |      Quantity      |      Points      |')
    for material in market.keys():
        print('     {}     |      {}      |      {}      |'.\
              format(material, market[material]['Qty'], market[material]['Points']) )
    
    # Ask the user if they want to put in or remove, validate input
    confirmation = str(input('Do you wish to put in items or take away items? (Y/N): ')).upper()
    while confirmation != 'Y' and confirmation != 'N':
        print('Invalid input!')
        confirmation = str(input('Do you wish to put in items or take away items? (Y/N): ')).upper()
    item = str(input('Please enter the item you wish to add or remove! (CASE-SENSITIVE): '))
    while item not in market.keys():
        print('Invalid input!')
        item = str(input('Please enter the item you wish to add or remove! (CASE-SENSITIVE): '))
    
    # Get points of the item, update dictionaries accordingly
    points = getPoints(item)
    if confirmation == 'Y':
        changePoints(points, username, users)
    else:
        changePoints(-points, username, users)
    changeQty(item, market, confirmation)
    print('Change applied! Enjoy your new item.')

    # Display new Market dictionary to user.
    print('===========================================================')
    print('     Material     |      Quantity      |      Points      |')
    for material in market.keys():
        print('     {}     |      {}      |      {}      |'.\
              format(material, market[material]['Qty'], market[material]['Points']) )   
    print('Your current points is {}.'.format(users[username]))

main()
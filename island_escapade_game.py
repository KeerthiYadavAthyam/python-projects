print("Welcome to Island Escapade adventure Game!")
print("Row a boat to an Island and retrieve the hidden treasure!")
name=input("Enter your name: ")
print(f"Hello, {name}! Get ready for an exciting adventure.")
print(f"{name}, you started riding a boat now.")
print("Collect the clues to find the treasure but be careful of the dangers")
print("Are you brave enough to start the adventure? (yes/no)")

# Function to open the treasure box
def openbox():
    print("You see a treasure box with a golden lock.")
    print("Use the golden key to open the treasure box. Type 'open' to open the box.")
    action = input("Enter your action: ").strip().lower()
    if action == 'open':
        print("You have successfully opened the treasure box!")
        print("Congratulations! You found the hidden treasure!")
        exit()
    else:
        print("You failed to open the treasure box! Game over.")
        exit()

# Function to find the hidden treasure
def findtreasure():
    print("You need a Golden key to open treasure box.")
    print("Golden key is under the protection of a snake and make a sound 'HISSS' to retrieve it.")
    print("Type 'HISSS' to retrieve the golden key.")
    sound = input("Enter your action: ").strip().upper()
    if sound == 'HISSS':
        print("You have successfully retrieved the golden key!") 
        openbox()
    else:
        print("You failed to retrieve the golden key! Game over.")
        exit()          
            
choice = input("Enter your choice: ").strip().lower()

# Function to escape from monster mermaid and reach the island
def escapemonstermermaid():
    print("You have reached the island safely!")
    print("Now, you need to find the hidden treasure.")
    print("As you explore the island, you encounter a giant sea monster mermaid blocking your path.")
    print("To escape the monster mermaid, you need to satisfy all of its conditions:")
    print("1. Point at the mermaid.")
    print("2. Wait until it reaches 5 meters distance from your boat.")
    print("3. Shoot an arrow in the water to kill it.")
    print("Type 'point', 'wait', and 'shoot' in order to satisfy the conditions.")
    
    conditions = ('point', 'wait', 'shoot')
    satisfied_conditions = []

    while len(satisfied_conditions) < 3:
        action = input("Enter your action: ").strip().lower()
        if action in conditions and action not in satisfied_conditions:
            satisfied_conditions.append(action)
            print(f"You have satisfied the condition: {action}")
        else:
            print("Invalid action or condition already satisfied. Try again.")

    if len(satisfied_conditions) == 3:
        print("You have successfully escaped the monster mermaid!")
        print("Congratulations! You reached the Island!")
        print("Now, you need to find the hidden treasure.")
        findtreasure()

# Function to escape from tides by rowing fast
def escapetides():  
    print("Now, you need to row fast to escape the strong tides.")
    print("Type 'row' five times quickly to escape the tides.")
    
    for i in range(5):
        action = input("Type 'row': ").strip().lower()
        if action != 'row':
            print("You failed to row fast enough! Game over.")
            exit()
        else:
            print(f"You rowed {i+1} times.")
    
    print("You have successfully escaped the strong tides and found the hidden treasure!")
    escapemonstermermaid()

# Function to escape the rocks
def escaperocks():
    print("Now, you see a waterfall ahead. You need to steer your boat carefully to avoid the rocks.")
    print("Steer left or right? (left/right)")
    choice = input("Enter your choice: ").strip().lower()
    if choice == 'left':
        print("You steered left and avoided the rocks! Well done.")
        escapetides()
    elif choice == 'right':
        print("You hit a rock and your boat capsized! Game over.")
        exit()
    else:
        print("Invalid choice. You hesitated and hit a rock! Game over.")
        exit()

#Function to escape the killing knives
def escapekillingknives():
    print("To cross the first danger, you have to bend down thrice and ride your boat to escape from killing knives.")
    bend = input("Bend down now! Type bend: ").strip().lower()
    if bend != 'bend':
        print("You failed to bend down in time! Game over.")
        exit()
    else:
        print("Congrats! You crossed the killing knives.")
        
    escaperocks()

# selecting choice to start the game
if choice.lower() != 'yes':
    print("Maybe next time! Goodbye.")
    exit()
else:
    escapekillingknives()
# Adventure
# Author: Bo Meers
# Date: 24/2/15

gameOver = 0


layout = []
position = 4

for i in range(1,25):
    layout.append(" ")


print("""
                    Welcome to the World of Pythonion! """)

name = input("\nWhat is your name? ")
print("""
                                Hello, """ + name + "!")

print("\nHere is your map: ")

while gameOver != 1:
    layout[position] = "o"
    
    print("""
_____________________________
|                           |
|           [quit]          |
|         ____||____        |""")
    print("|        _|" + layout[0] + layout[1] + layout[2] + layout[3] + layout[4] + layout[5] + layout[6] + layout[7] + "|_       |")
    print("| [store]_ " + layout[8] + layout[9] + layout[10] + layout[11] + layout[12] + layout[13] + layout[14] + layout[15] + " _[home] |")
    print("|         |" + layout[16] + layout[17] + layout[18] + layout[19] + layout[20] + layout[21] + layout[22] + layout[23] + "|        |")
    print("""|         ----||----        |
|         [mountains]       |
|___________________________|""")

    choice = input("Where would you like to go? (W/A/S/D/QUIT) ")
    
    if choice in ("W", "w"):
        layout[position] = " "
        position = position - 8
        
    elif choice in ("S", "s"):
        layout[position] = " "
        position = position + 8
        
    elif choice in ("D", "d"):
        layout[position] = " "
        position = position + 1
        
    elif choice in ("A", "a"):
        layout[position] = " "
        position = position - 1

    elif choice in ("QUIT", "Quit", "quit"):
        print("Have a good day sir.")
        gameOver = 1

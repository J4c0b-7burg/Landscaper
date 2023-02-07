game = {"tool": 0, "money": 0}

tools = [
    {"name": "Teeth", "profit": 1, "cost": 0},
    {"name": "Scissors", "profit": 5, "cost": 5},
    {"name": "Push Lawnmower", "profit": 20, "cost": 100},
    {"name": "Battery-Powered Lawnmower", "profit": 50, "cost": 500},
    {"name": "Magic Sythe", "profit": 100, "cost": 1000}
]

# Functions

def cut_grass():
    # next_tool = tools[game["tool"]+1]
    # if (game["money"] == next_tool["cost"]-1):
    #     print("UPGRADE AVAILABLE!!")

    tool = tools[game["tool"]]
    print(f"YOU CUT SOME GRASS WITH YOUR {tool['name']} AND MADE {tool['profit']}!")
    game["money"] += tool["profit"]
    
def check_bag():
    tool = tools[game["tool"]]
    print(f"YOU CURRENTLY HAVE {game['money']} AND ARE USING A {tool['name']}.")
    
def upgrade():
    if (game["tool"] >= len(tools) - 1):
        print("NO MORE TOOLS FOR YOU.")
        return 0

    next_tool = tools[game["tool"]+1]

    if (next_tool == None):
        print("THERE IS NO MORE UPGRADE.")
        return 0

    if (game["money"] < next_tool["cost"]):
        print("NOT ENOUGH MONEY TO UPGRADE?")
        return 0
    print("YOUR TOOL IS BEING UPGRADED!")
    game["money"] -= next_tool["cost"]
    game["tool"] += 1
    
def win_check():
    if(game["tool"] == 4 and game["money"] >= 5000):
        print("WINNER WINNER CHIKEN DINNER!!!")
        return True
    return False

while (True):
    
    i = input("[1] Cut Grass [2] Check bag [3] Upgrade [0] Quit - ")
    
    i = int(i)
    
    if (i == 1):
        cut_grass()
        
    if (i == 2):
        check_bag()
        
    if (i == 3):
        upgrade()
        
    if (i == 0):
        print("You quit the game")
        break

    if (i == ''):
        print("Error Try Again")
    
    if (win_check()):
        break
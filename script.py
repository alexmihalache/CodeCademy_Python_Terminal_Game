
import random

### TO DO: Find Some interesting ASCII Art to kick off the game
print("Welcome to:")


print("****  17th Century Battle ****")
print("****______________________****")
print("****   LETS PLAY A GAME   ****")
print("****______________________****") 

#Input data for Game

houses = [{
    "Name":"Austria",
    "Territories": ["Austria", "Hungary"],
    "Allies": ["Spain", "Vatican"],
    "Enemies": ["France", "Germany"],
    "User Player": False},
    {
    "Name": "France",
    "Territories":["France"], 
    "Allies": ["Germany"], 
    "Enemies":["Austria", "Spain"],
    "User Player": False}
    ]

battles = [{
    "Name": "Fight for France",
    "Territories in scope": ["France"],
    "Current Owner": "France",
    "Battle Fought": False},

    {
    "Name": "Fight for Hungary",
    "Territories in scope": ["Hungary"],
    "Current Owner": "Austria",
    "Battle Fought": False}]   

class Royal:
    id = 0
    def __init__(self, house_name, territories, allies, enemies, user_player):
        self.house_name = house_name
        self.territories = territories
        self.allies = allies
        self.enemies = enemies
        self.user = user_player
        Royal.id += 1
    
    def __repr__(self):
            return f"{self.house_name}, {self.allies}, {self.enemies}, {self.id}, {self.user}, {self.territories}"
        

class Battles(Royal):
        def __init__(self, name, territory_in_scope, current_owner, battle_fought):
            self.battle_name = name
            self.territory_in_scope = territory_in_scope
            self.current_owner = current_owner
            self.battle_fought = battle_fought #Status to show if the battle has been played/fought yet.

        def __repr__(self):
            return self.battle_name + " " + str(self.territory_in_scope) 
        
        ''' TO DO: Write a method that will remove the territory in scope for the 
                   battle from the owner of the territory if they lose the battle 
                   and add it to the winner
                
        def remove_teritory(self, battle):
            self.territories -= self.territory_in_scope
        '''

'''
def initialise_battles():
    for i in range(len(battles)):
        battles_list.append(Battles(battles[i]["Name"], battles[i]["Territories in scope"], battles[i]["Current Owner"]))
    print("Battles Initialised")

initialise_battles()
'''
def initialise_user_player(name = input("What's your name? ")):
    initial = name[0].lower()
    house_initials = []
    human_player = ""
    
    for i in range(len(houses)):
        house_initials.append(houses[i]["Name"][0].lower())
       
    if initial in house_initials:
        houses[0]["User Player"] = True
        human_player = Royal(house_name=houses[0]["Name"], territories=houses[0]["Territories"], allies=houses[0]["Allies"], enemies=houses[0]["Enemies"], user_player=houses[0]["User Player"])   
        #print(f"First if statement output: {human_player.house_name} & {human_player.user}")            
    else:
        houses[1]["User Player"] = True                
        human_player = Royal(house_name=houses[1]["Name"], territories=houses[1]["Territories"], allies=houses[1]["Allies"], enemies=houses[1]["Enemies"], user_player=houses[1]["User Player"]) 
        #print(f"Second if statement output: {human_player.house_name} & {human_player.user}")     
    
    print("User Player Initialised")
    return human_player
    
"""user_player = initialise_user_player()

print(f"You are playing as: {user_player.house_name}.")
print(user_player.id)"""

player_list = []

def initialise_players():
    user_player = initialise_user_player()
    player_list.append(user_player)

    viable_computer_players = []
    
    for house in houses:
        if house["User Player"] is False:
            viable_computer_players.append(houses.index(house))
        
    computer_player_index = random.choice(viable_computer_players)
    computer_player = Royal(house_name=houses[computer_player_index]["Name"], territories=houses[computer_player_index]["Territories"], allies=houses[computer_player_index]["Allies"], enemies=houses[computer_player_index]["Enemies"], user_player=houses[computer_player_index]["User Player"])
    player_list.append(computer_player)   
    print("Players Initialised")

initialise_players()

print(player_list)








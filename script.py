print("Welcome to:")


print("****  17th Century Battle ****")
print("****______________________****")
print("****   LETS PLAY A GAME   ****")
print("****______________________****") 

houses = [{
    "Name":"Austria",
    "Territories": ["Austria", "Hungary"],
    "Allies": ["Spain", "Vatican"],
    "Enemies": ["France", "Germany"]},
    {
    "Name": "French",
    "Territories":["France"], 
    "Allies": ["Germany"], 
    "Enemies":["Austria", "Spain"]}
    ]

battles = [{
    "Name": "Fight for France",
    "Territories in scope": ["France"],
    "Current Owner": "France"},

    {
    "Name": "Fight for Hungary",
    "Territories in scope": ["Hungary"],
    "Current Owner": "Austria"}]   

player_list = []
battles_list = []

class Royal:
    id = 0
    def __init__(self, house_name, territories, allies, enemies, user):
        self.house_name = house_name
        self.territories = territories
        self.allies = allies
        self.enemies = enemies
        self.user = user
        Royal.id += 1

class Battles(Royal):
        def __init__(self, name, territory_in_scope, current_owner):
            self.battle_name = name
            self.territory_in_scope = territory_in_scope
            self.current_owner = current_owner

        def __repr__(self):
            return self.battle_name + " " + str(self.territory_in_scope) 

        def remove_teritory(self, battle):
            self.territories -= self.territory_in_scope
      
def initialise_players():
    for i in range(len(houses)):
        player_list.append(Royal(houses[i]["Name"], houses[i]["Territories"], houses[i]["Allies"], houses[i]["Enemies"], False))
    print("Players Initialised")

initialise_players()

def initialise_battles():
    for i in range(len(battles)):
        battles_list.append(Battles(battles[i]["Name"], battles[i]["Territories in scope"], battles[i]["Current Owner"]))
    print("Battles Initialised")

initialise_battles()

def initialise_user_player(name = input("What's your name? ")):
    initial = name[0].lower()
    house_initials = []

    for i in range(len(player_list)):
        house_initials.append(player_list[i].house_name[0].lower())
        
    if initial in house_initials:
        player_list[0].user = True            
    else:
        player_list[1].user = True                
    
    print("User Player Initialised")

initialise_user_player()








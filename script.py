from typing import SupportsAbs


print("Welcome to:")


print("****  17th Century Battle ****")
print("****______________________****")
print("****   LETS PLAY A GAME   ****")
print("****______________________****") 

houses = [{
    "Name":"Austrian",
    "Teritories": ["Austria", "Hungary"],
    "Allies": ["Spain", "Vatican"],
    "Enemies": ["France", "Germany"]},
    {
    "Name": "French",
    "Teritories":["France"], 
    "Allies": ["Germany"], 
    "Enemies":["Austria", "Spain"]}
    ]

battles = [{
    "Name": "Fight for France",
    "Teritories in scope": ["France"]},

    {
    "Name": "Fight for Hungary",
    "Teritories in scope": ["Hungary"]}]   

player_list = []
battles_list = []

class Royal:
    id = 0
    def __init__(self, house_name, teritories, allies, enemies, user):
        self.house_name = house_name
        self.teritories = teritories
        self.allies = allies
        self.enemies = enemies
        self.user = user
        Royal.id += 1

class Battles(Royal):
        def __init__(self, name, teritory_in_scope):
            self.battle_name = name
            self.teritory_in_scope = teritory_in_scope

        def __repr__(self):
            return self.battle_name + " " + str(self.teritory_in_scope) 
        
        def remove_teritory(self, player_list):
            for i in range(len(player_list)):
                for key, value in player_list[i].items():
                    if self.teritory_in_scope in self.teritories:
                        print(player_list[i].teritories)
                        try:
                            self.teritories.remove(self.teritory_in_scope)
                            print(player_list[i].teritories)
                        except:
                            return "Teritory not found"
                    
  
def initialise_players():
    for i in range(len(houses)):
        player_list.append(Royal(houses[i]["Name"], houses[i]["Teritories"], houses[i]["Allies"], houses[i]["Enemies"], False))
    
initialise_players()

def initialise_battles():
    for i in range(len(battles)):
        battles_list.append(Battles(battles[i]["Name"], battles[i]["Teritories in scope"]))

initialise_battles()

print(battles_list)

battles_list[0].remove_teritory(player_list)

print(battles_list)

def initialise_user_player(name = input("What's your name? ")):
    initial = name[0].lower()
    
    house_initials = []

    for i in range(len(player_list)):
        house_initials.append(player_list[i].house_name[0].lower())
        
    
    if initial in house_initials:
        
        player_list[0].user = True            
    else:
        
        player_list[1].user = True                

initialise_user_player()








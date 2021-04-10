print("hello world")

print("****______________________****")
print("****   LETS PLAY A GAME   ****")
print("****______________________****")


class Royal:
    def __init__(self, house_name):
        self.house_name = house_name
        print(self.house_name)

new_royal_house = Royal(input("What is your house name?"))
print(new_royal_house.house_name)

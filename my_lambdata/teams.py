# example teams.py (functional approach)

class Team():
    def __init__(self, name, city):
        self.name = name
        self.city = city


def advertise(my_team):
    print(f"HEY COME TO {my_team['city'].upper()} TO SEE OUR GAMES!!!")

def full_name(my_team):
    return f"{my_team['city']} {my_team['name']}"

if __name__ == "__main__":
    # teams = [
    #     {"city": "New York", "name": "Yankees"},
    #     {"city": "New York", "name": "Mets"},
    #     {"city": "Boston", "name": "Red Sox"},
    #     {"city": "New Haven", "name": "Ravens"},
    #     {"city": "Washington", "name": "Nationals"}
    # ]

    # for team in teams:
    #     print("-------")
    #     print(full_name(team))
    #     advertise(team)

    # Instantiating classes similar to below:
    # df1= DataFrame({"x":[1,2,3], "y":[4,5,6]})
    # df1.head()
    # df1.columns
    # df2 = DataFrame({"x":[7,7,7], "y":[4,4,4]})
    # df2.head()

    team = Team(city="Washington", name="Wizards")  # intialize/create an instance
    print(team)
    print(type(team))
    print(team.name)   # invokining attributes
    print(team.city)    # invoking attributes

    
    team2 = Team("Pittsburgh", "Steelers")  # intialize/create an instance
    print(team2)
    print(type(team))
    print(team2.name)   # invokining attributes
    print(team2.city)    # invoking attributes
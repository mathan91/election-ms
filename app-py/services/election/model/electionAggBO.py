'''

This is the model class which will be exposed to UI

'''

class Country(object):

    def __init__(self, country):
        self.country = country

class State(Country):

    def __init__(self, country : str, state : str):
        Country.__init__(self, country)
        self.state = state
        if type(self.state) != dict:
            self.state = dict((state))
        else:
            self.state[len(self.state)] = state

class City(State):

    def __init__(self, country : str, state : str, city : str):
        State.__init__(self, country, state)
        self.city = city
        if type(self.city) != dict:
            self.city = dict((city))
        else:
            self.city[len(self.city)] = city

class Data(City):

    def __init__(self, country : str, state : str, city : str, party : str, seatsWon : int, no_of_seats : int):
        City.__init__(self, country, state, city)
        party = Party(party, seatsWon, no_of_seats)
        self.data = party
        if type(self.data) != list:
            self.data = list((party))
        else:
            self.data[len(self.data)] = party

class Party():
    def __init__(self, party : str, seatsWon : int, no_of_seats : int):
        self.party = party
        self.seatsWon = seatsWon
        self.no_of_seats = no_of_seats

class Horse:
    def __init__(self, name, breed, rider):
        self.name = name
        self.breed = breed
        self.rider = rider
class Rider:
    def __init__(self, name):
        self.name = name

joe = Rider("Joe Mandela")
rick = Horse("Ricky", "Bronco", joe)
print(rick.rider.name)

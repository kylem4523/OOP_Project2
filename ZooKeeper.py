from typing import List, TypeVar

# Code in this section taken from https://refactoring.guru/design-patterns/observer/python/example

# Declaring type variables for observer list
Animal = TypeVar("Animal")
ZooAnnouncer = TypeVar("ZooAnnouncer")


# Zoo Keeper class that handles all of the day to day in the zoo.
class ZooKeeper(object):

    # This is the state variable for all of the Zoo Keepers subscriber;
    state: str = None

    # List of observers who will watch what the Zoo Keeper does.
    observers: List[ZooAnnouncer] = []

    def __init__(self, animals : List[Animal]):
        self.animals = animals
        self.animals_len = len(animals)

    # Function that attaches an observer to our Zoo Keeper
    def attach(self, zoo_announcer: ZooAnnouncer):
        print("Zoo keeper attached an observer")
        self.observers.append(zoo_announcer)

    # Function that decouples an observer from our Zoo Keeper
    def detach(self, zoo_announcer: ZooAnnouncer):
        self.observers.remove(zoo_announcer)

    # Function that notify's all observers of the Zoo Keeper's current state
    def notify(self):
        for zoo_announcer in self.observers:
            zoo_announcer.update(self)

    def get_state(self):
        return self.state

    def get_observers(self):
        return self.observers

    # Function that wakes all the animals in the zoo.
    def wake_animals(self):
        self.state = "Waking the animals"
        self.notify()
        print(self.state)
        for i in range(self.animals_len):
            current_animal = self.animals[i]
            current_name = current_animal.get_name()
            current_type = type(current_animal).__name__
            print(current_name)
            print(current_type)
            current_animal.wake_up()

    # Function that roll calls the animals.
    def roll_call(self):
        self.state = "Calling the animals"
        self.notify()
        for i in range(self.animals_len):
            current_animal = self.animals[i]
            current_name = current_animal.get_name()
            current_type = type(current_animal).__name__
            print(current_name)
            print(current_type)
            current_animal.make_noise_strategy()

    # Function that feeds all the animals.
    def feed_animals(self):
        self.state = "Feeding the animals"
        self.notify()
        for i in range(self.animals_len):
            current_animal = self.animals[i]
            current_name = current_animal.get_name()
            current_type = type(current_animal).__name__
            print(current_name)
            print(current_type)
            current_animal.eat()

    # Function that exercises the animals
    def exercise_animals(self):
        self.state = "Exercising the animals"
        self.notify()
        for i in range(self.animals_len):
            current_animal = self.animals[i]
            current_name = current_animal.get_name()
            current_type = type(current_animal).__name__
            print(current_name)
            print(current_type)
            current_animal.roam_strategy()

    # Function that shuts down the zoo
    def shut_down(self):
        self.state = "Shutting down the zoo"
        self.notify()
        for i in range(self.animals_len):
            current_animal = self.animals[i]
            current_name = current_animal.get_name()
            current_type = type(current_animal).__name__
            print(current_name)
            print(current_type)
            current_animal.sleep()
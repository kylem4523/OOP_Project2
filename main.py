#!/usr/bin/python
import Cat
import Tiger
import Wolf
import Dog
import ZooKeeper
import ZooAnnouncer

if __name__ == '__main__':

    # Instantiating all the animals in the zoo.
    Chesire = Cat.Cat("Chesire")
    Calum = Cat.Cat("Calum")
    Timon = Tiger.Tiger("Timon")
    Tina = Tiger.Tiger("Tina")
    Walace = Wolf.Wolf("Walace")
    Willy = Wolf.Wolf("Willy")
    Diane = Dog.Dog("Diane")
    Dan = Dog.Dog("Dan")

    # Placing all the animals into a list
    animals = [Chesire, Calum, Timon, Tina, Walace, Willy, Diane, Dan]

    # Instantiating the Zoo Announcer, Zoo Keeper, Attaching the Announcer to get updates from
    # the Zoo Keeper, and having the Zoo Keeper go through their daily duties.
    Announcer = ZooAnnouncer.ZooAnnouncer()
    Keeper = ZooKeeper.ZooKeeper(animals)
    Keeper.attach(Announcer)
    Keeper.wake_animals()
    Keeper.roll_call()
    Keeper.feed_animals()
    Keeper.exercise_animals()
    Keeper.shut_down()
    Keeper.detach(Announcer)



import ZooKeeper

# Code in this section taken from https://refactoring.guru/design-patterns/observer/python/example


# This is the concrete observer class of the Zoo Keeper
class ZooAnnouncer(object):
    # Function that checks the zoo keepers state and makes announcements accordingly.
    def update(self, zoo_keeper: ZooKeeper):
        if zoo_keeper.get_state() == "Waking the animals":
            print("Hi, this is the Zoo Announcer.  The Zookeeper is about to wake the animals!")
        elif zoo_keeper.get_state() == "Calling the animals":
            print("Hi, this is the Zoo Announcer.  The Zookeeper is about to call out the animals!")
        elif zoo_keeper.get_state() == "Feeding the animals":
            print("Hi, this is the Zoo Announcer.  The Zookeeper is about to feed the animals!")
        elif zoo_keeper.get_state() == "Exercising the animals":
            print("Hi, this is the Zoo Announcer.  The Zookeeper is about to exercise the animals!")
        elif zoo_keeper.get_state() == "Shutting down the zoo":
            print("Hi, this is the Zoo Announcer.  The Zoo is now closing!")
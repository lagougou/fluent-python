class Bus:

    def __init__(self,passngers=None):
        if passngers is None:
            self.passngers = []
        self.passngers = list(passngers) #传入参数副本，避免可变参数共享和

    def pick(self,name):
        self.passngers.append(name)

    def drop(self,name):
        self.passngers.remove(name)


import copy
bus1 = Bus()
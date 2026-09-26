

# assume - abt control tower for airplane runway - there may be chances of conflicting decisions
# if various instances of same class.

# so singleton design pattern ensure-- only single instance of class



class Controltower:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("initialising control tower")

        return cls._instance

    def _callflight(self,flight):
         return f"hey {flight} onboard now "


tower1 = Controltower()
tower2 = Controltower()

a=tower1._callflight(3400)
print(a)
b=tower2._callflight(2400)
print(b)

print(tower1 is tower2)


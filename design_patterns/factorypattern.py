# class peporini:
#     def prepare(self):
#         return "prepare peporini"


# class cheese:
#     def prepare(self):
#         return "prepare cheese"


# class margeritza:
#     def prepare(self):
#         return "prepare margeritza"

class pizza:
    def prepare(self):
        raise NotImplementedError("extend by child class")

class peproni(pizza):
    def prepare(self):
        return "preparing peproni pizza"

class cornpizza(pizza):
    def prepare(self):
        return "preparing corn pizza"

    
class margeritza(pizza):
    def prepare(self):
        return "margarita is ready"


class pizzafactory:
    @staticmethod

    def create_pizza(pizza_type):
        if pizza_type=="corn":
           return cornpizza()

        elif pizza_type=="margeritza":
            return margeritza()


        else:
             raise ValueError(f"unknown piza {pizza_type}")




def main():

    # pza1 = peporini()
    # pza2 = cheese()
    # pza3 = margeritza()

    # print(pza1.prepare())
    # print(pza2.prepare())
    # print(pza3.prepare())

    # or we can take input from user than if else structure
    # issue
    # -- what if too many classes-- too many if else, 2. if class name changes than we need to modify main class too.abs and 3rd issue is tight coupling.abs

    try:
        user_input="corn"
        pizza=pizzafactory.create_pizza(user_input)
        print(pizza.prepare())

    except ValueError as e:
        print(e)
        







main()
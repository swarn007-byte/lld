class peporini:
    def prepare(self):
        return "prepare peporini"


class cheese:
    def prepare(self):
        return "prepare cheese"


class margeritza:
    def prepare(self):
        return "prepare margeritza"


def main():

    pza1 = peporini()
    pza2 = cheese()
    pza3 = margeritza()

    print(pza1.prepare())
    print(pza2.prepare())
    print(pza3.prepare())



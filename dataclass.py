class Storage:
    def __init__(self, rawdata):
        self.rawlist = rawdata
        self.shelf_height = 5
        self.list = self.datatranslator()
        self.shelf = self.shelf_creator(self.shelf_height)

    def datatranslator(self):
        f = open(self.rawlist, "r").read()
        crates_raw_data = f.split("\n")
        return crates_raw_data

    def shelf_creator(self, height):
        self.shelf_height = height
        biglist = []
        for i in range(height):
            biglist.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
        for test in self.list:
            i = 1
            height = []
            while i < len(test):
                height.append(test[i])
                i += 4
            biglist.append(height)
        self.shelf = biglist
        return biglist

    def addstore(self):
        store = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.shelf.insert(0, store)

    def removestore(self):
        del self.shelf[0]

    def topbox(self, x):
        i = len(self.shelf) - 1
        height = 0
        found = False
        while not found:
            current_crate = self.shelf[i][x]
            if current_crate == " ":
                found = True
            else:
                i -= 1
                height += 1
        return height

    def isspace(self):
        if all(item == " " for item in self.shelf[1]):
            self.removestore()
        if not all(item == " " for item in self.shelf[0]):
            self.addstore()


class MovePlan:
    def __init__(self, rawdata):
        self.rawdata = rawdata
        self.movelist = self.datatranslator()

    def datatranslator(self):
        f = open(self.rawdata, "r").read()
        crates_raw_data = f.split("\n")
        crates_raw_data = self.datacleaner(crates_raw_data)
        return crates_raw_data

    @staticmethod
    def datacleaner(rawlistfunc):
        output = []
        for abc in rawlistfunc:
            abc = abc.split()
            abc.remove("move")
            abc.remove("from")
            abc.remove("to")
            output.append(abc)
        return output

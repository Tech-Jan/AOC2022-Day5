class Crane:
    """big crane. 2models availabe model '9001' and '9000'
    please enter in which storage this crane is working"""

    def __init__(self, storage, model):
        self.model = model
        self.storage = storage
        self.move_box = []

    def movebox(self, amount_boxes, storage_from, storage_to):
        self.move_box = []
        for i in range(amount_boxes):
            self.isspace()
            self.pickup(storage_from)
        for i in range(amount_boxes):
            self.isspace()
            self.drop(storage_to)


    def isspace(self):
        if all(item == " " for item in self.storage.shelf[1]):
            self.storage.removestore()
        if not all(item == " " for item in self.storage.shelf[0]):
            self.storage.addstore()

    def pickup9000(self, storage_from):
        x = storage_from
        y = self.storage.topbox(x)
        self.move_box.append(self.storage.shelf[-y][x])
        self.storage.shelf[-y][x] = " "

    def pickup9001(self, storage_from):
        x = storage_from
        y = self.storage.topbox(x)
        self.move_box.append(self.storage.shelf[-y][x])
        self.storage.shelf[-y][x] = " "

    def pickup(self, storage_from):
        if self.model == "9000":
            self.pickup9000(storage_from)
        if self.model == "9001":
            self.pickup9001(storage_from)


    def drop(self,storage_to):
        if self.model == "9000":
            self.drop9000(storage_to)
        if self.model == "9001":
            self.drop9001(storage_to)

    def drop9000(self,storage_to):
        x = storage_to
        # +1 because you want to drop the box on top of the topbox
        y = self.storage.topbox(x) + 1
        self.storage.shelf[-y][x] = self.move_box[0]
        del self.move_box[0]

    def drop9001(self,storage_to):
        x = storage_to
        # +1 because you want to drop the box on top of the topbox
        y = self.storage.topbox(x) + 1
        self.storage.shelf[-y][x] = self.move_box[-1]
        del self.move_box[-1]





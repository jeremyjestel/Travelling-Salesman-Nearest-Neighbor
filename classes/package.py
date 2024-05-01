class package:
    def __init__(self, pack):
        self.id = pack[0]
        self.address = pack[1]
        self.city = pack[2]
        self.state = pack[3]
        self.zip = pack[4]
        self.deadline = pack[5]
        self.weight = pack[6]
        self.special = pack[7]
        self.status = "At The Hub"
class truck:
    #array to hold package id aka "currently loaded"
    def __init__(self):
        self.current = [None] * 12

    def load(self, id):
        self.current = [None] * len(id)
        for new in id:
            for val in range(len(self.current)):
                if self.current[val] == None:
                    self.current[val] = new
                    break


    def replace(self, id, spot):
        self.current[spot] = id

    def remove(self, id):
        for val in self.current:
            if val == id:
                val = None
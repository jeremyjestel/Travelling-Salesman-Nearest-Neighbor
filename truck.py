class truck:
    #array to hold package id aka "currently loaded"
    current = [None] * 16

    def load(self, id):
        for val in self.current:
            if val == None:
                val = id
                return True
        return False

    def replace(self, id, spot):
        self.current[spot] = id


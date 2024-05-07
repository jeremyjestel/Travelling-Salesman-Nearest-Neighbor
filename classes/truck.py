class truck:
    #array to hold package id aka "currently loaded"
   #initialize packagres loaded on truck to none
    def __init__(self):
        self.current = None
    # add array of packages to currently loaded
    def load(self, id):
        self.current = [None] * len(id)
        for new in id:
            for val in range(len(self.current)):
                if self.current[val] == None:
                    self.current[val] = new
                    break
    #
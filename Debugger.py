class Debug:
    def __init__(self, mode):
        self.active = mode

    def print(self, string):
        if self.active == bool(True):
            print(string)



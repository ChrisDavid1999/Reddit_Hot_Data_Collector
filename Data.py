class StorageData:
    def __init__(self):
        self.Dictionary = {}

    def entry(self, key, title, score):
        title = {'title': title, 'score': score}
        self.Dictionary[key] = title

    def keys(self):
        return self.Dictionary.keys()

    def title(self, key):
        return self.Dictionary[key]["title"]

    def score(self, key):
        return self.Dictionary[key]["score"]
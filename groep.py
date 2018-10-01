class Groep:
    def __init__(self, max=None):
        self.max = max
        self.leden = []

    def is_full(self):
        if self.max is None:
            return False
        return len(self.leden) >= self.max

    def add(self, lid):
        if not self.is_full():
            self.leden.append(lid)
            return True
        return False



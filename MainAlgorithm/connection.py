class Connection:
    def __init__(self, friendship_duration, mutual_friends):
        self.friendship_duration = friendship_duration
        self.mutual_friends = mutual_friends
        self.c = self.connection_value()

    def connection_value(self):
        if self.friendship_duration < 18:
            cfd = self.friendship_duration / 18
        else:
            cfd = 1
        if self.mutual_friends < 24:
            cmf = self.mutual_friends / 24
        else:
            cmf = 1
        return (cfd + cmf)/2
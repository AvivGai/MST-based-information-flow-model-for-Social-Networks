class User:
    def __init__(self, id, name, aua, tf):
        self.id = id
        self.name = name
        self.aua = aua
        self.tf = tf
        self.u = self.user_value()

    def user_value(self):
        if self.tf < 245:
            utf = self.tf / 245
        else:
            utf = 1
        if self.aua < 24:
            uaua = self.aua / 24
        else:
            uaua = 1
        return (utf + uaua)/2




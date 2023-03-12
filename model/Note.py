import datetime


class Note(object):
    def __init__(self, title, msg):
        date = datetime.datetime.today().now().strftime("%d/%m/%Y %I:%M:%S %p")
        self.title = title
        self.msg = msg
        self.date = date

    def __str__(self):
        return self.title + self.msg + self.date

    def __repr__(self):
        return repr((self.title, self.msg, self.date))

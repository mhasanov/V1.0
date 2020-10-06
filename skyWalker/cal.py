
class calendar(object):
    """Calendar representing class"""

    def __init__(self, events = list(), years = list()):
        self.events = events
        self.years = years
        
class event(object):
    """event representing class"""

    def __init__(self, title, date, time, note):
        self.titile = titile
        self.date = date
        self.time = time
        self.note = note

class date(object):
    """date"""
    
    events = list()

    def __init__(self, month, day, year, events):
        self.month = month
        self.day = day
        self.year = year
        self.events = events

class year (object):
    """date"""
    monthdict = []

class month (object):
    """date"""
    
    def __init__(self, number, name):
        self.number = number
        self.name = name

class week (object):
    """date"""
    
    def __init__(self):
        print("not done")

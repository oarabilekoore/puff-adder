# Signal Implementation In Python.

class signal: 
    def __init__(self, default_value = None):
        self._internal_variable = default_value
        self._subscribers = []

    def _notify(self):
        for subscriber in self._subscribers:
            subscriber(self._internal_variable)
    
    def subscribe(self, Fn):
        self._subscribers.append(Fn)
    
    @property
    def value(self):
        return self._internal_variable
    
    @value.setter
    def value(self, new_value):
        self._internal_variable = new_value
        self._notify()


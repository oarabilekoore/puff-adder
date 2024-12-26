# Observer Implementation

class observe:
    def __init__(self, target):
        if not isinstance(target, dict):
            raise AttributeError('The Target Is Not A Dictionary.')
        self._target = target
        self._observers = []

    def observer(self, Fn):
        self._observers.append(Fn)
    
    def __getattr__(self, name):
        if name in self._target:
            return self._target[name]
        raise AttributeError('This property: {name}, is not valid.')

    def __setattr__(self, name, value):
        if name in ['_target', '_observers']:
            super().__setattr__(name, value)
        else:
            self._target[name] = value
            for observer in self._observers:
                observer(name, value)
        

class signal:    
    def __init__(self, default=None):
        self.__subscriptions = set()
        self.__computedDeps = set()
        self.__value = default

    def __notify(self):
        for subscriber in self.__subscriptions:
            subscriber(self.value)
        
        for dep in self.__computedDeps:
            dep.recompute()  
    
    def subscribe(self, fn):
        self.__subscriptions.add(fn)
        return lambda: self.__subscriptions.remove(fn)    
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, new_value):
        if new_value != self.__value:
            self.__value = new_value
            self.__notify()
    
    def computed(self, compute_fn):
        computed_signal = signal(compute_fn(self.__value))
        
        # Define recompute method specifically for this computed signal
        def recompute():
            new_value = compute_fn(self.__value)
            if new_value != computed_signal.value:
                computed_signal.value = new_value
        
        computed_signal.recompute = recompute    
        
        # Add to dependencies
        self.__computedDeps.add(computed_signal)
        return computed_signal
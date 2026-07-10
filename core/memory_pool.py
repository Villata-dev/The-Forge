class ObjectPool:
    def __init__(self, object_class, initial_size: int = 50):
        self.pool = [object_class() for _ in range(initial_size)]
        self.in_use = []

    def acquire(self):
        if self.pool:
            obj = self.pool.pop()
            self.in_use.append(obj)
            return obj
        return None

    def release(self, obj):
        if obj in self.in_use:
            self.in_use.remove(obj)
            self.pool.append(obj)

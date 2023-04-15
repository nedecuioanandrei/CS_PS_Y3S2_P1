class IRepo:
    def __init__(self):
        pass

    def find(self, *args, **kwargs):
        raise NotImplementedError()

    def insert(self, *args, **kwargs):
        raise NotImplementedError()

    def update(self, *args, **kwargs):
        raise NotImplementedError()

    def delete(self, *args, **kwargs):
        raise NotImplementedError()

    def save(self):
        raise NotImplementedError()
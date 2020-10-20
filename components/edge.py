class Edge:

    def __init__(self, start, end, **kwargs):
        self.start = start
        self.end = end
        self.__dict__.update(kwargs)

class Tree:
    def __init__(self, basename, repository, children):
        self.basename = basename
        self.repository = repository
        self.children = children

class Repository:
    def __init__(self, url, kind='normal', meta=[]):
        self.url = url
        self.kind = kind
        self.meta = meta

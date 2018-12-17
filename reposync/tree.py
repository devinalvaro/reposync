class Tree:
    def __init__(self, repository, children):
        self.repository = repository
        self.children = children

    def execute(self, command):
        if self.repository is not None:
            command(self.repository)

        for child in self.children:
            child.execute(command)


class Repository:
    def __init__(self, path, url, kind='git', meta=[]):
        self.path = path
        self.url = url
        self.kind = kind
        self.meta = meta

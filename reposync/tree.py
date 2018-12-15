class Tree:
    def __init__(self, repository, children):
        self.repository = repository
        self.children = children

    def exec(self, command):
        if repository is not None:
            command(repository)

        for child in children:
            child.exec(command)

class Repository:
    def __init__(self, path, url, kind='git', meta=[]):
        self.path = path
        self.url = url
        self.kind = kind
        self.meta = meta

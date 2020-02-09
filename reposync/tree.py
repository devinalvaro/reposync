from threading import Thread


class Tree:
    def __init__(self, repository=None, children=[]):
        self.__repository = repository
        self.__children = children

    def execute(self, command, concurrent=False):
        if self.__repository is not None:
            if concurrent:
                Thread(target=command, args=(self.__repository,)).start()
            else:
                command(self.__repository)

        for child in self.__children:
            child.execute(command, concurrent=concurrent)


class Repository:
    def __init__(self, path, url):
        self.path = path
        self.url = url

import os

from .git import Git
from .parser import Parser


class Reposync:
    def __init__(self, file='repositories.yaml', scheme='https',
                 update=False, verbose=False):
        self.__file = file
        self.__scheme = scheme + '://'
        self.__update = update
        self.__verbose = verbose

        parser = Parser()
        self.__tree = parser.parse(self.__file)

        config = self.__build_config()
        self.__git = Git(config)

    def clone(self):
        self.__tree.execute(self.__git.clone)

    def pull(self):
        self.__tree.execute(self.__git.pull)

    # private

    def __build_config(self):
        return dict(
            gopath=os.getenv('GOPATH'),
            scheme=self.__scheme,
            update=self.__update,
            verbose=self.__verbose)

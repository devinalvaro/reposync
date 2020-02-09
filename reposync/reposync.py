import os

from .git import Git
from .parser import Parser


class Reposync:
    def __init__(
        self,
        file="repositories.yaml",
        method="ssh",
        concurrent=False,
    ):
        self.__file = file
        self.__method = method
        self.__concurrent = concurrent

        self.__git = Git(self.__method)
        self.__tree = Parser().parse(self.__file)

    def clone(self):
        self.__tree.execute(self.__git.clone, concurrent=self.__concurrent)

    def pull(self):
        self.__tree.execute(self.__git.pull, concurrent=self.__concurrent)

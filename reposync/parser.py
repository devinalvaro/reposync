import yaml

from .tree import Repository, Tree


class Parser:
    def parse(self, filename):
        yaml = self.open_yaml(filename)
        return self.build_tree(yaml)

    # private

    def open_yaml(self, filename):
        with open(filename, 'r') as file:
            return yaml.load(file)

    def build_tree(self, node, basenames=[]):
        path = '/'.join(basenames)

        if self.is_normal_repository(node):
            repository = Repository(path, url=node)
            return Tree(repository, children=[])

        if self.is_special_repository(node):
            url = node[1]
            kind = node[0]
            meta = node[2:] if len(node) >= 3 else []
            repository = Repository(path, url, kind, meta)
            return Tree(repository, children=[])

        children = [
            self.build_tree(child, basenames + [basename])
            for basename, child in node.items()
        ]
        return Tree(repository=None, children=children)

    def is_normal_repository(self, node):
        return isinstance(node, str)

    def is_special_repository(self, node):
        return isinstance(node, list)

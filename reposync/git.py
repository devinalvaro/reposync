import os
import subprocess

import git


class Git:
    def __init__(self, config):
        self.gopath = config.get('gopath')
        self.scheme = config.get('scheme')

    def clone(self, repository):
        if repository.kind == 'go':
            self.go_get(repository)
            return

        print("Cloning", repository.path, "...", end="", flush=True)
        try:
            git.Repo.clone_from(self.scheme + repository.url, repository.path)
        except git.exc.GitCommandError:
            print("skipped.")
        else:
            print("cloned.")

    def pull(self, repository):
        if repository.kind == 'go':
            self.go_get(repository)
            return

        print("Pulling", repository.path, "...", end="", flush=True)
        try:
            git.Git(repository.path).pull()
        except git.exc.GitCommandError:
            print("failed.")
        else:
            print("pulled.")

    # private

    def go_get(self, repository):
        print("Getting", repository.path, "...", end="", flush=True)

        if os.path.isdir(repository.path):
            print("skipped.")
            return

        meta = repository.meta
        cmd = meta[0] if len(meta) >= 1 else ''

        get = 'go get -v -u {}/{}'.format(repository.url, cmd)
        subprocess.call(get.split())

        mkdir = 'mkdir -p {}'.format(os.path.dirname(repository.path))
        subprocess.call(mkdir.split())

        ln = 'ln -v -s {}/{} {}'.format(self.gopath + '/src', repository.url,
                                        repository.path)
        subprocess.call(ln.split())

        print("done.")

import os
import subprocess

import git


class Git:
    def __init__(self, config):
        self.gopath = config.get('gopath')
        self.method = config.get('method')
        self.update = config.get('update')
        self.verbose = config.get('verbose')

    def clone(self, repository):
        if repository.kind == 'go':
            self.go_get(repository)
            return

        print("Cloning", repository.path, "...", end="", flush=True)
        try:
            git.Repo.clone_from(self.get_clone_url(repository.url), repository.path)
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

    def get_clone_url(self, repository_url):
        if self.method == 'https':
            return self.convert_to_https_url(repository_url)
        if self.method == 'ssh':
            return self.convert_to_ssh_url(repository_url)

    def convert_to_https_url(self, repository_url):
        return 'https://' + repository_url + '.git'

    def convert_to_ssh_url(self, repository_url):
        url_splits = repository_url.split('/')
        host, path = url_splits[0], '/'.join(url_splits[1:])
        return 'git@' + host + ':' + path + '.git'

    def go_get(self, repository):
        print("Getting", repository.path, "...", end="", flush=True)

        if os.path.isdir(repository.path):
            print("skipped.")
            return

        meta = repository.meta
        cmd = meta[0] if len(meta) >= 1 else ''

        get = 'go get {} {}/{}'.format(self.go_get_flags(), repository.url,
                                       cmd)
        subprocess.call(get.split())

        mkdir = 'mkdir -p {}'.format(os.path.dirname(repository.path))
        subprocess.call(mkdir.split())

        ln = 'ln {} {}/{} {}'.format(self.ln_flags(), self.gopath + '/src',
                                     repository.url, repository.path)
        subprocess.call(ln.split())

        print("done.")

    def go_get_flags(self):
        flags = [self.update_flag(), self.verbose_flag()]
        return ' '.join(flags)

    def ln_flags(self):
        flags = [self.verbose_flag(), '-s']
        return ' '.join(flags)

    def update_flag(self):
        return '-v' if self.update else ''

    def verbose_flag(self):
        return '-v' if self.verbose else ''

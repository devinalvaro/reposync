class VersionControl:
    def __init__(self, config):
        self.gopath = config.get('gopath')
        self.pull = config.get('pull')
        self.scheme = config.get('scheme')


class Git(VersionControl):
    def __init__(self, config):
        super().__init__(config)

    def clone(repository):
        print("Cloning", repository.path, "...", end="", flush=True)

        try:
            git.Repo.clone_from(self.scheme + repository.url, repository.path)
        except git.exc.GitCommandError:
            self.pull(repository.url, repository.path)
        else:
            print("cloned.")

    def pull(repository):
        if not self.pull:
            print("skipped.")
            return

        try:
            git.Git(repository.path).pull()
        except git.exc.GitCommandError:
            print("failed.")
        else:
            print("pulled.")


class Go(VersionControl):
    def __init__(self, config):
        super().__init__(config)

    def get(repository):
        print("Getting", repository.path, "...", end="", flush=True)

        if os.path.isdir(repository.path):
            print("skipped.")
            return

        meta = repository.meta
        cmd = meta[0]

        get = 'go get -v -u {}/{}'.format(repository.url, cmd)
        subprocess.Popen(get.split()).wait()

        command = 'ln -v -s {}/{} {}'.format(GOPATH + '/src', url, path[:-1])
        subprocess.Popen(command.split()).wait()

        print("done.")

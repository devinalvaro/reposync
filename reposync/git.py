import git


class Git:
    def __init__(self, config):
        self.gopath = config.get('gopath')
        self.scheme = config.get('scheme')

    def clone(repository):
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

    def pull(repository):
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

    def go_get(repository):
        print("Getting", repository.path, "...", end="", flush=True)

        if os.path.isdir(repository.path):
            print("skipped.")
            return

        meta = repository.meta
        cmd = meta[0]

        get = 'go get -v -u {}/{}'.format(repository.url, cmd)
        subprocess.Popen(get.split()).wait()

        command = 'ln -v -s {}/{} {}'.format(
            self.gopath + '/src', repository.url, repository.path[:-1])
        subprocess.Popen(command.split()).wait()

        print("done.")

import git


class Git:
    def __init__(self, method):
        self.method = method

    def clone(self, repository):
        print("Cloning", repository.path, "...")
        try:
            git.Repo.clone_from(self.get_clone_url(repository.url), repository.path)
        except git.exc.GitCommandError:
            print("Skipped cloning", repository.path)
        else:
            print("Cloned", repository.path)

    def pull(self, repository):
        print("Pulling", repository.path, "...")
        try:
            git.Git(repository.path).pull()
        except git.exc.GitCommandError:
            print("Failed pulling", repository.path)
        else:
            print("Pulled", repository.path)

    # private

    def get_clone_url(self, repository_url):
        if self.method == "https":
            return self.convert_to_https_url(repository_url)
        if self.method == "ssh":
            return self.convert_to_ssh_url(repository_url)
        raise ValueError("invalid method")

    def convert_to_https_url(self, repository_url):
        return "https://" + repository_url + ".git"

    def convert_to_ssh_url(self, repository_url):
        url_splits = repository_url.split("/")
        host, path = url_splits[0], "/".join(url_splits[1:])
        return "git@" + host + ":" + path + ".git"

# reposync

reposync helps you manage many git repositories. By declaring the repositories in a YAML file, reposync can then apply various git commands (limited to `clone` and `pull` for now) to the repositories in appropriate manners.

## Installation

`$ pip install reposync`

## Usage

Declare repositories in `repositories.yaml` like so:

```
Projects:
  Past:
    alpha: github.com/yourusername/alpha
  Current:
    beta: github.com/yourusername/beta
    omega: github.com/yourusername/omega

Dotfiles: github.com/yourusername/dotfiles

Others:
  TensorFlow: github.com/tensorflow/tensorflow
  Helm: [go, github.com/helm/helm]
```

Then run `$ reposync clone` to clone the repositories, resulting in the directory structure below:

```
.
├── Projects
│   ├── Past
│   │   └── alpha
│   └── Current
│       └── beta
│       └── omega
├── Dotfiles
└── Others
    ├── TensorFlow
    └── Helm
```

To update these repositories, use `$ reposync pull`.

You can specify the YAML file with `--file <filename>.yaml`. For the full options, see `$ reposync -- --help`.

### Go Support

In Go, it is preferred to put repositories at GOPATH. reposync supports this by cloning the Go repositories to their proper path in GOPATH (simulating `go get`), then creates symbolic links to the repositories at the path specified.

To specify a Go repository, you need to put a special list. In the example above, `Helm` is a Go repository and its value is `[go, github.com/helm/helm]`. The first element indicates Go repository, the second is the import path, and the last is the binary location (optional, defaults to the import path).

Internally, reposync will first run `git clone https://github.com/helm/helm $GOPATH/src/github.com/helm/helm` then `ln -s $GOPATH/src/github.com/helm/helm Others/Helm`.

### SSH Support

Reposync supports cloning repositories using ssh, just pass `--method=ssh` (which defaults to `--method=https`). This argument will make reposync automatically use repository URLs' (found in `repositories.yaml`) corresponding ssh URLs.

### Concurrency Support

Reposync supports executing commands concurrently via multithreading by passing `--concurrent`.

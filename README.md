# reposync

reposync helps you organize git repositories. By declaring the repositories in a YAML file, reposync can then apply various git commands (limited to `clone` and `pull` for now) to the repositories in appropriate manners.

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

Contribs
  TensorFlow: github.com/tensorflow/tensorflow
  Rust github.com/rust-lang/rust
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
└── Contribs
    ├── TensorFlow
    └── Rust
```

To update these repositories, use `$ reposync pull`.

You can specify the YAML file with `--file <filename>.yaml`. For the full options, see `$ reposync -- --help`.

# Upsearch

App for finding file in nearest parent folder, very useful in aliases.

## Examples

If you want to run nearest `manage.py`:

```bash
➜ alias manage.py='python $(upsearch manage.py)'
➜ manage.py shell

In [1]:
...
```

Or `setup.py`:

```bash
➜ alias setup.py='python $(upsearch setup.py)'
➜ setup.py --help
Common commands: (see '--help-commands' for more)
```

## Usage

It works not only with python, but with whatever you want, alias should be like:

```bash
alias aliasName='app $(upsearch fileName)'
```

With your own `aliasName` and `app`.

## Installation

App can be easily installed from pip:

```bash
sudo pip install upsearch
```

## Licensed under MIT

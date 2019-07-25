# Git Validator

Git prepare-commit-msg hook, checks if the branch naming is correct as well validates the commit message format

## How to install

Go to the root of your directory and run

```sh
wget https://raw.githubusercontent.com/hemdesignstudio/git_validator/master/install.sh
```

```sh
chmod +x install.sh
```

```sh
 ./install.sh
```

## Or Manual install

clone or download

```sh
cd git_validator
```

### Add to project

```sh
$ cp prepare-commit-msg {path_to_your_project}/.git/hooks
```

```sh
$ chmod +x {path_to_your_project}/.git/hooks/prepare-commit-msg
```

## Formating and linting before commit (Python)

Black config

```sh
$ cp pyproject.toml {path_to_your_project}
```

flake8 config

```sh
$ cp .flake8 {path_to_your_project}
```

Pre-commit config

```sh
$ cp .pre-commit-config.yaml {path_to_your_project}
```

### Installing Pre-commit

```sh
$ pipenv install pre-commit
```

```sh
$ pipenv run pre-commit install
```

### Configure

Use vim or Vscode or any editor your like and go to

    {path_to_your_project}/.git/hooks/

and open "prepare-commit-msg" file

```py
# jira board code, BCD for backend, FRON for Frontend
jira_code = "BCD"

# prefixes
branch_prefixes = ["feature", "bugfix", "test"]

# git default branches
default_branches = ["master", "dev", "staging"]
```

enjoy !

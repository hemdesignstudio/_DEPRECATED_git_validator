# Git Validator

Git prepare-commit-msg hook, checks if the branch naming is correct as well validates the commit message format

## How to install

clone or download

```sh
cd git_validator
```

### configure

```py
jira_code = "BCD"

# prefixes
branch_prefixes = ["feature", "bugfix", "test"]

# git default branches
default_branches = ["master", "dev", "staging"]
```

add to project

```sh
$ mv prepare-commit-msg {path_to_your_project}/.git/hooks
```

enjoy !

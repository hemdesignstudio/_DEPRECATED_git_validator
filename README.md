# Git Validator

Git prepare-commit-msg hook, checks if the branch naming is correct as well validates the commit message format

## How to install

clone or download

```sh
cd git_validator
```

### Configure

Use vim or Vscode or any editor your like

and open "prepare-commit-msg" file

```py
jira_code = "BCD"

# prefixes
branch_prefixes = ["feature", "bugfix", "test"]

# git default branches
default_branches = ["master", "dev", "staging"]
```

### Add to project

```sh
$ mv prepare-commit-msg {path_to_your_project}/.git/hooks
```

```sh
$ chmod +x {path_to_your_project}/.git/hooks/prepare-commit-msg
```

enjoy !

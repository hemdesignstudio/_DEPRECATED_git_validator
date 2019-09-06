# Git Validator

Git prepare-commit-msg hook, checks if the branch naming is correct as well validates the commit message format

## Dependencies

    git
    pipenv

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

### Configure

Use vim or Vscode or any editor your like and go to
and open ".git-validator-config.json" file and change accordingly

```
{
  "jira_code": "BCD",
  "default_branches": ["master", "dev", "test"],
  "branch_prefixes": ["feature", "bugfix", "test"]
}
```

## Branch name format

```
    prefix/JIRA-No/branch-name
    e.g.
        feature/BCD-192/install-script-enhancement
        bugfix/BCD-195/prepare-msg-commit-fix
```

enjoy !

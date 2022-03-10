# Sort Python Imports plugin for Sublime Text 4

Simple plugin to run `isort` on the current Python file.

# Usage

Open the Command Pallete and run "Sort Python Imports".

If the current view has a file path, it will be passed to isort to [find a configuration file](https://pycqa.github.io/isort/docs/configuration/config_files.html), if one exists.

# TODO

- Configuration via ST settings if isort config file is not found.
- Actually require ST4 since it won't run on earlier versions due to Python 3.8 requirement.

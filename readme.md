# Sort Python Imports plugin for Sublime Text 4

Simple plugin to run `isort` on the current Python file. Uses my preferred `isort` configuration for now.

# Usage

Open the Command Pallete and run "Sort Python Imports".

# TODO

- Configuration via ST settings
- Actually require ST4 since it won't run on earlier versions due to Python 3.8 requirement.
- Handle isort configuration from user files (see [CONFIG_SOURCES in settings.py](./_vendor/isort/settings.py)).

import os
import sublime
import sublime_plugin
import sys


isort_config: dict = {}


class SortPythonImportsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Only run on python files.
        syntax = self.view.syntax()
        if syntax is not None and syntax.name == 'Python':
            setup_vendored_lib_path()
            import isort

            region = sublime.Region(0, self.view.size())
            content = self.view.substr(region)

            output = isort.code(content, **isort_config)

            self.view.replace(
                edit,
                region,
                output
            )

        else:
            sublime.error_message('Not a Python file.')


def setup_vendored_lib_path():
    plugin_dir = os.path.abspath(os.path.dirname(__file__))
    vendor_dir = os.path.join(plugin_dir, '_vendor')
    sys.path.append(vendor_dir)


def plugin_loaded():
    # plugin_settings = sublime.load_settings(SETTINGS_FILE)

    global isort_config
    isort_config = {
        'no_sections': True,
        'lines_after_imports': 2,
        'lines_between_types': 0,
        'include_trailing_comma': True,
        'force_alphabetical_sort': True,
        'multi_line_output': 5,
    }

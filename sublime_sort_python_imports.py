import os
import sys
from pathlib import Path

import sublime
import sublime_plugin


isort_config_overrides: dict = {}


class SortPythonImportsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Only run on python files.
        syntax = self.view.syntax()
        if syntax is None or syntax.name != 'Python':
            sublime.error_message('Not a Python file.')
            return

        setup_vendored_lib_path()
        import isort
        clear_isort_caches()

        region = sublime.Region(0, self.view.size())
        content = self.view.substr(region)

        file_path = self.view.file_name()
        if file_path and len(file_path) > 0:
            # If the view has a file path, get the directory containing it so
            # that isort's logic for finding configuration will operate from there.
            file_path = Path(file_path).resolve()
            if file_path.is_file():
                file_path = file_path.parent
        else:
            file_path = None

        print(f'file_path={file_path}')
        output = isort.code(
            content,
            file_path=file_path,
            **isort_config_overrides
        )

        if content != output:
            self.view.replace(
                edit,
                region,
                output
            )


def setup_vendored_lib_path():
    plugin_dir = os.path.abspath(os.path.dirname(__file__))
    vendor_dir = os.path.join(plugin_dir, '_vendor')
    sys.path.append(vendor_dir)


def clear_isort_caches():
    """ isort uses functools.lru_cache on the functions that load settings from file.
        We want to re-read the file any time the plugin is run in case it has been changed,
        but I haven't found a way to force that other than importing these functions
        and clearing the cache.
    """

    from isort.settings import _find_config, _get_config_data, find_all_configs
    for fn in (_find_config, find_all_configs, _get_config_data):
        fn.cache_clear()


def plugin_loaded():
    # plugin_settings = sublime.load_settings(SETTINGS_FILE)

    global isort_config_overrides
    isort_config_overrides = {
        # 'include_trailing_comma': True,
        # 'lines_after_imports': 2,
        # 'lines_between_sections': 1,
        # 'lines_between_types': 0,
        # 'multi_line_output': 3,
        # 'no_sections': False,
    }

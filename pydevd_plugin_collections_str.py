from _pydevd_bundle.pydevd_extension_api import StrPresentationProvider
from .pydevd_helpers import find_mod_attr


class SizedShapeStr:

    def can_provide(self, type_object, type_name):
        type_list = [list, tuple, dict, set]
        for type in type_list:
            if isinstance(type_object, type):
                return True
        return False

    def get_str(self, val):
        return f'len: {len(val)}, value: {val}'


import sys

if not sys.platform.startswith("java"):
    StrPresentationProvider.register(SizedShapeStr)

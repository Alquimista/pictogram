#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import partial
import os

try:
    import plugin as plug
except ImportError:
    from . import plugin as plug

from wand.display import display
from wand.image import Image


ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
DEFAULT_XDG_DATA = os.path.join(os.path.expanduser("~"), ".local/share")
XDG_DATA_HOME = os.environ.get("XDG_DATA_HOME", DEFAULT_XDG_DATA)

PLUGIN_PATHS = [
    os.path.join(ROOT_PATH, "filters"),
    os.path.join(XDG_DATA_HOME, "pictogram", "filters")
]


class Photo(object):

    """docstring for Photo"""

    def __init__(self, im=None):
        super(Photo, self).__init__()
        self._im = im
        if not hasattr(self._im, 'gaussian_blur'):
            self._im = Image(filename=self._im)
        self.__plugins = plug.Plugin(PLUGIN_PATHS)
        self._filters = {}

        for plugin_name in self.__plugins.list_plugins():
            plugin = self.__plugins.load_plugin(plugin_name)
            try:
                plugin.setup(self)
            except AttributeError:
                continue

        for name, func in self._filters.items():
            setattr(self.__class__, name, func)

        self.width = self._im.width
        self.height = self._im.height
        self.size = self.width, self.height

    def list_filters(self):
        return list(self._filters.keys())

    def register_filter(self, name, func):
        """A function a plugin can use to register a image filter."""
        self._filters[name] = func

    # def filter(self, name, *args, **kwargs):
    #     return self._filters[name](self, *args, **kwargs)

    def _photo(self):
        return Photo(self._im)

    def copy(self):
        return Photo(self._im.clone())

    def show(self):
        return display(image=self._im)

    def save(self, filename, *args, **kwargs):
        try:
            show = kwargs.pop("show")
            self._im.save(filename=filename, *args, **kwargs)
            if show:
                self.show()
        except KeyError:
            self._im.save(filename=filename, *args, **kwargs)


def main():
    im = Photo("../tests/lena512color.tiff")
    frame = im.copy()

    print(im.size)
    print(im.width, im.height)
    # im.filter("blur", strength=0.5)
    im.show()
    im.save(filename="../tests/lena512color.png")

    print(im.list_filters())

    frame.blur(strength=0.5)
    frame.bord("#000", 20).flop()
    print(frame.size)
    frame.save(filename="../tests/lena512color_blur.png", show=True)


if __name__ == '__main__':
    main()

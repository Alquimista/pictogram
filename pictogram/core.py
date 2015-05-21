#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os

try:
    import plugin as plug
    from image import Image
except ImportError:
    from . import plugin as plug
    from .image import Image

from wand.display import display


ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
# Filters with the same name in .local/share/pictogram overrides the
# internal ones
DEFAULT_XDG_DATA = os.path.join(os.path.expanduser("~"), ".local/share")
XDG_DATA_HOME = os.environ.get("XDG_DATA_HOME", DEFAULT_XDG_DATA)

PLUGIN_PATHS = [
    os.path.join(ROOT_PATH, "filters"),
    os.path.join(XDG_DATA_HOME, "pictogram", "filters")
]


class Photo(object):

    """docstring for Photo"""

    def __init__(self, im=None):
        self._im = self._new(im)
        self._filters = set()

        self._load_plugins()

    def _load_plugins(self):
        # Register Plugins/Filters
        plugins = plug.Plugin(PLUGIN_PATHS)
        for name in plugins.plugins:
            plugin = plugins.load_plugin(name)
            try:
                plugin.setup(self)
            except AttributeError:
                continue

    def _new(self, im):
        # im = filename or im = Image class
        if not hasattr(im, "gaussian_blur"):
            return Image(filename=im)
        else:
            return Image(image=im)

    @property
    def width(self):
        return self._im.width

    @property
    def height(self):
        return self._im.height

    @property
    def size(self):
        return self.width, self.height

    @property
    def filters(self):
        return tuple(self._filters)

    def register_filter(self, name, func):
        """A function a plugin can use to register a image filter."""
        self._filters.add(name)
        setattr(self.__class__, name, func)

    def copy(self):
        return Photo(self._im)

    def show(self):
        return display(image=self._im)

    def save(self, filename, *args, **kwargs):
        try:
            show = kwargs.pop("show")
        except KeyError:
            show = False
        self._im.strip()
        self._im.save(filename=filename, *args, **kwargs)
        if show:
            self.show()


def main():
    im = Photo("../tests/lena512color.tiff")
    frame = im.copy()

    # im filters
    print(im.filters)

    # im
    im.save(filename="../tests/lena512color.png")

    # frame
    frame.blur(0.5).sepia(.85).vintage().lomo().frame("kelvin")
    frame.save(filename="../tests/lena512color_lomo.png", show=True)

    # frame2
    frame2 = frame.copy()
    frame2.bord(15)
    frame2.show()


if __name__ == "__main__":
    main()

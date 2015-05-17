#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

try:
    import plugin as plug
    from image import Image
except ImportError:
    from . import plugin as plug
    from .image import Image

from wand.display import display


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
        self._new(im)
        self.__plugins = plug.Plugin(PLUGIN_PATHS)
        self._filters = {}

        for plugin_name in self.__plugins.plugins:
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

    def _new(self, im):
        if not hasattr(im, 'gaussian_blur'):
            self._im = Image(filename=im)
        else:
            self._im = im

    @property
    def filters(self):
        return list(self._filters.keys())

    def register_filter(self, name, func):
        """A function a plugin can use to register a image filter."""
        self._filters[name] = func

    def _photo(self):
        return Photo(self._im)

    def copy(self):
        return Photo(self._im.clone())

    def show(self):
        return display(image=self._im)

    def save(self, filename, *args, **kwargs):
        self._im.strip()
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

    # im
    im.save(filename="../tests/lena512color.png")

    # frame
    frame.sepia(0.85).mask("radial").frame("kelvin")
    frame.save(filename="../tests/lena512color_lomo.png", show=True)


if __name__ == '__main__':
    main()

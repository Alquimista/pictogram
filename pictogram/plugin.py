#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import imp
import os
import sys


def makedirs(path, exist_ok=False):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == os.errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


if float('.'.join(map(str, sys.version_info[:2]))) >= 3.2:
    makedirs = os.makedirs


class Plugin(object):

    """docstring for Plugin"""

    def __init__(self, searchpath):
        super(Plugin, self).__init__()
        self.searchpath = searchpath
        self.__plugins = {}
        self.__load_plugins()

    def __load_plugins(self):
        for path in self.searchpath:
            makedirs(path, exist_ok=True)
            for plugin in glob.glob(path + "/*.py"):
                if plugin.endswith("__init__.py"):
                    continue
                basename = os.path.basename(plugin)
                basename_without_extension = os.path.splitext(basename)[0]
                self.__plugins[basename_without_extension] = plugin

    def load_plugin(self, name):
        return imp.load_source(name, self.__plugins[name])

    @property
    def plugins(self):
        return list(self.__plugins.keys())

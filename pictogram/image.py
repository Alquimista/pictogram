#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wand.image import Image as WandImage
from wand.image import CHANNELS
from wand.api import library
from ctypes import c_void_p, c_double, c_int

# Define C-API method signatures
library.MagickLevelImage.argtypes = [c_void_p,  # wand
                                     c_double,  # black_point
                                     c_double,  # gamma
                                     c_double]  # white_point
library.MagickLevelImageChannel.argtypes = [c_void_p,  # wand
                                            c_int,  # channelType (Enumeration)
                                            c_double,  # black_point
                                            c_double,  # gamma
                                            c_double]  # white_point
library.MagickLevelImage.restype = c_int
library.MagickLevelImageChannel.restype = c_int

library.MagickSepiaToneImage.argtypes = [c_void_p, c_double]
library.MagickSepiaToneImage.restype = None


class Pixel(object):

    def __init__(self, red=0, green=0, blue=0):
        self.red = red
        self.green = green
        self.blue = blue
        self.rgb = self.red, self.green, self.blue
        self.hex = "{0.red:02X}{0.green:02X}{0.blue:02X}".format(self)

    def __getitem__(self, index):
        return self.rgb[index]

    def __setitem__(self, index, value):
        self.rgb[index] = value

    def __len__(self):
        return 3

    def __iter__(self):
        return iter(self.rgb)

    def __str__(self):
        return "[" + ", ".join(map(str, self.rgb)) + "]"

    def __repr__(self):
        return "<{} {}, {}, {}>".format(self.__class__.__name__, *self.rgb)


class Image(WandImage):

    @property
    def pixels(self):
        pixels = []
        self.depth = 8
        blob = self.make_blob(format='RGB')
        for cursor in range(0, self.width * self.height * 3, 3):
            pixel = Pixel(red=blob[cursor],
                          green=blob[cursor + 1],
                          blue=blob[cursor + 2])
            pixels.append(pixel)
        return pixels

    def level(self, black, white=None, gamma=1.0, channel=None):
        # Assert black, gamma, & white are float types
        # between 0.0 & 1.0.
        # Both black & white values must be converted to
        # QuantumRange percentages.
        if not white:
            white = 1 - black
        bp = float(self.quantum_range * black)
        wp = float(self.quantum_range * white)
        if channel:
            try:
                ch_const = CHANNELS[channel]
            except KeyError:
                raise ValueError(repr(channel) + ' is an invalid channel type'
                                 '; see wand.image.CHANNELS dictionary')
            r = library.MagickLevelImageChannel(
                self.wand, ch_const, bp, gamma, wp)
        else:
            r = library.MagickLevelImage(self.wand, bp, gamma, wp)
        if not r:
            self.raise_exception()

    def sepia(self, threshold):
        quantum = float(self.quantum_range)
        return library.MagickSepiaToneImage(self.wand, threshold * quantum)

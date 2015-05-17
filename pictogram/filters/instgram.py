#!/usr/bin/env python
# -*- coding: utf-8 -*-

# AUTHOR: Roberto Gea (Alquimista) <robertogea@openmailbox.org>
# VERSION: 0.1.0
# WEB: https://bitbucket.com/alquimista/pictogram
import os
import sys
try:
    from pictogram.filters import default
    from pictogram import PImage
except ImportError:
    sys.path.insert(0, os.path.abspath(".."))
    from pictogram.filters import default
    from pictogram import Image


ROOTPATH = os.path.abspath(os.path.dirname(__file__))


def lens_flare(p):
    bg = Image(filename=os.path.join(ROOTPATH, "img/lensflare.png"))
    bg.transform(resize="{:d}x".format(p._im.width))
    p._im.composite_channel(
        channel="all_channels",
        image=bg,
        operator="screen")
    return p._photo()


def mask(p, name, operator="multiply"):
    bg = Image(filename=os.path.join(ROOTPATH, "img/{}.png".format(name)))
    bg.resize(*p._im.size)
    p._im.composite_channel(
        channel="all_channels",
        image=bg,
        operator="multiply")
    return p._photo()


def black_and_white(p):
    bg = Image(filename=os.path.join(ROOTPATH, "img/bwgrad.png"))
    bg.resize(*p._im.size)
    p._im.type = 'grayscale'
    p._im.composite_channel(
        channel="all_channels",
        image=bg,
        operator="soft_light")
    return p._photo()


def frame(p, name):
    f = Image(filename=os.path.join(ROOTPATH, "img/{}.png".format(name)))
    f.resize(*p._im.size)
    p._im.composite_channel(
        channel="all_channels",
        image=f,
        operator="over")
    return p._photo()


# Fix lomo and sepia


def lomo(p):
    # only for level, sepia and pixel custom functions
    p._im = Image(image=p._im.clone())
    p._im.level(channel="red", black=0.33)
    p._im.level(channel="green", black=0.33)
    return p._photo()


def sepia(p, threshold):
    p._im = Image(image=p._im.clone())
    p._im.sepia(threshold)
    return p._photo()


def setup(app):
    app.register_filter("black_and_white", black_and_white)
    app.register_filter("lens_flare", lens_flare)
    app.register_filter("lomo", lomo)
    app.register_filter("frame", frame)
    app.register_filter("sepia", sepia)
    app.register_filter("mask", mask)

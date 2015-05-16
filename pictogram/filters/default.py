#!/usr/bin/env python
# -*- coding: utf-8 -*-

# AUTHOR: Roberto Gea (Alquimista) <robertogea@openmailbox.org>
# VERSION: 0.1.0
# WEB: https://bitbucket.com/alquimista/pictogram
from wand.color import Color


def blur(photo, strength):
    photo._im.gaussian_blur(0, strength)
    return photo._photo()


def crop(photo, left, top, right, bottom):
    photo._im.crop(left, top, right, bottom)
    return photo._photo()


def flip(photo):
    photo._im.flip()
    return photo._photo()


def flop(photo):
    photo._im.flop()
    return photo._photo()


def resize(photo, width, height):
    photo._im.resize(width, height)
    return photo._photo()


def liquid_resize(photo, width, height):
    photo._im.liquid_resize(width, height)
    return photo._photo()


def bord(photo, color='black', width=20):
    photo = resize(photo, photo.width - width * 2, photo.height - width * 2)
    photo._im.border(Color(color), width, width)
    return photo._photo()


def modulate(photo, brightness, saturation, hue):
    return photo._photo()


def setup(app):
    app.register_filter("blur", blur)
    app.register_filter("bord", bord)
    app.register_filter("resize", resize)
    app.register_filter("liquid_resize", liquid_resize)
    app.register_filter("crop", crop)
    app.register_filter("flip", flip)
    app.register_filter("flop", flop)

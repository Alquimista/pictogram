#!/usr/bin/env python
# -*- coding: utf-8 -*-

# AUTHOR: Roberto Gea (Alquimista) <robertogea@openmailbox.org>
# VERSION: 0.1.0
# WEB: https://bitbucket.com/alquimista/pictogram
from wand.color import Color


def blur(p, strength=None):
    if not strength:
        strength = min(p.size) / 300
    p._im.gaussian_blur(strength, strength)
    return p


def crop(p, left, top, right, bottom):
    p._im.crop(left, top, right, bottom)
    return p


def flip(p):
    p._im.flip()
    return p


def flop(p):
    p._im.flop()
    return p


def resize(p, width, height):
    p._im.resize(width, height)
    return p


def liquid_resize(p, width, height):
    p._im.liquid_rescale(width, height)
    return p


def bord(p, size=15, color='black'):
    p._im.resize(p._im.width - size * 2, p._im.height - size * 2)
    p._im.border(Color(color), size, size)
    return p


def grayscale(p):
    p._im.type = 'grayscale'
    return p


def rotate(p, degree=90, background=None):
    original_size = p._im.size
    p._im.rotate(degree=degree, background=background)
    p._im.resize(*original_size)
    return p


def composite(p, img, left=None, top=None):
    p._im.composite_channel(
        channel="all_channels", image=bg, operator="over", left=left, top=top)
    return p


def opacity(p, value):
    p._im.transparentize(value)
    return p


def level(p, black, white=None, gamma=1.0, channel=None):
    p._im = Image(image=p._im.clone())
    p._im.level(black, white, gamma, channel)
    return p


def negate(p, grayscale=False, channel=None):
    p._im.negate(grayscale=False, channel=None)
    return p


def setup(app):
    app.register_filter("blur", blur)
    app.register_filter("bord", bord)
    app.register_filter("resize", resize)
    app.register_filter("liquid_resize", liquid_resize)
    app.register_filter("crop", crop)
    app.register_filter("flop", flop)
    app.register_filter("flip", flip)
    app.register_filter("grayscale", grayscale)
    app.register_filter("greyscale", grayscale)
    app.register_filter("rotate", rotate)
    app.register_filter("composite", rotate)
    app.register_filter("negate", negate)
    app.register_filter("opacity", opacity)
    app.register_filter("level", level)

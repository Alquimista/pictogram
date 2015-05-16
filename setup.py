#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

with open("requirements.txt") as f:
    req = f.readlines()

APP_NAME, APP_VERSION = "pictogram", "0.1.0"

requirements = []
for r in requirements:
    if not r.startswith("Wand"):
        continue
    requirements.append(r)

setup(
    name=APP_NAME,
    version=APP_VERSION,
    description="Photo Filters",
    long_description=readme,
    author="Roberto Gea",
    author_email="robertogea@openmailbox.org",
    url="https://bitbucket.com/alquimista/pictogram",
    download_url="https://bitbucket.org/alquimista/pictogram/downloads",
    license=license,
    packages=['pictogram'],
    install_requires=requirements,
    # scripts=["bin/pictogram"],
    # entry_points = {
    #       'console_scripts': [
    #           'command-name = package.module:main_func_name',
    #       ],
    #   },
    classifiers=[
        "Development Status :: 1",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
    keywords="photo instagram picture pictogram image filter",
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os
import re
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return codecs.open(os.path.join(here, *parts), "r").read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


long_description = read("README.md") + "\n" + read("CHANGES.md")


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ["--strict", "--verbose", "--tb=long", "tests"]
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name="pictogram",
    version=find_version("pictogram", "__init__.py"),
    description="Photo Filters",
    long_description=long_description,
    author="Roberto Gea",
    author_email="robertogea@openmailbox.org",
    url="https://bitbucket.com/alquimista/pictogram",
    download_url="https://bitbucket.org/alquimista/pictogram/downloads",
    license=license,
    packages=["pictogram"],
    include_package_data=True,
    zip_safe=False,
    cmdclass={"test": PyTest},
    test_suite="tests",
    tests_require=["pytest"],
    install_requires="Wand",
    entry_points={
        'console_scripts': [
            'pictogram = pictogram.__main__:main'
        ]
    },
    package_data={"pictogram": ["filters/img/*"]},
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
    extras_require={"testing": ["pytest"]},
    keywords="photo instagram picture pictogram image filter",
)

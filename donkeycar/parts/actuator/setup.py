#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['donkey_actuator'],
    package_dir={'': 'src'},
    scripts=['bin/actuator_node']
)

setup(**d)
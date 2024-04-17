#!/usr/bin/env python
IS_CATKIN = False

try:
    from catkin_pkg.python_setup import generate_distutils_setup
    import selectors
    from setuptools import setup, find_packages
    IS_CATKIN = True
except ImportError:
    from setuptools import setup, find_packages
    pass

VERSION = '1.0.0'

setup_args = dict(
    name='hyperion-graph-vis',
    packages=find_packages(),

    version=VERSION,
    install_requires=[
        'graphviz',
    ],

    description='Graph visualisation extension for the Hyperion Launch Engine',
    author='David Leins',
    author_email='dleins@techfak.uni-bielefeld.de',
    url='https://github.com/DavidPL1/hyperion-start/hyperion-user-interfaces.git',
    keywords=['hyperion'],
    classifiers=[],
    entry_points={
            'hyperion.visualisation': [
                'graph_gen = hyperion_graph_visualisation.graph_generator'
            ]
    },
    include_package_data=True,
    zip_safe=False
)

if IS_CATKIN:
    setup_args = generate_distutils_setup(
        **setup_args
    )

setup(**setup_args)

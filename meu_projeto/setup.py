from setuptools import setup, find_packages

import funcoes

setup(
    name = 'nes_functions',
    version =  '0.1',
    description = 'Functions developed on NES POO course',
    install_requires = ['numpy', 'pandas'],
    packages = find_packages()
)
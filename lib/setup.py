from setuptools import find_packages, setup

setup(name='common', version='1.0', packages=find_packages(
    include=['common', 'common.*']))

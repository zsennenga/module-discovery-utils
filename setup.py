from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='module-discovery-utils',
    version='1.0.1',
    packages=['module_discovery_utils'],
    url='https://github.com/zsennenga/module-discovery-utils',
    license='Apache License 2.0',
    author='Zach Ennenga',
    author_email='astrozees@gmail.com',
    description='A simple library to allow easy package/module level introspection',
    long_description=long_description,
    long_description_content_type='text/markdown',
)

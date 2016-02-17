#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup,find_packages

# For Testing:
#
# python3.4 setup.py register -r https://testpypi.python.org/pypi
# python3.4 setup.py bdist_wheel upload -r https://testpypi.python.org/pypi
# python3.4 -m pip install -i https://testpypi.python.org/pypi
#
# For Realz:
#
# python3.4 setup.py register
# python3.4 setup.py bdist_wheel upload
# python3.4 -m pip install

setup(
    name='vicious',
    version='0.0.1',
    description='Vicious Python',
    author='Invisigoth Kenshoto',
    author_email='invisigoth.kenshoto@gmail.com',
    url='https://github.com/vivisect/vicious',
    license='Apache License 2.0',

    packages=find_packages(exclude=['*.tests','*.tests.*']),

    install_requires=[
    ],

    classifiers=[
        'Development Status :: 4 - Alpha',
        'License :: OSI Approved :: Apache Software License',
    ],

)

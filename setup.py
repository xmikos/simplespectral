#!/usr/bin/env python

from setuptools import setup

setup(
    name="SimpleSpectral",
    version="1.0.0",
    description="Heavily simplified scipy.signal.spectral module which only depends on NumPy and supports pyFFTW",
    long_description=open('README.rst').read(),
    author="Michal Krenek (Mikos)",
    author_email="m.krenek@gmail.com",
    url="https://github.com/xmikos/simplespectral",
    license="MIT",
    py_modules=["simplespectral"],
    install_requires=[
        'numpy',
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering"
    ]
)

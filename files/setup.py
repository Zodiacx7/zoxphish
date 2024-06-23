#!/usr/bin/env python

from setuptools import setup

version = open("files/version.txt").read().strip()
long_description = open("README.md").read().strip()

setup(
    name='zoxphish',
    version=version,
    description='A python phishing script for login phishing, image phishing video phishing an many more!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Zodiac',
    author_email='Zodiacxhacker@gmail.com',
    license="MIT",
    url='https://github.com/Zodiacx7/zoxphish.git',
    scripts=['Zoxphish'],
    install_requires=["requests", "rich"]
)

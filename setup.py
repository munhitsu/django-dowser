import os
from setuptools import setup

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

VERSION = '0.1.8'

setup(
    name="django-dowser",
    version=VERSION,

    author="Mateusz Lapsa-Malawski",
    author_email="m@cr3.io",

    description="Django fork of amazing memory leaks tracking application for python wsgi - the Dowser",
    long_description=open("README.rst").read(),
    long_description_content_type='text/x-rst',

    url="http://github.com/munhitsu/django-dowser",

    keywords=["django", "dowser", "debug", "memory leak"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Debuggers",
        "License :: OSI Approved :: MIT License",
    ],
    packages=['django_dowser'],
    include_package_data=True,
    zip_safe=False,  # because we're including media that Django needs
)

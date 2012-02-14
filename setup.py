import os
from setuptools import setup, find_packages

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

setup(
	name="django-dowser",
	version='0.1',

	author="Mateusz Łapsa-Malawski",
	author_email="mateusz@munhitsu.com",
	url="http://munhitsu.com",

	description="Django fork of amazing memory leaks tracking application for python wsgi - the Dowser",
	long_description=open("README.markdown").read(),
	keywords=["django","dowser"],
	classifiers=[
			"Programming Language :: Python",
			"Programming Language :: Python :: 2.7",
			"Intended Audience :: Developers",
			"Natural Language :: English",
			"Operating System :: OS Independent",
			"Environment :: Other Environment",
			"Topic :: Utilities",
			"Topic :: Software Development :: Libraries",
		],
        packages = find_packages(),
        include_package_data=True,
        zip_safe=False, # because we're including media that Django needs
)

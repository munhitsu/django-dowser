import os
from setuptools import setup, find_packages

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

setup(
	name="django-dowser",
	version='0.1.1',

	author="Mateusz Lapsa-Malawski",
	author_email="mateusz@munhitsu.com",
	url="http://github.com/munhitsu/django-dowser",

	description="Django fork of amazing memory leaks tracking application for python wsgi - the Dowser",
	long_description=open("README.markdown").read(),
	keywords=["django","dowser", "debug", "memory leak"],
	license = open("LICENSE").read(),
	download_url="https://nodeload.github.com/munhitsu/django-dowser/tarball/master",
	platforms="",
	classifiers=[
			"Programming Language :: Python",
			"Programming Language :: Python :: 2.7",
			"Intended Audience :: Developers",
			"Natural Language :: English",
			"Operating System :: OS Independent",
			"Environment :: Other Environment",
			"Topic :: Utilities",
			"Topic :: Software Development :: Libraries",
			"License :: OSI Approved :: BSD License",
		],
        packages = find_packages(),
        include_package_data=True,
        zip_safe=False, # because we're including media that Django needs
)

import os
from setuptools import setup, find_packages

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

VERSION = '0.1.3'

setup(
	name="django-dowser",
	version=VERSION,

	author="Mateusz Lapsa-Malawski",
	author_email="mateusz@munhitsu.com",
	url="http://github.com/munhitsu/django-dowser",

	description="Django fork of amazing memory leaks tracking application for python wsgi - the Dowser",
	long_description=open("README.markdown").read(),
	keywords=["django","dowser", "debug", "memory leak"],
	license = open("LICENSE").read(),
	download_url="http://pypi.python.org/packages/source/d/django-dowser/django-dowser-%s.tar.gz" % VERSION,
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
        packages = ['django_dowser'],
        package_data = {
                        'django_dowser': ['templates/django_dowser/*.html','templates/django_dowser/*.css'],
                },
        include_package_data = True,
        zip_safe = False, # because we're including media that Django needs
)

import setuptools, sys

setuptools.setup(
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
    },
	packages=['django_dowser'],
)

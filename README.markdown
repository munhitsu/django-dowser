About
=====
Based on: [Dowser](http://www.aminus.net/wiki/Dowser)

Original dowser was wsgi enabled. Unfortunatelly not all django hosting solutions provide wsgi. 
In daily development the most common usage pattern is ./manage.py runserver which defenetly is not wsgi.
That's the story why this fork was created.

In other words the target of this project is to provide easy to use and install django app to debug your memory leaks.

Following enhancements have been implemented on top of original dowser:

- long term analysis, 1m, 1h, 1d, 4w buffers
- optimization by moving from lists to python deque
- server load optimization by moving charts to google chart
- only authenticated superuser can view analysis (django specific)


![Screen shot](https://github.com/munhitsu/django-dowser/raw/master/wiki/screen0.png)



Installation
============
	pip install git+git://github.com/munhitsu/django-dowser.git

Than modify project configuration to add the app:

settings.py
-----------
	INSTALLED_APPS = (
	#...
	    'django_dowser',
	#...
	)

urls.py
-------
	urlpatterns += patterns('',
	    (r'^dowser/', include('django_dowser.urls')),
	)


Example buildout recipe
-----------------------
	[django-dowser]
	location = django-dowser
	recipe = zerokspot.recipe.git
	repository = https://github.com/munhitsu/django-dowser

Note
----
Use django-dowser only on multithreaded servers. In case forking occurs than
each fork will have it's own dowser storage.

Usage
-----
Start the project and open link:

	http://domain:port/dowser/

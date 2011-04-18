Installation
============

Check it out and add to PYTHONPATH.
Than modify project configuration.


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

Note
----
Use django-dowser only on multithreaded servers. In case forking occurs than
each fork will have it's own dowser storage.


Usage
-----
start the app and open link:
http://domain:port/dowser/

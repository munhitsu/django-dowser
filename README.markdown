About
=====
Based on: [dowser](http://www.aminus.net/wiki/Dowser)

Ported as an easy to install django app to debug your memory leaks.

Following extensions has been made:

- long term analysis, 1m, 1h, 1d, 4w buffers
- optimization by moving from lists to python deque
- server load optimization by moving charts to google chart
- django specific - only authenticated superuser can view analysis


![Screen shot](https://github.com/munhitsu/django-dowser/raw/master/wiki/screen0.png)



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

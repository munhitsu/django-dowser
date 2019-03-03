About
=====

Based on: `Dowser <http://www.aminus.net/wiki/Dowser>`__

A Django specific Dowser port.

Following enhancements have been implemented on top of the original Dowser:

-  long term historical analysis: 1m, 1h, 1d, 4w buffers
-  optimization by moving from lists to python deque
-  server load optimization by moving charts to google chart
-  only superuser can view the analysis (Django specific)

.. figure:: https://github.com/munhitsu/django-dowser/raw/master/wiki/screen0.png
   :alt: Screen shot

   Screen shot

Future
======
- move charts to javascript
- move inline html to templates
- drop Django 1.x and Python 2.x compatibility

Installation
============

::

    # latest release
    pip install django-dowser
    # or latest master
    pip install git+git://github.com/munhitsu/django-dowser.git

Next, modify project configuration.

settings.py
-----------

::

    INSTALLED_APPS += ['django_dowser']

urls.py
-------

::

    from django.urls import path, include
    urlpatterns += [url(r'^dowser/', include('django_dowser.urls'))]


Note
----

Use django-dowser only on multithreaded/gevent servers. With forking, or multiple servers, each process
will have it's own Dowser storage, so you will only get a glimpse into one process and further requests may be load
balanced to the other servers.


Usage
-----

Start the project and open link:

::

    http://domain/dowser/

When running in the local development mode, it is usually:

::

    http://127.0.0.1:8000/dowser/

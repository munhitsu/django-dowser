About
=====

Based on: `Dowser <http://www.aminus.net/wiki/Dowser>`__

The original Dowser is WSGI enabled. Unfortunately, not all Django
hosting providers use WSGI. In daily development the most common usage
pattern is ./manage.py runserver which is not using WSGI. That's the
story why this fork was created.

In the other words the target of this project is to provide easy to use
and install Django app to debug your memory leaks.

Following enhancements have been implemented on top of original Dowser:

-  long term analysis, 1m, 1h, 1d, 4w buffers
-  optimization by moving from lists to python deque
-  server load optimization by moving charts to google chart
-  only authenticated superuser can view analysis (Django specific)

.. figure:: https://github.com/munhitsu/django-dowser/raw/master/wiki/screen0.png
   :alt: Screen shot

   Screen shot

Installation
============

::

    # latest release
    pip install django-dowser
    # or latest master
    pip install git+git://github.com/munhitsu/django-dowser.git

Next, modify project configuration to add the app:

settings.py
-----------

::

    INSTALLED_APPS = (
    #...
        'django_dowser',
    #...
    )

urls.py
-------

::

    urlpatterns += [url(r'^dowser2/', include('django_dowser.urls'))]

Example buildout recipe
-----------------------

::

    [django-dowser]
    location = django-dowser
    recipe = zerokspot.recipe.git
    repository = https://github.com/munhitsu/django-dowser

Note
----

Use django-dowser only on multithreaded servers. With forking, each fork
will have it's own Dowser storage.

Usage
-----

Start the project and open link:

::

    http://domain:port/dowser/

With development server, this is typically

::

    http://localhost:8000/dowser/

About
=====

Based on: `Dowser <http://www.aminus.net/wiki/Dowser>`__

A Django specific Dowser port.

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

    urlpatterns += [url(r'^dowser/', include('django_dowser.urls'))]

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

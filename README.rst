==========================
django-codenerix-corporate
==========================

Codenerix Corporate is a module that enables `CODENERIX <https://www.codenerix.com/>`_ to manage corporate/enterprise data on several platforms in a general manner. Model for managing business's information

.. image:: https://github.com/codenerix/django-codenerix/raw/master/codenerix/static/codenerix/img/codenerix.png
    :target: https://www.codenerix.com
    :alt: Try our demo with Codenerix Cloud

*********
Changelog
*********

2018-01-17 - Codenerix Corporate v1.x is incompatible with v2.x, `what has changed and how to migrate to v2.x? <https://github.com/codenerix/django-codenerix-corporate/wiki/Codenerix-Corporate-version-1.x-is-icompatible-with-2.x>`_.

****
Demo
****

You can have a look to our `demo online <http://demo.codenerix.com>`_.

You can find some working examples in GITHUB at `django-codenerix-examples <https://github.com/codenerix/django-codenerix-examples>`_ project.

**********
Quickstart
**********

1. Install this package::

    For python 2: sudo pip2 install django-codenerix-corporate
    For python 3: sudo pip3 install django-codenerix-corporate

2. Add "codenerix_corporate" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'codenerix_corporate',
    ]

3. Add the param in setting:
	# list of languages available for the translation of the content of the models
	LANGUAGES_DATABASES = ['ES', 'EN']

4. Since Codenerix Corporate is a library, you only need to import its parts into your project and use them.

*************
Documentation
*************

Coming soon... do you help us?

You can get in touch with us `here <https://codenerix.com/contact/>`_.

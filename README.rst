============
fullqualname
============

Fully qualified names for Python objects.

Install
=======

.. code::

    $ pip install git+git://github.com/etgalloway/fullqualname#egg=fullqualname

Use
===

.. code::

    In [1]: from fullqualname import fullqualname

    In [2]: import datetime

    In [3]: obj = datetime.timedelta.days

    In [4]: fullqualname(obj)
    Out[4]: 'datetime.timedelta.days'

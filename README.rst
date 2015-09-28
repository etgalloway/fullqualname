============
fullqualname
============

The `fully qualified name` of an object in Python is the full dotted "path"
to its definition.

`fullqualname` provides fully qualified names for a variety of types in Python
2 and 3.

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

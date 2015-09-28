"""Fully qualified names for Python objects.
"""
import inspect
import sys

__version__ = '0.1.0'


def fullqualname_py3(obj):
    """Fully qualified name for objects in Python 3."""

    if type(obj).__name__ == 'builtin_function_or_method':

        return _fullqualname_builtin_py3(obj)

    elif type(obj).__name__ == 'function':

        return _fullqualname_function_py3(obj)

    elif type(obj).__name__ in ['member_descriptor', 'method_descriptor',
                                'wrapper_descriptor']:

        return obj.__objclass__.__module__ + '.' + obj.__qualname__

    elif type(obj).__name__ == 'method':

        return _fullqualname_method_py3(obj)

    elif type(obj).__name__ == 'method-wrapper':

        return fullqualname_py3(obj.__self__) + '.' + obj.__name__

    elif type(obj).__name__ == 'module':

        return obj.__name__

    elif type(obj).__name__ == 'property':

        return obj.fget.__module__ + '.' + obj.fget.__qualname__

    elif inspect.isclass(obj):

        return obj.__module__ + '.' + obj.__qualname__

    return obj.__class__.__module__ + '.' + obj.__class__.__qualname__


def _fullqualname_builtin_py3(obj):
    """Fully qualified name for 'builtin_function_or_method' objects in
    Python 3.
    """

    if obj.__module__ is not None:
        # built-in functions
        module = obj.__module__
    else:
        # built-in methods
        if inspect.isclass(obj.__self__):
            module = obj.__self__.__module__
        else:
            module = obj.__self__.__class__.__module__

    return module + '.' + obj.__qualname__


def _fullqualname_function_py3(obj):
    """Fully qualified name for 'function' objects in Python 3.
    """

    if hasattr(obj, "__wrapped__"):
        # Required for decorator.__version__ <= 4.0.0.
        qualname = obj.__wrapped__.__qualname__
    else:
        qualname = obj.__qualname__

    return obj.__module__ + '.' + qualname


def _fullqualname_method_py3(obj):
    """Fully qualified name for 'method' objects in Python 3.
    """

    if inspect.isclass(obj.__self__):
        cls = obj.__self__.__qualname__
    else:
        cls = obj.__self__.__class__.__qualname__

    return obj.__self__.__module__ + '.' + cls + '.' + obj.__name__


def fullqualname_py2(obj):
    """Fully qualified name for objects in Python 2."""

    if type(obj).__name__ == 'builtin_function_or_method':

        return _fullqualname_builtin_py2(obj)

    elif type(obj).__name__ == 'function':

        return obj.__module__ + '.' + obj.__name__

    elif type(obj).__name__ in ['member_descriptor', 'method_descriptor',
                                'wrapper_descriptor']:

        return (obj.__objclass__.__module__ + '.' +
                obj.__objclass__.__name__ + '.' +
                obj.__name__)

    elif type(obj).__name__ == 'instancemethod':

        return _fullqualname_method_py2(obj)

    elif type(obj).__name__ == 'method-wrapper':

        return fullqualname_py2(obj.__self__) + '.' + obj.__name__

    elif type(obj).__name__ == 'module':

        return obj.__name__

    elif inspect.isclass(obj):

        return obj.__module__ + '.' + obj.__name__

    return obj.__class__.__module__ + '.' + obj.__class__.__name__


def _fullqualname_builtin_py2(obj):
    """Fully qualified name for 'builtin_function_or_method' objects
    in Python 2.
    """

    if obj.__self__ is None:
        # built-in functions
        module = obj.__module__
        qualname = obj.__name__
    else:
        # built-in methods
        if inspect.isclass(obj.__self__):
            cls = obj.__self__
        else:
            cls = obj.__self__.__class__
        module = cls.__module__
        qualname = cls.__name__ + '.' + obj.__name__

    return module + '.' + qualname


def _fullqualname_method_py2(obj):
    """Fully qualified name for 'instancemethod' objects in Python 2.
    """

    if obj.__self__ is None:
        # unbound methods
        module = obj.im_class.__module__
        cls = obj.im_class.__name__
    else:
        # bound methods
        if inspect.isclass(obj.__self__):
            # methods decorated with @classmethod
            module = obj.__self__.__module__
            cls = obj.__self__.__name__
        else:
            module = obj.__self__.__class__.__module__
            cls = obj.__self__.__class__.__name__

    return module + '.' + cls + '.' + obj.__func__.__name__


if sys.version_info >= (3,):
    fullqualname = fullqualname_py3
else:
    fullqualname = fullqualname_py2

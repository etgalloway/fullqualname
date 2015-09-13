"""Tests for fullqualname."""

import datetime
import decorator
import inspect
import nose
import sys

from fullqualname import fullqualname


def decorator_(f_):
    def wrapper_(f_, *args, **kw):
        return f_(*args, **kw)
    return decorator.decorator(wrapper_, f_)


class C_(object):
    @decorator_
    def decorated_method_(self):
        """decorated method"""


def test_builtin_function():
    # Test built-in function object.

    obj = len

    # Type is 'builtin_function_or_method'.
    assert type(obj).__name__ == 'builtin_function_or_method'

    # Object is a function.
    assert 'built-in function' in repr(obj)

    if sys.version_info >= (3, ):
        expected = 'builtins.len'
    else:
        expected = '__builtin__.len'

    nose.tools.assert_equals(fullqualname(obj), expected)


def test_builtin_method():
    # Test built-in method object.

    obj = [1, 2, 3].append

    # Object type is 'builtin_function_or_method'.
    assert type(obj).__name__ == 'builtin_function_or_method'

    # Object is a method.
    assert 'built-in method' in repr(obj)

    # Object __self__ attribute is not a class.
    assert not inspect.isclass(obj.__self__)

    if sys.version_info >= (3, ):
        expected = 'builtins.list.append'
    else:
        expected = '__builtin__.list.append'

    nose.tools.assert_equals(fullqualname(obj), expected)


def test_builtin_classmethod():
    # Test built-in class method object.

    obj = object.mro

    # Object type is 'builtin_function_or_method'.
    assert type(obj).__name__ == 'builtin_function_or_method'

    # Object is a method.
    assert 'built-in method' in repr(obj)

    # Object __self__ attribute is a class.
    assert inspect.isclass(obj.__self__)

    if sys.version_info >= (3, ):
        expected = 'builtins.object.mro'
    else:
        expected = '__builtin__.object.mro'

    nose.tools.assert_equals(fullqualname(obj), expected)


def func_():
    """function"""


def test_function():
    # Test function object.

    obj = func_

    assert type(obj).__name__ == 'function'

    expected = __name__ + '.func_'

    nose.tools.assert_equals(fullqualname(obj), expected)


def test_function_wrapped_attribute():
    # Test function object that has a __wrapped__ attribute.

    obj = C_.decorated_method_

    assert hasattr(obj, '__wrapped__')

    # In Python 3, object type is 'function'.
    assert type(obj).__name__ == 'function' or sys.version_info[0] == 2

    # In Python 2, object is an 'instancemethod'.
    assert type(obj).__name__ == 'instancemethod' or sys.version_info[0] == 3

    expected = __name__ + '.C_.decorated_method_'

    nose.tools.assert_equals(fullqualname(obj), expected)


def test_member_descriptor():
    # Test member descriptor object.

    obj = datetime.timedelta.days

    assert type(obj).__name__ == 'member_descriptor'

    expected = 'datetime.timedelta.days'

    nose.tools.assert_equals(fullqualname(obj), expected)


def test_method_descriptor():
    # Test method descriptor object.

    obj = str.split

    assert type(obj).__name__ == 'method_descriptor'

    if sys.version_info >= (3, ):
        expected = 'builtins.str.split'
    else:
        expected = '__builtin__.str.split'

    nose.tools.assert_equals(fullqualname(obj), expected)


def test_wrapper_descriptor():
    # Test wrapper descriptor object.

    obj = int.__add__

    assert type(obj).__name__ == 'wrapper_descriptor'

    if sys.version_info >= (3, ):
        expected = 'builtins.int.__add__'
    else:
        expected = '__builtin__.int.__add__'

    nose.tools.assert_equals(fullqualname(obj), expected)


def test_module():
    # Test module object.

    obj = sys
    assert type(obj).__name__ == 'module'

    expected = 'sys'
    nose.tools.assert_equals(fullqualname(obj), expected)

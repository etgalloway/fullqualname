"""Tests for fullqualname."""

import inspect
import nose
import sys

from fullqualname import fullqualname


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

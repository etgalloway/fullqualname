"""Tests for fullqualname."""

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

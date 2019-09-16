==========
multistack
==========
Example of multiple stacks in one array.

Usage::

    >>> s = MultiStack(4, 4)
    >>> s.push(stack=1, value=35)
    >>> s.push(1, 10)
    >>> s.push(0, 2)
    >>> s.push(2, -33)
    >>> s.peek(stack=1)
    10
    >>> s.pop(stack=2)
    -33
    >>> print(s)
    [None, None, None, 2, None, None, 10, 35, None, None, None, None, None, None, None, None]



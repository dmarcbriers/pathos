#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 1997-2016 California Institute of Technology.
# License: 3-clause BSD.  The full license text is available at:
#  - http://trac.mystic.cacr.caltech.edu/project/pathos/browser/pathos/LICENSE

from dill import source
def test_source(obj):
    _obj = source._wrap(obj)
    assert _obj(1.57) == obj(1.57)
    src = source.getimportable(obj, alias='_f')
    exec(src, globals())
    assert _f(1.57) == obj(1.57)
    name = source.getname(obj)
    assert name == obj.__name__ or src.split("=",1)[0].strip()

def test_ppmap(obj):
    from pathos.pools import ParallelPool
    p = ParallelPool(2)
    x = [1,2,3]
    assert list(map(obj, x)) == p.map(obj, x)


if __name__ == '__main__':

    from math import sin
    f = lambda x:x+1
    def g(x):
        return x+2

    for func in [g, f, abs, sin]:
        test_source(func)
        test_ppmap(func)

# EOF

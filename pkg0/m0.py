"""
Basic classes, methods, functions
"""

import os

class Class0(object):
    """Class0 docstring"""
    var0 = 0
    def meth0(self): pass

class Class1(object):
    def __init__(self):
        self.var0 = 0
        self.var0 = []
        self.var1 = None

    def meth0(self):
        var0 = Class0()
        self.var1 = var0

class Class0_0(Class0):
    def __init__(self, arg0, arg1, *args, **kwargs):
        super(Class0_0, self).meth0()

def f0():
    var0 = Class0()
    var1 = Class1()
    var2 = Class0_0(1, 2)
    return (var0, var1, var2)

# variable "defined" in 2 places
x = 1
if True:
    x = 2

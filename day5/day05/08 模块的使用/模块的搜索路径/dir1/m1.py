# from dir1 import m2
from . import m2
def f1():
    print('m1.f1')
    m2.f2()
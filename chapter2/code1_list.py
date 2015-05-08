__author__ = 'Administrator'


def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]

def test4():

    l = list(range(1000))


from timeit import Timer

t1 = Timer("test1()", "from __main__ import test1")
print("concat ", t1.timeit(number=1000), "milliseconds")

t2 = Timer("test2()", "from __main__ import test2")
print("concat ", t2.timeit(number=1000), "milliseconds")

t3 = Timer("test3()", "from __main__ import test3")
print("concat ", t3.timeit(number=1000), "milliseconds")

t4 = Timer("test4()", "from __main__ import test4")
print("concat ", t4.timeit(number=1000), "milliseconds")

print("\n")


x = list(range(200000))
pop_zero = Timer("x.pop(0)", "from __main__ import x")
print("concat ", pop_zero.timeit(number=1000), "milliseconds")

y = list(range(200000))
pop_end = Timer("y.pop()", "from __main__ import y")
print("concat ", pop_end.timeit(number=1000), "milliseconds")


l = [1, 2, 3, 4, 5]
print(l.pop())
print(l.pop())
print(l.pop())
print(l.pop())
print(l.pop())
print(l)
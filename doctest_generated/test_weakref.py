
try:
    import weakref
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class Dict(dict):
        pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    obj = Dict(red=1, green=2, blue=3)   # this object is weak referencable
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    r = weakref.ref(obj)
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 7')
    print(print(r() is obj)
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    import weakref
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class Object:
        pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    o = Object()
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    r = weakref.ref(o)
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    o2 = r()
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 17')
    print(o is o2
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    del o, o2
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 21')
    print(print(r())
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    import weakref
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    class ExtendedRef(weakref.ref):
        def __init__(self, ob, callback=None, **annotations):
            super().__init__(ob, callback)
            self.__counter = 0
            for k, v in annotations.items():
                setattr(self, k, v)
        def __call__(self):
            '''Return a pair containing the referent and the number of
            times the reference has been called.
            '''
            ob = super().__call__()
            if ob is not None:
                self.__counter += 1
                ob = (ob, self.__counter)
            return ob
    class A:   # not in docs from here, just testing the ExtendedRef
        pass
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    a = A()
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    r = ExtendedRef(a, foo=1, bar="baz")
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 45')
    print(r.foo
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 48')
    print(r.bar
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 51')
    print(r()[1]
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 54')
    print(r()[1]
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 57')
    print(r()[0] is a
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    import weakref
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    _id2obj_dict = weakref.WeakValueDictionary()
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    def remember(obj):
        oid = id(obj)
        _id2obj_dict[oid] = obj
        return oid
    def id2obj(oid):
        return _id2obj_dict[oid]
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    a = A()             # from here, just testing
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    a_id = remember(a)
except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    print('Line 72')
    print(id2obj(a_id) is a
    )

except Exception as __e:
    print("Occurred", type(__e), __e)


try:
    del a
except Exception as __e:
    print("Occurred", type(__e), __e)

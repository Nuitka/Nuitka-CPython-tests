# Minimal tests for dis module

from test.test_support import run_unittest
import unittest
import sys
import dis
import StringIO

# Nuitka: Removed test parts that relied on correct "co_codelines" tables, which
# we won't have.


def bug708901():
    for res in range(1,
                     10):
        pass

def bug1333982(x=[]):
    assert 0, ([s for s in x] +
              1)
    pass


_BIG_LINENO_FORMAT = """\
%3d           0 LOAD_GLOBAL              0 (spam)
              3 POP_TOP
              4 LOAD_CONST               0 (None)
              7 RETURN_VALUE
"""

class DisTests(unittest.TestCase):
    def do_disassembly_test(self, func, expected):
        s = StringIO.StringIO()
        save_stdout = sys.stdout
        sys.stdout = s
        dis.dis(func)
        sys.stdout = save_stdout
        got = s.getvalue()
        # Trim trailing blanks (if any).
        lines = got.split('\n')
        lines = [line.rstrip() for line in lines]
        expected = expected.split("\n")
        import difflib
        if expected != lines:
            self.fail(
                "events did not match expectation:\n" +
                "\n".join(difflib.ndiff(expected,
                                        lines)))

    def test_opmap(self):
        self.assertEqual(dis.opmap["STOP_CODE"], 0)
        self.assertIn(dis.opmap["LOAD_CONST"], dis.hasconst)
        self.assertIn(dis.opmap["STORE_NAME"], dis.hasname)

    def test_opname(self):
        self.assertEqual(dis.opname[dis.opmap["LOAD_FAST"]], "LOAD_FAST")

    def test_boundaries(self):
        self.assertEqual(dis.opmap["EXTENDED_ARG"], dis.EXTENDED_ARG)
        self.assertEqual(dis.opmap["STORE_NAME"], dis.HAVE_ARGUMENT)

    def test_dis(self):
        self.do_disassembly_test(_f, dis_f)

    def test_bug_708901(self):
        self.do_disassembly_test(bug708901, dis_bug708901)

    def test_big_linenos(self):
        def func(count):
            namespace = {}
            func = "def foo():\n " + "".join(["\n "] * count + ["spam\n"])
            exec func in namespace
            return namespace['foo']

        # Test all small ranges
        for i in xrange(1, 300):
            expected = _BIG_LINENO_FORMAT % (i + 2)
            self.do_disassembly_test(func(i), expected)

        # Test some larger ranges too
        for i in xrange(300, 5000, 10):
            expected = _BIG_LINENO_FORMAT % (i + 2)
            self.do_disassembly_test(func(i), expected)

def test_main():
    run_unittest(DisTests)


if __name__ == "__main__":
    test_main()

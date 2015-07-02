#!/usr/bin/env python3.4

from __future__ import print_function

import os, sys, subprocess

# Go its own directory, to have it easy with path knowledge.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

search_mode = len( sys.argv ) > 1 and sys.argv[1] == "search"

start_at = sys.argv[2] if len( sys.argv ) > 2 else None

if start_at:
    active = False
    start_at = start_at.replace("/", os.path.sep)
else:
    active = True

if "PYTHON" not in os.environ:
    os.environ["PYTHON"] = sys.executable

# Make sure we flush after every print, the "-u" option does more than that
# and this is easy enough.
def my_print(*args, **kwargs):
    print(*args, **kwargs)

    sys.stdout.flush()

reportSkip = my_print

def check_output(*popenargs, **kwargs):
    from subprocess import Popen, PIPE, CalledProcessError

    if 'stdout' in kwargs:
        raise ValueError('stdout argument not allowed, it will be overridden.')
    process = Popen(stdout=PIPE, *popenargs, **kwargs)
    output, unused_err = process.communicate()
    retcode = process.poll()
    if retcode:
        cmd = kwargs.get("args")
        if cmd is None:
            cmd = popenargs[0]
        raise CalledProcessError(retcode, cmd, output=output)
    return output

version_output = check_output(
    [os.environ["PYTHON"], "--version"],
    stderr = subprocess.STDOUT
)

python_version = version_output.split()[1]

if sys.version.startswith("3"):
    python_version = python_version.decode()

os.environ[ "NUITKA_EXTRA_OPTIONS" ] = \
  os.environ.get("NUITKA_EXTRA_OPTIONS", "") + \
  " --recurse-none"

my_print("Using concrete python", python_version)

def checkPath(filename, path):
    global active

    extra_flags = [
        "silent",
        "remove_output",
        # Import test_support which won't be included and potentially others.
        "binary_python_path",
        # Ignore warnings about missing imports
        "ignore_warnings",
        # Keep us informed about timing, even if concurrent runs spoil the
        # accuracy.
        "timing",
        # Use the original __file__ value, at least one case warns about things
        # with filename included.
        "original_file"
    ]

    # Avoid memory runaway of CPython2.
    if path == "doctest_generated/test_itertools.py" and python_version < "3":
        reportSkip("This triggers memory error with CPython2.x", os.path.dirname(path), filename)
        return

    if python_version < "3":
        # Order of syntax errors found is not the same. Encoding errors often
        # overtake print function despite it being statement in Python2 errors-
        if filename in ("test_locale.py", "test_xml_etree.py",
                        "test_getpass.py", "test_hash.py",
                        "test_warnings.py", "test_configparser.py"):
            extra_flags.append("ignore_stderr")

    if "doctest_generated" in path:
        if python_version >= "3.4":
            extra_flags.append("expect_success")

        if filename == "test_generators.py":
            extra_flags.append("ignore_stderr")

            # On Windows with 32 bit, the MemoryError breaks the test
            if os.name == "nt":
                my_print("Skipping", path, "not enough memory with 32 bits.")
                return
    else:
        # TODO: Deprecation warnings for some unknown reason. Need to find
        # out why we don't successfully disable it.
        if filename == "test_shutil.py":
            extra_flags.append("ignore_stderr")

    # TODO: These don't compile in debug mode yet, due to missing optimization
    if "--debug" in os.environ["NUITKA_EXTRA_OPTIONS"]:
        if filename in ("test_grammar.py",):
            my_print("Skipping (due to warnings issue)", path)
            return

    # TODO: This deadlocks, likely a threading problem.
    if python_version >= "3.4" and \
       filename == "test_concurrent_futures.py":
        my_print("Skipping (due to threading issue)", path)
        return

    # TODO: This fails to compiler, super is not fully solved.
    if python_version >= "3.4" and \
       filename == "test_super.py":
        my_print("Skipping (due to compilation issue)", path)
        return

    # TODO: The output from cgit attempts to access locals not in the frame,
    # probably due to chaining problems from above.
    if filename == "test_cgitb.py":
        my_print("Skipping (due to traceback issue)", path)
        return

    # TODO: This fails to compile, super is not fully solved.
    if python_version < "3.4":
        if filename in ("test_contextlib.py", "test_format.py",
                        "test_poplib.py", "test_pickle.py",
                        "test_exceptions.py"):
            my_print("Skipped, CPython bug old versions.")
            return

        if filename == "test_docxmlrpc.py":
            my_print("Skipped, older CPython gives random port outputs.")
            return

        if filename == "test_sched.py":
            my_print("Skipped, older CPython gives random time stamps.")
            return

        if filename == "test_scope.py":
            my_print("Skipped, older CPython fails test that Nuitka passes.")
            return

        if filename == "test_pkg.py":
            my_print("Skipped, older CPython fails test with random output.")
            return

        if filename == "test_urllib.py":
            my_print("Skipped, older CPython fails test with random output.")
            return

        if filename == "test_strftime.py":
            my_print("Skipped, older CPython bug causes crash.")
            return

        if filename == "test_super.py":
            my_print("Skipped, older CPython bug causes crash.")
            return

        if filename == "test_xml_etree_c.py":
            my_print("Skipped, older CPython bug causes crash.")
            return

        if filename == "test_pep277.py":
            my_print("Skipped, older CPython has divergent unicode warning.")
            return

    result = subprocess.call(
        "%s %s %s %s" % (
            sys.executable,
            os.path.join("..", "..", "bin", "compare_with_cpython"),
            path,
            " ".join(extra_flags)
        ),
        shell = True
    )

    if result != 0 and search_mode:
        sys.exit(result)

def checkDir(directory):
    global active

    for filename in sorted(os.listdir(directory)):
        if not filename.endswith(".py") or not filename.startswith("test_"):
            continue

        if filename == "test_support.py":
            continue

        path = os.path.join( directory, filename )

        if not active and start_at in ( filename, path ):
            active = True

        if active:
            checkPath(filename, path)
        else:
            my_print("Skipping", path)

checkDir("test")
checkDir("doctest_generated")

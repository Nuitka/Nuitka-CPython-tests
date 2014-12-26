#!/usr/bin/env python3.2

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
    [ os.environ["PYTHON"], "--version" ],
    stderr = subprocess.STDOUT
)

python_version = version_output.split()[1]

os.environ[ "NUITKA_EXTRA_OPTIONS" ] = \
  os.environ.get( "NUITKA_EXTRA_OPTIONS", "" ) + \
  " --recurse-none"

my_print("Using concrete python", python_version)

def checkPath( filename, path ):
    global active

    extra_flags = [
        "silent",
        "remove_output",
        # Import test_support which won't be included and potentially others.
        "binary_python_path",
        # Ignore warnings about missing imports
        "ignore_warnings",
    ]

    if path == "test" + os.path.sep + "test_shelve.py":
        extra_flags.append("ignore_stderr")

    if python_version < b"3" and \
       filename in ("test_locale.py", "test_nntplib.py", \
                    "test_sys_settrace.py", "test_warnings.py",
                    "test_xml_etree.py"):
        extra_flags.append("ignore_stderr")

    # Deprecation warnings on wrong lines.
    if python_version >= b"3.3" and \
       filename in ("test_smtpd.py", "test_unicode.py"):
        my_print("Skipping (warning output with wrong line)", path)
        return

    if python_version >= b"3.4" and \
       filename in ("test_ast.py", "test_base64.py", "test_cmd_line_script.py"):
        return

    if python_version >= b"3.2" and python_version < b"3.3" and os.name == "nt":
        if filename in ("test_ast.py", "test_descr.py", "test_imp.py",
                        "test_json.py", "test_os.py", "test_pickle.py",
                        "test_pickletools.py", "test_time.py"):
            my_print("Skipping (crashes CPython on Windows)", path)
            return

        if filename == "test_pep3120.py":
            my_print("Skipping (crashes CPython compiled the file on Windows)", path)
            return

        if filename in ("test_exceptions.py", "test_keywordonlyarg.py",
                        "test_raise.py"):
            my_print("Skipping (the CPython fails more on Windows)", path)
            return

        if filename == "test_range.py":
            my_print("Skipping (crashes for unknown reason on Windows with MSVC only)", path)
            return

    if "doctest_generated" in path:
        if python_version >= b"3":
            extra_flags.append("expect_success")

        if filename == "test_generators.py":
            extra_flags.append("ignore_stderr")

            # On Windows with 32 bit, the MemoryError breaks the test
            if os.name == "nt":
                my_print("Skipping", path, "not enough memory with 32 bits.")
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

    for filename in sorted(os.listdir( directory )):
        if not filename.endswith(".py") or not filename.startswith("test_"):
            continue

        if filename == "test_support.py":
            continue

        path = os.path.join(directory, filename)

        if not active and start_at in (filename, path):
            active = True

        # This goes havoc on memory consumption.
        if filename == "test_itertools.py" and directory == "doctest_generated" and python_version < b"3":
            continue

        if active:
            checkPath( filename, path )
        else:
            my_print("Skipping", path)

checkDir("test")
checkDir("doctest_generated")

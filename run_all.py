#!/usr/bin/env python

from __future__ import print_function

import os, sys, subprocess

# Go its own directory, to have it easy with path knowledge.
os.chdir( os.path.dirname( os.path.abspath( __file__ ) ) )

search_mode = len( sys.argv ) > 1 and sys.argv[1] == "search"

start_at = sys.argv[2] if len( sys.argv ) > 2 else None

if start_at:
    active = False
else:
    active = True

if "PYTHON" not in os.environ:
    os.environ[ "PYTHON" ] = "python" if os.name != "nt" else sys.executable

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
    [ os.environ[ "PYTHON" ], "--version" ],
    stderr = subprocess.STDOUT
)

python_version = version_output.split()[1]

os.environ[ "NUITKA_EXTRA_OPTIONS" ] = \
  os.environ.get( "NUITKA_EXTRA_OPTIONS", "" ) + \
  " --recurse-none"

print( "Using concrete python", python_version )

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
        extra_flags.append( "ignore_stderr" )

    if python_version < b"3" and \
       filename in ( "test_locale.py", "test_nntplib.py", \
                     "test_sys_settrace.py", "test_warnings.py",
                     "test_xml_etree.py" ):
        extra_flags.append( "ignore_stderr" )

    if "doctest_generated" in path:
        if python_version >= b"3":
            extra_flags.append( "expect_success" )

        if filename == "test_generators.py":
            extra_flags.append( "ignore_stderr" )

    result = subprocess.call(
        "%s %s %s %s" % (
            sys.executable,
            os.path.join( "..", "..", "bin", "compare_with_cpython" ),
            path,
            " ".join( extra_flags )
        ),
        shell = True
    )

    if result != 0 and search_mode:
        sys.exit( result )

def checkDir( directory ):
    global active

    for filename in sorted( os.listdir( directory ) ):
        if not filename.endswith( ".py" ) or not filename.startswith( "test_" ):
            continue

        if filename == "test_support.py":
            continue

        path = os.path.join( directory, filename )

        if not active and start_at in ( filename, path ):
            active = True

        # This goes havoc on memory consumption.
        if filename == "test_itertools.py" and directory == "doctest_generated" and python_version < b"3":
            continue

        if active:
            checkPath( filename, path )
        else:
            print( "Skipping", path )

checkDir( "test" )
checkDir( "doctest_generated" )

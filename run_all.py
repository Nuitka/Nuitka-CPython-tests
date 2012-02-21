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
    os.environ[ "PYTHON" ] = "python"

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

os.environ[ "PYTHONPATH" ] = os.getcwd()
os.environ[ "NUITKA_EXTRA_OPTIONS" ] = os.environ.get( "NUITKA_EXTRA_OPTIONS", "" ) + " --execute-with-pythonpath --recurse-none"

print( "Using concrete python", python_version )

def checkPath( filename, path ):
    global active

    extra_flags = [ "silent", "exec_in_tmp" ]

    if filename in ( "test_import.py", "test_importhooks.py", "test_pkgimport.py", "test_py3kwarn.py", "test_runpy.py", "test_zipimport.py" ):
        # These will given the __import__ not resolved warning and there won't be anything
        # to ever change that.
        extra_flags.append( "ignore_stderr" )
    elif filename in ( "test_fork1.py", "test_pyclbr.py", "test_scriptpackages.py", "test_uuid.py" ):
        # These will given the __import__ not resolved warning, but they ought to go away.
        extra_flags.append( "ignore_stderr" )
    elif python_version < b"2.7" and filename == "test_strop.py":
        extra_flags.append( "ignore_stderr" )
    elif python_version >= b"2.7" and filename in ( "test_xml_etree.py", "test_xml_etree_c.py" ):
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

        if active:
            checkPath( filename, path )
        else:
            print( "Skipping", path )

checkDir( "test" )
checkDir( "doctest_generated" )

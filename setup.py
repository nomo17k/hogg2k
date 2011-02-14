#!/usr/bin/env python
import os, sys

# BEFORE importing distutils, remove MANIFEST. distutils doesn't
# properly update it when the contents of directories change.
if os.path.exists('MANIFEST'): os.remove('MANIFEST')

from distutils.core import setup, Extension


version = '0.2'
__version__ = version


if (not hasattr(sys, 'version_info')
    or sys.version_info < (2, 4, 4, 'final', 0)):
    raise SystemExit, 'Python 2.4.4 or later required.'


def add_user_options():
    """Add user options"""
    if "--help" in sys.argv:
        print 
        print ' options:'
        print '--local=<dir> same as setting both'
        print '  --install-lib=<dir>/lib/pythonX.X/site-packages and'
        print '  --install-script=<dir>/bin'
    for a in sys.argv:
        if a.startswith('--local='):
            instdir = a.split('=')[1]
            # Figure out the site-packages path.
            pyversion = ('%d.%d' % tuple(sys.version_info[0:2]))
            libpath = ('%s/lib/python%s/site-packages' % (instdir, pyversion))
            sys.argv.extend(['--install-lib=%s' % libpath,
                             '--install-script=%s/bin' % instdir])
            sys.argv.remove(a)


def main():
    add_user_options()

    setup(name='hogg2k',
          version=version,
          description='hogg2k by Taro Sato',
          author='Taro Sato',
          author_email='nomo17k@gmail.com',
          maintainer='Taro Sato',
          maintainer_email='nomo17k@gmail.com',
          url='',
          download_url='',
          license='GPL',
          platforms=['Linux'],
          #packages=['hogg2k'],
          py_modules = ['hogg2k'],
          #package_dir={'hogg2k': 'lib/hogg2k'},
          #scripts=[],
          #ext_modules=[]
          )


if __name__ == "__main__":
    main()


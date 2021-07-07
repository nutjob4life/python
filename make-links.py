# encoding: utf-8

import os, sys

_filter = frozenset([
    '.',
    '..',
    '__pycache__',
    'activate',
    'activate.csh',
    'activate.fish',
    'Activate.ps1',
    'pip',
    'pip3',
    'pip3.9',
    'python',
    'python3',
    'python3.9',
])


def main():
    if not os.path.isfile('pyvenv.cfg') or not os.path.isdir('bin'):
        print('⚠️ Please run this from the virtual environment for the Python Junk Drawer')
        sys.exit(1)
    here = os.path.join(os.path.abspath('.'), 'bin')
    home = os.path.join(os.path.abspath(os.environ['HOME']), 'bin')
    for fn in os.listdir(here):
        if fn in _filter: continue
        source, target = os.path.join(here, fn), os.path.join(home, fn)
        if os.path.isfile(target):
            os.remove(target)
        os.symlink(source, target)
    sys.exit(0)


if __name__ == '__main__':
    main()

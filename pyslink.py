"""Soft link a file/directory with python site-packages directory"""
import os
import subprocess
import sys
from distutils.sysconfig import get_python_lib

__version__ = "0.4.0"


def sh(command: str) -> str:
    return subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        universal_newlines=True,
    ).communicate()[0]


def main() -> int:
    argv = sys.argv
    if len(argv) > 1 and len(argv) < 3:
        path = argv[1]
    else:
        print("requires one positional parameters")
        return 1

    pylib = get_python_lib()
    original = os.path.abspath(path)
    path, target = os.path.split(original)
    dest = os.path.join(pylib, target)
    #
    print(sh("ln -sfnv %s %s" % (original, dest)))
    #
    setup = os.path.join(path, "setup.py")
    if os.path.isfile(setup):
        eggdir = None
        current = os.getcwd()
        try:
            os.chdir(path)
            print(sh("%s setup.py egg_info" % sys.executable))
            for name in os.listdir(path):
                if name.endswith(".egg-info"):
                    eggdir = name
                    break
        finally:
            os.chdir(current)

        if eggdir:
            original = os.path.join(path, eggdir)
            dest = os.path.join(pylib, eggdir)
            print(sh("ln -sfnv %s %s" % (original, dest)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

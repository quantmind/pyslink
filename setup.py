from setuptools import setup, find_packages

import pylink as mod


def read(name):
    with open('./%s' % name, 'r') as f:
        return f.read()


def run():

    setup(name='pylink',
          version=mod.__version__,
          author='Luca Sbardella',
          description=mod.__doc__,
          license='BSD',
          long_description=read('README.md'),
          packages=find_packages(),
          include_package_data=True,
          zip_safe=False,
          scripts=['bin/luxmake.py'],
          classifiers=[
              'Development Status :: 4 - Beta',
              'Intended Audience :: Developers',
              'License :: OSI Approved :: BSD License',
              'Operating System :: OS Independent',
              'Programming Language :: Python',
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 3.4',
              'Programming Language :: Python :: 3.5',
              'Topic :: Utilities',
              'Topic :: Software Development :: Libraries :: Python Modules'],
          entry_points={
              'console_scripts': [
                  "pylink = pylink:main"
              ]
          })


if __name__ == '__main__':
    run()

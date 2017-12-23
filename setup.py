from setuptools import setup

import pyslink as mod


def read(name):
    with open('./%s' % name, 'r') as f:
        return f.read()


def run():

    setup(name='pyslink',
          version=mod.__version__,
          author='Luca Sbardella',
          author_email="luca@quantmind.com",
          url="https://github.com/quantmind/pyslink",
          description=mod.__doc__,
          license='BSD',
          long_description=read('README.rst'),
          py_modules=['pyslink'],
          zip_safe=False,
          classifiers=[
              'Development Status :: 5 - Production/Stable',
              'Intended Audience :: Developers',
              'License :: OSI Approved :: BSD License',
              'Operating System :: OS Independent',
              'Programming Language :: Python',
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 3.4',
              'Programming Language :: Python :: 3.5',
              'Programming Language :: Python :: 3.6',
              'Topic :: Utilities',
              'Topic :: Software Development :: Libraries :: Python Modules'],
          entry_points={
              'console_scripts': [
                  "pyslink = pyslink:main"
              ]
          })


if __name__ == '__main__':
    run()

from setuptools import setup

setup(name='conc_edgefilter',
      version='1.0',
      description='Takes the ice-concentration and -edge OSI SAF products '
                  'and produces a filtered ice-concentration product, where '
                  'the ice-concentration is set to zero outside of the ice edge.',
      author='John Lavelle',
      author_email='jol@dmi.dk',
      install_requires=['docopt', 'netCDF4']
      )
from setuptools import setup, find_packages

VERSION = '0.2'

setup(name='upsearch',
      version=VERSION,
      description="App for finding file in nearest parent folder",
      author='Vladimir Iakovlev',
      author_email='nvbn.rm@gmail.com',
      url='https://github.com/nvbn/upsearch',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples',
                                      'tests', 'release']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['pathlib'],
      entry_points={'console_scripts': [
          'upsearch = upsearch.main:main']})

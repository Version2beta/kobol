from distutils.core import setup

setup(
    name='kobol',
    version='0.0.1',
    author=['Rob Martin @version2beta', 'Miranda Handley @PhoenixToFlame'],
    author_email=['rob@version2beta.com', 'miranda@mirandahandley.com'],
    packages=['kobol'],
    scripts=[],
    url='http://pypi.python.org/pypi/kobol/',
    license='LICENSE.txt',
    description='A static site generator for Python.',
    long_description=open('README.rst').read(),
    install_requires=[
      'flask',
      'jinja2',
      'flask_frozen',
      'pygments',
      'boto',
      'PyYAML',
      'unittest',
      'expecter',
      'dingus'
    ],
    package_data={
        '': ['*.dist'],
        '': ['src/tests/support'],
        '': ['src/skel'],
      },
    entry_points={
        'console_scripts': [
          'kobol = kobol:main',
        ],
      },
)

from distutils.core import setup

setup(
    name='Algorythm',
    version='0.1.0',
    author='Lucky ME',
    author_email='nothing@example.com',
    packages=['algorythm'],
#    scripts=['bin/stowe-towels.py','bin/wash-towels.py'],
    url='http://pypi.python.org/pypi/Algorythm/',
    license='LICENSE.txt',
    description='Useful Algorythm-related stuff.',
    long_description=open('README.txt').read(),
    install_requires=[
        "Django >= 1.1.1",
        "caldav == 0.1.4",
    ],
)

